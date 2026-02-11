db = db.getSiblingDB('market_data');

print("Initializing Market Data Database");

db.createCollection('sample_data');
db.createCollection('alerts');
db.createCollection('news');

db.sample_data.createIndex({ticker:1,timestamp:-1});
db.sample_data.createIndex({timestamp:-1});

db.alerts.createIndex({timestamp:-1});
db.alerts.createIndex({acknowledged:1});

print("Markets Data database initialized successfully!");