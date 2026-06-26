# Enterprise ETL Pipeline using Airflow, Snowflake & dbt

## Overview

This repository demonstrates an end-to-end cloud ETL pipeline using modern Data Engineering technologies.

Pipeline Features

- AWS S3 Landing Zone
- Python Data Ingestion
- Snowflake Data Warehouse
- dbt Transformations
- Apache Airflow Orchestration
- Amazon QuickSight Dashboard
- AWS SNS Notifications
- Slack Alerts
- Email Alerts
- Data Quality Validation

---

## Architecture

![Architecture](docs/architecture.png)

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | ETL |
| Apache Airflow | Workflow Orchestration |
| Snowflake | Cloud Warehouse |
| dbt | Data Transformation |
| AWS S3 | Landing Zone |
| SNS | Notifications |
| Slack | Alerts |
| QuickSight | BI Dashboard |
| SQL | Data Modeling |
| Docker | Deployment |

---

## Repository Structure

```text
configs/
dags/
dbt_project/
scripts/
snowflake/
sql/
notifications/
monitoring/
tests/
```

---

## Pipeline Flow

CSV

↓

AWS S3

↓

Python

↓

Snowflake RAW

↓

dbt Stage

↓

dbt Fact

↓

QuickSight

↓

Business Users

---

## Monitoring

Pipeline failures trigger

- AWS SNS
- Slack
- Email

---

## Status

Project Under Development

Phase 1 ✔

Phase 2 ⏳

Phase 3 ⏳

Phase 4 ⏳

Phase 5 ⏳