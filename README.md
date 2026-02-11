Market Sentiment Tracker

A real-time stock market sentiment analysis dashboard built with FastAPI, Streamlit, and MongoDB. Generate simulated market data with sentiment scores and visualize trends through interactive charts.

Overview

Market Sentiment Tracker is a full-stack microservices application that demonstrates real-time data processing, visualization, and analysis. Built with modern Python frameworks and containerized with Docker, it provides hands-on experience with:

- RESTful API design with FastAPI
- Interactive dashboards with Streamlit
- NoSQL database management with MongoDB
- Microservices architecture with Docker Compose
- Real-time data visualization with Plotly

Features

Core Functionality
- Real-time Data Generation - Simulate market data with randomized prices and sentiment scores
- Multi-Stock Support - Track 7 major tech stocks (AAPL, GOOGL, MSFT, TSLA, AMZN, META, NVDA)
- Interactive Dashboard - Filter stocks, view trends, and analyze sentiment distributions
- RESTful API - Well-documented endpoints with automatic API docs (Swagger UI)
- Persistent Storage - MongoDB with optimized indexes for fast queries

Visualizations
- Price Trends - Multi-line chart showing price movements over time
- Sentiment Analysis - Box plots displaying sentiment distribution
- Market Overview - Real-time metrics with color-coded sentiment indicators
- Data Tables - Interactive tables with sorting and filtering

Technical Features
- Docker Support - One-command deployment with docker-compose
- Auto-refresh - Optional real-time data updates (20-second intervals)
- Error Handling - Robust retry logic and user-friendly error messages
- Database Indexing - Optimized MongoDB queries for performance
- Responsive Design - Works on desktop and mobile devices

Architecture
```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│   Streamlit     │──────▶│    FastAPI      │──────▶│    MongoDB      │
│   Dashboard     │◀──────│    Backend      │◀──────│    Database     │
│   Port: 8501    │       │   Port: 8000    │       │   Port: 27017   │
└─────────────────┘       └─────────────────┘       └─────────────────┘
        │                          │                          │
        │                          │                          │
    Plotly Charts            REST API                  Indexed
    Auto-refresh          Swagger Docs              Collections
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Frontend | Streamlit 1.28.0 | Interactive web dashboard |
| Backend | FastAPI 0.104.1 | REST API server |
| Database | MongoDB 6.0 | Data persistence & storage |
| Visualization | Plotly 5.17.0 | Interactive charts |
| Containerization | Docker & Docker Compose | Deployment & orchestration |
| Language | Python 3.9+ | Core programming language |
| Server | Uvicorn | ASGI web server |

---

Prerequisites

Before you begin, ensure you have:

- Docker Desktop (v20.10+) - [Download here](https://www.docker.com/products/docker-desktop)
- Git (v2.30+) - [Download here](https://git-scm.com/downloads)
- 4GB+ RAM allocated to Docker
- 8GB+ free disk space

Optional (for local development without Docker):
- Python 3.9 or higher
- pip package manager

---

Quick Start (Recommended)

1️. Clone the Repository

```bash
git clone https://github.com/yourusername/market-sentiment-tracker.git
cd market-sentiment-tracker
```

2️. Start All Services

```bash
docker-compose up -d
```

This single command will:
- Pull and build all Docker images
- Start MongoDB database
- Launch FastAPI backend
- Start Streamlit dashboard
- Create persistent volumes

3️. Access the Application

| Service | URL | Description |
|---------|-----|-------------|
| Dashboard | http://localhost:8501 | Main web interface |
| API Documentation | http://localhost:8000/docs | Interactive API docs (Swagger) |
| API Health Check | http://localhost:8000/health | Service status |
| MongoDB | mongodb://localhost:27017 | Database connection |

4️. Generate Sample Data

1. Open the dashboard at http://localhost:8501
2. Click "Generate Sample data" button (multiple times for more data)
3. Select a stock from the sidebar dropdown
4. Explore the charts and metrics!

---

Manual Installation (Without Docker)

Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start MongoDB (using Docker)
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password123 \
  mongo:6.0

# Start FastAPI server
python main.py
# Or with auto-reload:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Dashboard Setup

```bash
# Navigate to dashboard directory
cd dashboard

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Update API URL in the dashboard
# Open app.py and change line 27 to:
# api_url = st.sidebar.text_input("API URL","http://localhost:8000")

