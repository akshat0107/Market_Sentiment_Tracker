A real-time market sentiment analysis dashboard with FastAPI backend, Streamlit frontend, and MongoDB database.

🚀 Features
Real-time Data Generation: Generate simulated market data with sentiment scores

Interactive Dashboard: Visualize stock prices and sentiment trends

Sentiment Analysis: Track sentiment scores for various stocks

RESTful API: Fully documented FastAPI backend

MongoDB Integration: Persistent data storage

Docker Support: Easy deployment with Docker containers

📋 Prerequisites
Docker and Docker Compose

Python 3.9+ (for local development)

Git

🛠️ Installation
Using Docker (Recommended)
Clone the repository:

bash
git clone https://github.com/yourusername/market-sentiment-tracker.git
cd market-sentiment-tracker
Start the application:

bash
docker-compose up -d
Access the application:

Dashboard: http://localhost:8501

API Documentation: http://localhost:8000/docs

API Health Check: http://localhost:8000/health

Manual Setup (Development)
Set up MongoDB:

bash
docker run -d --name mongodb -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:6.0
Set up Backend:

bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000
Set up Dashboard:

bash
cd dashboard
pip install -r requirements.txt
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
📁 Project Structure
text
market-sentiment-tracker/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile          # Backend Docker configuration
├── dashboard/
│   ├── app.py              # Streamlit dashboard
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Dashboard Docker configuration
├── docker-compose.yml      # Multi-container setup
└── README.md              # This file
🔧 API Endpoints
Method	Endpoint	Description
GET	/	API welcome message
GET	/health	Health check and database status
GET	/generate-sample	Generate sample market data
GET	/get-data	Retrieve stored data (limit: 100)
GET	/summary	Get summary statistics
📊 Dashboard Features
Market Overview: Real-time metrics for each stock

Interactive Charts:

Price trends over time

Sentiment distribution by ticker

Raw Data View: Complete dataset with filtering

System Status: API and database connectivity status

Auto-refresh: Configurable auto-refresh interval

🐳 Docker Commands
bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart
docker-compose up -d --build

# Check service status
docker-compose ps
🧪 Testing
Test API Connectivity
bash
curl http://localhost:8000/health
Generate Sample Data
bash
curl http://localhost:8000/generate-sample
Get All Data
bash
curl http://localhost:8000/get-data
🔄 Environment Variables
Variable	Description	Default
MONGO_INITDB_ROOT_USERNAME	MongoDB admin username	admin
MONGO_INITDB_ROOT_PASSWORD	MongoDB admin password	password123
API_URL	Backend API URL for dashboard	http://backend:8000
🐛 Troubleshooting
Common Issues
"Cannot reach API" in dashboard

Check if backend container is running: docker ps | grep fastapi-backend

Verify API health: curl http://localhost:8000/health

Ensure containers are on same network

MongoDB connection issues

Check MongoDB logs: docker logs mongodb

Verify credentials in backend/main.py

Port conflicts

Change ports in docker-compose.yml

Check running services: netstat -ano | findstr :8501

Docker build issues

Clear Docker cache: docker system prune -a

Rebuild with no cache: docker-compose build --no-cache

Logs Inspection
bash
# Backend logs
docker logs fastapi-backend

# Dashboard logs
docker logs streamlit-dashboard

# MongoDB logs
docker logs mongodb
📈 Data Model
Each data point includes:

ticker: Stock symbol (e.g., AAPL, MSFT)

price: Current price (USD)

change: Price change from previous

volume: Trading volume

sentiment: Sentiment score (-1 to 1)

timestamp: ISO format timestamp

_id: MongoDB unique identifier

🚢 Deployment
Production Considerations
Security:

Change default MongoDB credentials

Add authentication to API endpoints

Use HTTPS with reverse proxy (Nginx)

Scaling:

Add more backend workers

Implement Redis for caching

Use MongoDB replica sets

Monitoring:

Add health check endpoints

Implement logging with ELK stack

Set up metrics with Prometheus

🤝 Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
FastAPI for the web framework

Streamlit for the dashboard framework

Plotly for interactive charts

MongoDB for data persistence
