📈 Market Sentiment Tracker
A real-time market sentiment analysis dashboard with FastAPI backend, Streamlit frontend, and MongoDB database. Generate simulated stock data with sentiment scores and visualize market trends through interactive charts.

https://via.placeholder.com/800x400?text=Market+Sentiment+Tracker+Dashboard

✨ Features
Real-time Data Generation - Create simulated market data with sentiment scores

Interactive Dashboard - Visualize stock prices and sentiment trends

Multi-stock Support - Track AAPL, GOOGL, MSFT, TSLA, AMZN, META, NVDA

Sentiment Analysis - Monitor sentiment scores (-1 to 1) for market psychology

RESTful API - Well-documented FastAPI backend

MongoDB Integration - Persistent data storage with optimized indexes

Docker Support - Easy deployment with containerization

Responsive Design - Works on desktop and mobile devices

🏗️ Architecture
text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Streamlit  │────▶│   FastAPI   │────▶│   MongoDB   │
│  Dashboard  │◀────│   Backend   │◀────│  Database   │
└─────────────┘     └─────────────┘     └─────────────┘
      Port              Port                Port
      8501              8000               27017
Technology Stack
Component	Technology	Purpose
Frontend	Streamlit	Interactive dashboard UI
Backend	FastAPI	REST API server
Database	MongoDB	Data persistence
Charts	Plotly	Interactive visualizations
Container	Docker	Deployment & isolation
Language	Python 3.9+	Core programming
📋 Prerequisites
Docker Desktop (v20.10+)

Git (v2.30+)

Python 3.9+ (optional, for local development)

4GB+ RAM allocated to Docker

🚀 Quick Start (Docker Compose)
1. Clone the Repository
bash
git clone https://github.com/yourusername/market-sentiment-tracker.git
cd market-sentiment-tracker
2. Create Docker Compose File
yaml
# docker-compose.yml
version: '3.8'

services:
  mongodb:
    image: mongo:6.0
    container_name: mongodb
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password123
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    networks:
      - sentiment-network

  backend:
    build: ./backend
    container_name: fastapi-backend
    depends_on:
      - mongodb
    ports:
      - "8000:8000"
    networks:
      - sentiment-network

  dashboard:
    build: ./dashboard
    container_name: streamlit-dashboard
    depends_on:
      - backend
    ports:
      - "8501:8501"
    networks:
      - sentiment-network

volumes:
  mongodb_data:

networks:
  sentiment-network:
    driver: bridge
3. Start the Application
bash
docker-compose up -d
4. Access the Services
Service	URL	Credentials
Dashboard	http://localhost:8501	None
API Docs	http://localhost:8000/docs	None
API Health	http://localhost:8000/health	None
MongoDB	mongodb://localhost:27017	admin/password123
5. Generate Sample Data
Open dashboard at http://localhost:8501

Click "Generate Sample Data" button

View real-time charts and metrics

🛠️ Manual Installation (Without Docker)
Backend Setup
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start MongoDB (via Docker or local)
docker run -d --name mongodb -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:6.0

# Start FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Dashboard Setup
bash
# Navigate to dashboard directory
cd dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Streamlit app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
📁 Project Structure
text
market-sentiment-tracker/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile          # Backend container config
│   └── README.md           # Backend documentation
├── dashboard/
│   ├── app.py              # Streamlit dashboard
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile         # Dashboard container config
│   └── README.md          # Dashboard documentation
├── mongo-init.js          # MongoDB initialization script
├── docker-compose.yml     # Multi-container setup
├── .gitignore            # Git ignore rules
└── README.md            # This file

🔌 API Reference

Base URL
http://localhost:8000
Endpoints
Method	Endpoint	Description	Response
GET	/	API welcome message	{message, status, mongodb}
GET	/health	Health check	{status, timestamp, database}
GET	/generate-sample	Generate random market data	{message, data, success}
GET	/get-data	Get stored data (limit: 100)	{count, data, success}
GET	/summary	Get summary statistics	{summary, success}

Example Request
# Generate sample data
curl -X GET "http://localhost:8000/generate-sample"

# Response
{
  "message": "Sample data generated",
  "data": {
    "ticker": "MSFT",
    "price": 462.90,
    "change": 4.84,
    "volume": 992134,
    "sentiment": -0.609,
    "timestamp": "2026-02-11T18:00:25.867418",
    "_id": "697f94b95aa2afd11f8689a3"
  },
  "success": true
}