# Start Streamlit app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

---

Project Structure

```
market-sentiment-tracker/
├── backend/
│   ├── main.py                 # FastAPI application with 5 endpoints
│   ├── requirements.txt        # Python dependencies (FastAPI, PyMongo)
│   ├── Dockerfile             # Backend container configuration
│   └── README.md              # Backend-specific documentation
│
├── dashboard/
│   ├── app.py                 # Streamlit dashboard application
│   ├── requirements.txt       # Python dependencies (Streamlit, Plotly)
│   ├── Dockerfile            # Dashboard container configuration
│   └── README.md             # Dashboard-specific documentation
│
├── mongo-init/
│   └── init.js               # MongoDB initialization script
│
├── scripts/
│   └── data_generator.py     # Utility script for bulk data generation
│
├── docker-compose.yml        # Multi-container orchestration
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
└── README.md               # This file
```

---

 API Reference

# Base URL
```
http://localhost:8000
```

# Endpoints

1. Root Endpoint
```http
GET /
```

Response:
```json
{
  "message": "Market Sentiment API",
  "status": "running",
  "mongodb": "connected"
}
```

2. Health Check
```http
GET /health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2026-02-11T18:00:00.000000",
  "database": "connected"
}
```

3. Generate Sample Data
```http
GET /generate-sample
```

Response:
```json
{
  "message": "Sample data generated",
  "data": {
    "ticker": "AAPL",
    "price": 432.56,
    "change": 2.45,
    "volume": 876234,
    "sentiment": 0.723,
    "timestamp": "2026-02-11T18:00:00.000000",
    "_id": "507f1f77bcf86cd799439011"
  },
  "success": true
}
```

4. Get Data
```http
GET /get-data?limit=50
```

Parameters:
- `limit` (optional, default: 100) - Maximum number of records to return

Response:
```json
{
  "count": 50,
  "data": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "ticker": "AAPL",
      "price": 432.56,
      "change": 2.45,
      "volume": 876234,
      "sentiment": 0.723,
      "timestamp": "2026-02-11T18:00:00.000000"
    }
    // ... more records
  ],
  "success": true
}
```

5. Get Summary Statistics
```http
GET /summary
```

Response:
```json
{
  "summary": [
    {
      "ticker": "AAPL",
      "avg_price": 345.67,
      "avg_sentiment": 0.234,
      "latest_price": 432.56,
      "count": 25
    }
    // ... more tickers
  ],
  "success": true
}
```

# Interactive API Documentation

FastAPI provides automatic interactive documentation:
- Swagger UI: http://localhost:8000/docs
- ReDo*: http://localhost:8000/redoc

---

Data Model

Sample Data Document
```javascript
{
  "_id": ObjectId,           // MongoDB unique identifier
  "ticker": String,          // Stock symbol (AAPL, GOOGL, etc.)
  "price": Float,           // Current price in USD (100-500)
  "change": Float,          // Price change from previous (-5 to +5)
  "volume": Integer,        // Trading volume (10,000-1,000,000)
  "sentiment": Float,       // Sentiment score (-1 to +1)
  "timestamp": ISODate      // ISO format timestamp
}
```

Sentiment Scale:
- `0.0 to 1.0` - positive sentiment (🟢)
- `-1.0 to 0.0` - negative sentiment (🔴)

Database Indexes

Optimized for query performance:

```javascript
// Compound index for ticker-based time-series queries
db.sample_data.createIndex({ ticker: 1, timestamp: -1 })

// Single index for sorting by time
db.sample_data.createIndex({ timestamp: -1 })
```

---

Dashboard Features

1. Market Overview (Tab 1)
- Stock Selector - Dropdown to choose specific ticker
- Real-time Metrics - Current price and average sentiment
- Recent Data Table - Last 10 data points for selected stock
- Line Chart - Price trend visualization

