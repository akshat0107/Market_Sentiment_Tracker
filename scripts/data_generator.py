import requests
import random
import time
from datetime import datetime

API_URL = "http://localhost:8000"

def generate_data(num_points=20):
    print(f"Generating {num_points} data points...")

    for i in range(num_points):
        try:
            response = requests.get(f"{API_URL}/generate-sample")
            if response.status_code==200:
                data = response.json()["data"]
                print(f"{i+1}. Generated: {data['ticker']} @ ${data['price']} "
                      f"(Sentiment: {data['sentiment']})")
            else:
                print(f"Error: API returned {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(0.5)
    
    print("Data generation complete!")

if __name__=="__main__":
    generate_data(20)