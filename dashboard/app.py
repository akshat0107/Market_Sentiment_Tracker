import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime
import json


st.set_page_config(
    page_title = "Market Sentiment Tracker",
    page_icon="📈",
    layout = "wide"
)

if 'data' not in st.session_state:
    st.session_state.data = []

if 'last_update' not in st.session_state:
    st.session_state.last_update = datetime.now()

st.title("Market Sentiment Tracker")
st.markdown("Real-time market data with sentiment analysis")

st.sidebar.header("Controls")
api_url = st.sidebar.text_input("API URL","http://fastapi-backend:8000")
auto_refresh = st.sidebar.checkbox("Auto-refresh (10s)",True)
refresh_btn = st.sidebar.button("Manual Refresh")

def fetch_data():
    try:
        response = requests.get(f"{api_url}/get-data",params={"limit":50})
        if response.status_code==200:
            return response.json()["data"]
        
    except:
        return []
    
    return []

def fetch_summary():
    try:
        response = requests.get(f"{api_url}/summary")
        if response.status_code == 200:
            return response.json()["summary"]
    except:
        return []
    return []

def generate_sample():
    try:
        response = requests.get(f"{api_url}/generate-sample")
        return response.status_code == 200
    except:
        return False
    
col1,col2,col3 = st.columns(3)

with col1:
    if st.button("Generate Sample data"):
        if generate_sample():
            st.success("Sample data generated")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Failed to generate data")

with col2:
    if refresh_btn:
        st.session_state.data = fetch_data()
        st.session_state.last_update = datetime.now()
        st.rerun()

with col3:
    # st.metric("Last Updated ",st.session_state.last_update.strftime("%Y-%m-%d %H:%M:%S"))
    st.write("Last updated:\n")
    st.markdown(
    f'<p style="font-size: 20px;">{st.session_state.last_update.strftime("%Y-%m-%d %H:%M:%S")}</p>', 
    unsafe_allow_html=True
)

if not st.session_state.data or refresh_btn:
    st.session_state.data = fetch_data()

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    tab1,tab2,tab3 = st.tabs(["Dashboard","Charts","Raw Data"])

    with tab1:
        st.subheader("Market Overview")
        summary = fetch_summary()
        if summary:
            summary_df = pd.DataFrame(summary)
            tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NVDA"]
            symbol = st.sidebar.selectbox("Select a stock symbol: ",tickers,index=2)

            if symbol:
                stock_data = summary_df[summary_df["ticker"]==symbol]

                col_st, col_sentiment = st.columns(2)

                if stock_data is not None:
                    # for idx,(_,row) in enumerate(summary_df.iterrows()):
                    #     with cols[idx]:
                    #         sentiment_color = "green" if row['avg_sentiment']>0 else "red" if row['avg_sentiment']<0 else "gray"
                            
                    #         st.metric(
                    #             label=row['ticker'],
                    #             value = f"${row['latest_price']:.2f}",
                    #             delta = f"{row['avg_sentiment']:.3f} sentiment"
                    #         )
                    
                        sentiment_color = "green" if stock_data.iloc[0]['avg_sentiment']>0 else "red" if stock_data.iloc[0]['avg_sentiment']<0 else "gray"
                        st.metric(label = stock_data.iloc[0]['ticker'],value = f"{stock_data.iloc[0]['latest_price']:.2f}",delta = f"{stock_data.iloc[0]['avg_sentiment']:.3f}")
                else:
                    st.warning(f"No data available for {symbol}.")
                    
                st.subheader(f"10 data points from latest data for {symbol}")
                recent_df = df[df['ticker']==symbol].sort_values('timestamp')
                st.dataframe(recent_df[['ticker','price','sentiment','timestamp']],width=600,height=400,hide_index=True) 

                st.subheader("Line chart")
                st.line_chart(recent_df,y='price',x='timestamp')
            
    with tab2:
        st.subheader("Interactive charts")

        fig1 = go.Figure()

        for ticker in df['ticker'].unique():
            ticker_df = df[df['ticker']==ticker].sort_values('timestamp')
            fig1.add_trace(
                go.Scatter(
                    x=ticker_df['timestamp'],
                    y=ticker_df['price'],
                    name=ticker,
                    mode = 'lines+markers'
                )
            )
        fig1.update_layout(
            title = "Stock Prices over time",
            xaxis_title = "Time",
            yaxis_title = "Price ($)",
            hovermode = 'x unified'
        )

        st.plotly_chart(fig1,use_container_width=True)

        if 'sentiment' in df.columns:
            fig2 = go.Figure()

            for ticker in df['ticker'].unique():
                ticker_df = df[df['ticker']==ticker]
                fig2.add_trace(go.Box(
                    y=ticker_df['sentiment'],
                    name=ticker,
                    boxpoints='all'
                ))
            
            fig2.update_layout(
                title="Sentiment Distribution by Ticker",
                yaxis_title="Sentiment Score",
                xaxis_title="Ticker"
            )
            
            st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.subheader("Raw Data")
        st.dataframe(df,use_container_width=True)

        with st.expander("Data Statistics"):
            st.write(df.describe())

else:
    st.info("No data available. Click 'Generate Sample Data' to start.")


st.sidebar.markdown("---")
st.sidebar.markdown('### System Status')

try:
    health = requests.get(f"{api_url}/health")
    if health.status_code==200:
        st.sidebar.success("API connected")

    else:
        st.sidebar.error("API disconnected")
except:
    st.sidebar.error("Cannot reach API")

st.sidebar.markdown(f"Data Points: {len(st.session_state.data)}")

if auto_refresh:
    time.sleep(10)
    st.rerun()

    