2. Interactive Charts (Tab 2)
- Multi-Stock Price Chart - Compare all stocks simultaneously
  - Hover tooltips with detailed information
  - Legend for toggling visibility
  - Zoom and pan capabilities
- Sentiment Distribution - Box plots showing sentiment ranges
  - All individual data points displayed
  - Quartile analysis

3. Raw Data (Tab 3)
- Complete Data Table - All records with sorting
- Statistical Summary - Expandable section with:
  - Mean, median, std deviation
  - Min/max values
  - Quartile information

### 4. Sidebar Controls
- API URL Configuration - Change backend endpoint
- Auto-refresh Toggle - Enable/disable automatic updates (20s intervals)
- Manual Refresh Button - On-demand data reload
- System Status Indicator - API connectivity monitor
- Data Point Counter - Total records in session

---

Docker Commands

Basic Operations

```bash
# Start all services in detached mode
docker-compose up -d

# View real-time logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend

# Stop all services (keeps data)
docker-compose stop

# Stop and remove containers (keeps volumes)
docker-compose down

# Stop and remove everything including volumes (DELETES DATA)
docker-compose down -v
```

Maintenance Commands

```bash
# Check service status
docker-compose ps

# Rebuild images after code changes
docker-compose up -d --build

# Restart a specific service
docker-compose restart backend

# Execute command in running container
docker exec -it fastapi-backend bash
docker exec -it mongodb mongosh -u admin -p password123

# View resource usage
docker stats
```

Troubleshooting Commands

```bash
# Check container logs for errors
docker-compose logs --tail=100 backend

# Inspect container
docker inspect fastapi-backend

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Full system cleanup (BE CAREFUL!)
docker system prune -a --volumes
```

---

Troubleshooting

Problem 1: "Cannot reach API" in Dashboard

Symptoms: Dashboard shows "Cannot reach API" in sidebar

Solutions:

```bash
# 1. Check if backend is running
curl http://localhost:8000/health

# 2. Check container status
docker-compose ps

# 3. View backend logs for errors
docker-compose logs backend

# 4. Update API URL in dashboard sidebar
# Change from: http://fastapi-backend:8000
# To: http://localhost:8000 (if running locally)
# Or: http://backend:8000 (if in Docker network)

# 5. Restart backend service
docker-compose restart backend
```

Problem 2: MongoDB Connection Failed

Symptoms: Backend logs show MongoDB connection errors

Solutions:

```bash
# 1. Check MongoDB is running
docker-compose ps mongodb

# 2. Test MongoDB connection
docker exec mongodb mongosh --eval "db.adminCommand('ping')"

# 3. Check MongoDB logs
docker-compose logs mongodb

# 4. Verify credentials in backend/main.py
# Should be: mongodb://admin:password123@mongodb:27017/

# 5. Restart MongoDB
docker-compose restart mongodb
```

Problem 3: Port Already in Use

Symptoms: Error message "port is already allocated"

Solutions:

```bash
# Windows - Find and kill process
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux - Find and kill process
lsof -i :8501
kill -9 <PID>

# Alternative: Change port in docker-compose.yml
# Change "8501:8501" to "8502:8501"
```

Problem 4: No Data Appearing

Symptoms: Dashboard shows "No data available"

Solutions:

```bash
# 1. Generate sample data via API
curl http://localhost:8000/generate-sample

# 2. Check if data was saved
docker exec -it mongodb mongosh -u admin -p password123
> use market_data
> db.sample_data.countDocuments()

# 3. Verify API returns data
curl http://localhost:8000/get-data

# 4. Click "Manual Refresh" in dashboard

# 5. Check browser console for errors (F12)
```

Problem 5: Docker Build Fails

Symptoms: Build process fails with errors

Solutions:

```bash
# 1. Clear Docker cache
docker system prune -a

# 2. Rebuild without cache
docker-compose build --no-cache

# 3. Check Dockerfile syntax
docker run -it --rm --entrypoint bash market_sentiment_tracker-backend

# 4. Verify requirements.txt is valid
cat backend/requirements.txt

# 5. Update Docker Desktop to latest version
```

