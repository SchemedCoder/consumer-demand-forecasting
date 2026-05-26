# Consumer Demand Forecasting Platform

## Overview

A cloud-ready batch ETL pipeline built using Python, Airflow, PostgreSQL, FastAPI, and Azure Blob Storage.

The platform processes retail sales data, handles late-arriving transactions, builds analytical datasets, and serves demand insights through REST APIs.

---

## Business Problem

Retail organizations receive sales data from multiple stores.

Challenges:

- Delayed file arrivals
- Duplicate records
- Missing values
- Inconsistent product information
- Demand analysis requirements

This platform solves these issues through a layered ETL architecture.

---

## Architecture

Store Systems
↓
Azure Blob Storage
↓
Airflow
↓
Bronze Layer
↓
Silver Layer
↓
Late Arrival Reconciliation
↓
Gold Layer
↓
FastAPI
↓
Power BI

---

## Features

- Batch ETL Processing
- Incremental Loads
- Late Arriving Data Handling
- Data Quality Validation
- Historical Demand Analysis
- REST APIs
- Docker Deployment

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- Apache Airflow
- FastAPI
- Docker
- Azure Blob Storage

---

## Data Layers

### Bronze

Raw source data.

### Silver

Validated and transformed records.

### Gold

Business-ready analytical tables.

---

## Late Arriving Data Strategy

Every DAG run reprocesses:

Current Date
+
Previous 7 Days

This ensures delayed transactions are reconciled automatically.

---

## Project Structure

consumer-demand-forecasting/
├── airflow/
├── etl/
├── api/
├── sql/
├── sample_data/
├── tests/
└── README.md
