from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime
import random
import uvicorn
import time

app = FastAPI(title="Market Sentiment API")

# MongoDB connection with retry logic
def connect_mongodb():
    max_retries = 5
    for i in range(max_retries):
        try:
            print(f"Attempting MongoDB connection (try {i+1}/{max_retries})...")
            client = MongoClient(
                "mongodb://admin:password123@mongodb:27017/",
                serverSelectionTimeoutMS=5000,
                connectTimeoutMS=5000
            )
            # Test connection
            client.admin.command('ping')
            db = client["market_data"]
            print("✅ MongoDB connected successfully!")
            return db
        except Exception as e:
            print(f"❌ MongoDB connection failed: {e}")
            if i < max_retries - 1:
                print(f"Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Starting without MongoDB.")
                return None
    return None

# Connect to MongoDB
db = connect_mongodb()

# Routes
@app.get("/")
def root():
    db_status = "connected" if db is not None else "disconnected"
    return {
        "message": "Market Sentiment API", 
        "status": "running",
        "mongodb": db_status
    }

@app.get("/health")
def health():
    db_status = "connected" if db is not None else "disconnected"
    return {
        "status": "healthy", 
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_status
    }

@app.get("/generate-sample")
def generate_sample():
    """Generate sample market data"""
    if db is None:
        return {"error": "Database not connected", "data": None}
    
    tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NVDA"]
    
    data = {
        "ticker": random.choice(tickers),
        "price": round(random.uniform(100, 500), 2),
        "change": round(random.uniform(-5, 5), 2),
        "volume": random.randint(10000, 1000000),
        "sentiment": round(random.uniform(-1, 1), 3),
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        # Insert into MongoDB
        result = db.sample_data.insert_one(data.copy())
        data["_id"] = str(result.inserted_id)
        
        return {
            "message": "Sample data generated",
            "data": data,
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "data": None,
            "success": False
        }

@app.get("/get-data")
def get_data(limit: int = 100):
    """Get all stored data"""
    if db is None:
        return {"error": "Database not connected", "data": [], "count": 0}
    
    try:
        # Get data from MongoDB
        cursor = db.sample_data.find().sort("timestamp", -1).limit(limit)
        data = list(cursor)
        
        # Convert ObjectId to string
        for item in data:
            item["_id"] = str(item["_id"])
        
        return {
            "count": len(data),
            "data": data,
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "data": [],
            "count": 0,
            "success": False
        }

@app.get("/summary")
def summary():
    """Get summary statistics"""
    if db is None:
        return {"error": "Database not connected", "summary": [], "success": False}
    
    try:
        # Simple summary
        all_data = list(db.sample_data.find())
        
        if not all_data:
            return {"summary": [], "success": True, "message": "No data yet"}
        
        # Manual grouping (simpler than aggregation)
        ticker_data = {}
        for item in all_data:
            ticker = item.get("ticker", "Unknown")
            if ticker not in ticker_data:
                ticker_data[ticker] = {
                    "prices": [],
                    "sentiments": [],
                    "count": 0
                }
            
            ticker_data[ticker]["prices"].append(item.get("price", 0))
            ticker_data[ticker]["sentiments"].append(item.get("sentiment", 0))
            ticker_data[ticker]["count"] += 1
        
        # Format results
        formatted = []
        for ticker, data in ticker_data.items():
            if data["prices"]:
                formatted.append({
                    "ticker": ticker,
                    "avg_price": round(sum(data["prices"]) / len(data["prices"]), 2),
                    "avg_sentiment": round(sum(data["sentiments"]) / len(data["sentiments"]), 3),
                    "latest_price": data["prices"][-1] if data["prices"] else 0,
                    "count": data["count"],
                    "prices": data["prices"]
                })
        
        return {
            "summary": formatted,
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "summary": [],
            "success": False
        }

# Startup event
@app.on_event("startup")
def startup_db_client():
    print("🚀 Starting up Market Sentiment API...")
    if db is not None:
        try:
            # Create collection if it doesn't exist
            collections = db.list_collection_names()
            if "sample_data" not in collections:
                db.create_collection("sample_data")
                print("✅ Created 'sample_data' collection")
            
            # Create index for faster queries
            db.sample_data.create_index([("timestamp", -1)])
            print("✅ Created timestamp index")
            
            print("✅ Startup complete")
        except Exception as e:
            print(f"⚠️ Startup error: {e}")

if __name__ == "__main__":
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)