---

Testing

API Testing with cURL

```bash
# Health check
curl http://localhost:8000/health

# Generate single data point
curl http://localhost:8000/generate-sample

# Generate 10 data points
for i in {1..10}; do
  curl -X GET "http://localhost:8000/generate-sample"
  echo ""
done

# Get all data (formatted)
curl http://localhost:8000/get-data | python -m json.tool

# Get summary statistics
curl http://localhost:8000/summary | python -m json.tool

# Test with specific limit
curl "http://localhost:8000/get-data?limit=5" | python -m json.tool
```

Database Testing

```bash
# Connect to MongoDB
docker exec -it mongodb mongosh -u admin -p password123

# Switch to database
use market_data

# View all collections
show collections

# Count documents
db.sample_data.countDocuments()

# View sample data
db.sample_data.find().limit(5).pretty()

# Check indexes
db.sample_data.getIndexes()

# Query specific ticker
db.sample_data.find({ ticker: "AAPL" }).limit(3).pretty()

# Get aggregation stats
db.sample_data.aggregate([
  { $group: {
    _id: "$ticker",
    avgPrice: { $avg: "$price" },
    count: { $sum: 1 }
  }}
])

# Exit MongoDB shell
exit
```

Python Testing Script

```python
# test_api.py
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health Check: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_generate():
    for i in range(5):
        response = requests.get(f"{BASE_URL}/generate-sample")
        if response.status_code == 200:
            data = response.json()["data"]
            print(f"{i+1}. Generated: {data['ticker']} @ ${data['price']}")

def test_get_data():
    response = requests.get(f"{BASE_URL}/get-data?limit=10")
    data = response.json()
    print(f"Retrieved {data['count']} records")

if __name__ == "__main__":
    test_health()
    test_generate()
    test_get_data()
```

---

Performance Optimization

MongoDB Performance Tips

```javascript
// Monitor query performance
db.sample_data.find({ ticker: "AAPL" }).explain("executionStats")

// Add compound index for specific queries
db.sample_data.createIndex({ ticker: 1, timestamp: -1, sentiment: 1 })

// Monitor index usage
db.sample_data.aggregate([{ $indexStats: {} }])

// Clean up old data (keep last 30 days)
db.sample_data.deleteMany({
  timestamp: { $lt: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) }
})
```

Docker Resource Limits

```yaml
# docker-compose.yml
services:
  mongodb:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          memory: 256M
  
  backend:
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 256M
  
  dashboard:
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 256M
```

Streamlit Performance

```python
# In app.py - Cache expensive computations
@st.cache_data(ttl=60)  # Cache for 60 seconds
def fetch_data():
    # ... existing code

@st.cache_data(ttl=120)  # Cache for 2 minutes
def fetch_summary():
    # ... existing code
```

---

Security Considerations

> Warning: This project uses default credentials for demonstration purposes. DO NOT use in production without proper security measures.

For Production Deployment

1. Change Default Credentials
   ```yaml
   # docker-compose.yml
   environment:
     MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER}
     MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
   ```

2. Use Environment Variables
   ```bash
   # .env file (add to .gitignore!)
   MONGO_USER=your_username
   MONGO_PASSWORD=your_secure_password
   API_SECRET_KEY=your_secret_key
   ```

3. Enable Authentication
   ```python
   # Add to backend/main.py
   from fastapi import Security, Depends, HTTPException
   from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
   
   security = HTTPBearer()
   
   async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
       # Implement token verification
       pass
   ```

4. Network Security
   ```yaml
   # docker-compose.yml - Remove external port exposure
   mongodb:
     ports:
       - "127.0.0.1:27017:27017"  # Bind to localhost only
   ```

5. Add SSL/TLS
   - Use nginx reverse proxy
   - Get free SSL certificates from Let's Encrypt
   - Configure HTTPS for dashboard and API

---

Production Deployment

Using Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml market-tracker

# Scale services
docker service scale market-tracker_backend=3

# View services
docker service ls

