Advanced Data Systems — Analytics & Streaming Pipeline
Overview 

This repository contains an end-to-end data engineering and analytics project built for an Advanced Data Systems course. The project demonstrates how large-scale public datasets can be ingested, modeled, indexed, analyzed, and optimized using MongoDB, Redis, and Python, with a focus on performance engineering, time-series analytics, and stream processing concepts.

The system combines batch analytics, materialized views, query optimization, and real-time caching/stream simulation, reflecting patterns used in modern data platforms.

Datasets Used
1. OWID COVID-19 Dataset (CSV)     

Source:

https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv


Used for:

Time-series pandemic analysis

Rolling averages and surge detection

Annual risk index computation

Policy, vaccination, and health outcome correlations

2. NYC TLC Yellow Taxi Trips (Parquet – Sept 2024)

Source:

https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-09.parquet


Used for:

Large-scale event data ingestion

Hour-of-day demand and revenue analytics

Percentile and moving-average calculations

Performance engineering experiments

Architecture & Technology Stack

Languages & Tools

Python (Pandas, PyMongo, PyArrow)

MongoDB Atlas (Aggregation Framework, Indexing, $merge, $setWindowFields)

Redis (Caching, TTL, Streams)

MongoDB Compass & Atlas Charts

Core Concepts Demonstrated

Schema design & data normalization

Time-series analytics

Window functions & rolling statistics

Materialized views

Index-driven performance optimization

Caching & stream consumption patterns

Data Ingestion
OWID COVID-19 Data

Imported using a custom Python script

Reduced to essential analytical fields to fit cloud storage constraints

Converted dates to ISODate

Cleaned missing values (NaN → null)

Inserted using insert_many via PyMongo

NYC TLC Taxi Trips

Parquet file loaded using Pandas + PyArrow

Selected key operational and financial fields

Sampled first 200,000 rows to remain within Atlas free-tier limits

Converted timestamps to datetime

Inserted into MongoDB using PyMongo

Index Strategy

Indexes were designed to support analytics workloads, not just point lookups.

OWID Collection (owid_daily)

{ location: 1, date: 1 }
Enables efficient time-series window operations and surge detection.

{ continent: 1, date: 1 }
Supports continent-level aggregation and trend analysis.

TLC Collection (tlc_trips)

{ tpep_pickup_datetime: 1 }
Optimizes time-based scans, rolling averages, and performance experiments.

{ PULocationID: 1, tpep_pickup_datetime: 1 }
Enables fast zone-and-time demand analytics.

Analytical Workloads
Pandemic Surge Detection

7-day rolling averages using $setWindowFields

14-day lag comparison using $shift

Surge multiplier calculation

ISO week grouping

Weekly top-5 countries by surge intensity

Performance verified using explain() before and after indexing

Annual Risk Index

A composite risk_index computed per country per year using:

Cases per 100k

Deaths per 100k

Median stringency index

Vaccination coverage

Each component is normalized and weighted to produce a bounded risk score reflecting public health impact and mitigation factors.

Materialized View

Annual country-level risk metrics written using $merge

Stored in risk_annual_v1

Unique compound index ensures one record per country per year

Designed for dashboards and downstream analytics

NYC Taxi Demand & Revenue Analytics

Hour-level aggregations

95th percentile fare analysis

3-hour moving averages using window functions

Identification of peak demand and high-revenue periods

Patterns consistent with commuter and airport traffic behavior

Performance Engineering

A heavy aggregation query was evaluated in three stages:

Baseline – no index (COLLSCAN)

Indexed – time-based index (IXSCAN)

Rewritten – reduced projections and optimized pipeline order

Results show:

Reduced documents examined

Elimination of in-memory sorts

Lower execution time and resource usage

Real-Time Concepts (Redis)
Caching

Demand or surge results cached using Redis keys

TTL applied to ensure freshness

Cache-miss triggers recomputation and refresh

Demonstrates read-through cache behavior

Streaming Simulation

Redis Streams used to simulate live taxi events

Consumer group processes events

Aggregates trips by hour and zone

Writes results to MongoDB materialized collection

Ensures at-least-once processing semantics

Repository Contents

FinalExam.pdf — Full project report with explanations and screenshots

import_tlc.py — Python script used to ingest NYC TLC data

README.md — Project overview and technical documentation

.gitignore — Prevents accidental commits of data files or secrets

Why This Project Matters

This project mirrors real-world data engineering workflows:

Handling large datasets under resource constraints

Designing indexes for analytics, not just CRUD

Using window functions for time-series analysis

Materializing views for performance

Integrating batch and streaming concepts

Applying caching to reduce computation cost

It demonstrates practical skills relevant to Data Engineering, Analytics Engineering, and Backend Data Systems roles.

Author

Harkamal Toor
Advanced Data Systems — Final Project