📊 Data Model
Sample Data Document
{
  "_id": "ObjectId",
  "ticker": "string",        // Stock symbol (AAPL, MSFT, etc.)
  "price": "float",         // Current price in USD
  "change": "float",        // Price change from previous
  "volume": "integer",      // Trading volume
  "sentiment": "float",     // Sentiment score (-1 to 1)
  "timestamp": "datetime"   // ISO format timestamp
}
Alert Document
json
{
  "_id": "ObjectId",
  "message": "string",      // Alert description
  "timestamp": "datetime",  // When alert was triggered
  "acknowledged": "boolean", // Read status
  "severity": "string"     // low, medium, high
}
🎨 Dashboard Features
1. Market Overview
Real-time stock metrics

Sentiment color coding (🟢 positive, 🔴 negative)

Last update timestamp

Manual refresh button

2. Interactive Charts
Price Trends: Line chart with markers

Sentiment Distribution: Box plot visualization

Hover tooltips with detailed data

3. Data Management
Generate sample data on demand

Auto-refresh every 20 seconds

View raw data table

Statistical summaries

4. System Monitoring
API connectivity status

Data point counter

Error handling with user feedback

🐳 Docker Commands
Basic Operations
# Start services
docker-compose up -d

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# View logs
docker-compose logs -f

# Rebuild images
docker-compose up -d --build

Maintenance
# Remove everything (including data)
docker-compose down -v
docker system prune -a

# Check container status
docker-compose ps

# Execute commands in container
docker exec -it fastapi-backend bash
docker exec -it mongodb mongosh -u admin -p password123

🔧 Troubleshooting
Issue 1: "Cannot reach API" in Dashboard
# Check if backend is running
curl http://localhost:8000/health

# Check container logs
docker-compose logs backend

# Common fix: Update API URL in sidebar to http://localhost:8000
Issue 2: MongoDB Connection Failed
# Check MongoDB status
docker-compose ps mongodb

# Test MongoDB connection
docker exec mongodb mongosh --eval "db.adminCommand('ping')"

# Verify credentials in backend/main.py
Issue 3: Port Already in Use
# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8501
kill -9 <PID>
Issue 4: Docker Build Fails
# Clear Docker cache
docker system prune -a

# Rebuild with no cache
docker-compose build --no-cache

# Check Dockerfile syntax
docker run -it --rm --entrypoint bash market_sentiment_tracker-backend

🧪 Testing
API Testing
# Health check
curl http://localhost:8000/health

# Generate 5 sample data points
for i in {1..5}; do
  curl -X GET "http://localhost:8000/generate-sample"
done

# Get all data
curl http://localhost:8000/get-data | json_pp

# Get summary statistics
curl http://localhost:8000/summary | json_pp
Database Testing
javascript
// Connect to MongoDB
docker exec -it mongodb mongosh -u admin -p password123

// Switch to market_data database
use market_data

// Check collections
show collections

// View sample data
db.sample_data.find().pretty()

// Check indexes
db.sample_data.getIndexes()
📈 Performance Optimization
MongoDB Indexes
javascript
// Pre-created for optimal performance
db.sample_data.createIndex({ticker: 1, timestamp: -1})
db.sample_data.createIndex({timestamp: -1})
db.alerts.createIndex({acknowledged: 1})
Docker Resource Allocation
yaml
# docker-compose.yml
services:
  mongodb:
    deploy:
      resources:
        limits:
          memory: 512M
    mem_limit: 512m
  
  backend:
    mem_limit: 256m
  
  dashboard:
    mem_limit: 256m
🔒 Security Considerations
For Production Deployment
Change default credentials

Update MongoDB password

Use environment variables

Enable authentication

Add API key middleware

Implement JWT tokens

Network security

Use internal networks

Limit exposed ports

Add SSL/TLS (HTTPS)

Data validation

Sanitize user inputs

Implement rate limiting

🚢 Production Deployment
Using Docker Swarm
bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml market-tracker

# Scale services
docker service scale market-tracker_backend=3
Using Kubernetes
yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: market-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: market_sentiment_tracker-backend:latest
        ports:
        - containerPort: 8000

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

Development Guidelines
Follow PEP 8 style guide

Write docstrings for functions

Add tests for new features

Update documentation

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

MIT License

Copyright (c) 2026 Market Sentiment Tracker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...

👥 Authors
Akshat Gupta - Initial work - GitHub

🙏 Acknowledgments
FastAPI - Modern web framework

Streamlit - Interactive dashboard framework

Plotly - Interactive visualization library

MongoDB - NoSQL database

Docker - Containerization platform

📚 Additional Resources
FastAPI Documentation

Streamlit Documentation

MongoDB Manual

Docker Documentation

📊 Roadmap
Basic data generation

Interactive charts

Docker support

Real stock market API integration

User authentication

Email alerts

Machine learning predictions

Mobile app