# Remove stack
docker stack rm market-tracker
```

Using Kubernetes

```yaml
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
        image: market-sentiment-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: MONGODB_URI
          valueFrom:
            secretKeyRef:
              name: mongo-credentials
              key: uri
```

Cloud Deployment Options

- AWS ECS - Elastic Container Service
- Google Cloud Run - Serverless containers
- Azure Container Instances - Managed containers
- DigitalOcean App Platform - Simple deployment
- Heroku - Platform as a Service

---

Contributing

Contributions are welcome! Here's how you can help:

Getting Started

1. Fork the repository
2. Clone your fork
   ```bash
   git clone https://github.com/your-username/market-sentiment-tracker.git
   ```
3. Create a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. Make your changes
5. Commit with descriptive messages
   ```bash
   git commit -m "Add feature: real-time alerts for sentiment changes"
   ```
6. Push to your fork
   ```bash
   git push origin feature/amazing-feature
   ```
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write docstrings for all functions and classes
- Add unit tests for new features
- Update documentation for any changes
- Keep commits atomic and descriptive
- Test locally before pushing

### Code Style

```python
# Good example
def fetch_market_data(ticker: str, limit: int = 100) -> dict:
    """
    Fetch market data for a specific ticker.
    
    Args:
        ticker: Stock symbol (e.g., 'AAPL')
        limit: Maximum number of records to return
    
    Returns:
        Dictionary containing market data and metadata
    """
    # Implementation
    pass
```

---

Learning Resources

### FastAPI
- [Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

### Streamlit
- [Official Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### MongoDB
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [MongoDB University](https://university.mongodb.com/) (Free courses)

### Docker
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

### Plotly
- [Plotly Python Documentation](https://plotly.com/python/)
- [Plotly Figure Reference](https://plotly.com/python/reference/)
- [Graph Examples](https://plotly.com/python/basic-charts/)

---

Roadmap

Completed
- [x] Basic data generation and storage
- [x] Interactive dashboard with multiple tabs
- [x] Docker containerization
- [x] MongoDB integration with indexes
- [x] Real-time charts with Plotly
- [x] Stock-specific filtering

In Progress
- [ ] Add unit tests with pytest
- [ ] Implement CI/CD pipeline
- [ ] Add data export functionality (CSV, JSON)

Future Enhancements
- [ ] Real Stock API Integration
  - Alpha Vantage API
  - Yahoo Finance API
  - Real-time WebSocket data
  
- [ ] User Authentication
  - JWT token-based auth
  - User profiles and preferences
  - Personalized watchlists
  
- [ ] Advanced Features
  - Email/SMS alerts for sentiment changes
  - Machine learning sentiment prediction
  - Technical indicators (RSI, MACD, Moving Averages)
  - Backtesting capabilities
  
- [ ] Mobile App
  - React Native mobile application
  - Push notifications
  - Offline support

- [ ] Performance Improvements
  - Redis caching layer
  - Database sharding
  - Load balancing

---

## License

```
MIT License

Copyright (c) 2026 Akshat Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Author

Akshat Gupta
- GitHub: [@akshat0107](https://github.com/akshat0107)
- LinkedIn: (https://www.linkedin.com/in/akshat-gupta-frm/)

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework
- [Streamlit](https://streamlit.io/) - Easy-to-use dashboard framework
- [Plotly](https://plotly.com/) - Interactive visualization library
- [MongoDB](https://www.mongodb.com/) - Flexible NoSQL database
- [Docker](https://www.docker.com/) - Containerization platform
- Python Community - For amazing open-source tools

---

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search [existing issues](https://github.com/yourusername/market-sentiment-tracker/issues)
3. Open a [new issue](https://github.com/yourusername/market-sentiment-tracker/issues/new) with:
   - Detailed description
   - Steps to reproduce
   - Error messages/logs
   - System information

---

## Show Your Support

If you found this project helpful, please consider:
- Sharing it with others
- Contributing improvements
- Providing feedback

---

<div align="center">

Built by Akshat Gupta

[⬆ Back to Top](#-market-sentiment-tracker)

</div>
