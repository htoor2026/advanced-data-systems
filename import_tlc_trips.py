import pandas as pd
from pymongo import MongoClient

# Load Parquet file
df = pd.read_parquet("yellow_tripdata_2024-09.parquet")

cols = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",                                    
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "total_amount",
    "payment_type"
]

df = df[cols].head(200000)

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

df = df.where(pd.notnull(df), None)
records = df.to_dict(orient="records")

client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@prog2270-cluster.tbue57s.mongodb.net/?retryWrites=true&w=majority"
)

db = client["global_lab"]

print("Starting TLC import...")
db.tlc_trips.insert_many(records)
print("TLC import completed successfully!")
