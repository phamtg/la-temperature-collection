# Los Angeles Daily Temperature Collection Project

## Description
This project collects daily temperature data for Los Angeles from the Open-Meteo API for April through May 2024 and ingests it into an AWS data pipeline. The data is processed and stored in AWS S3, transformed and cleaned using AWS Glue, and made available for querying in AWS Athena. A Grafana dashboard is created to visualize the data, providing insights.

## Table of Contents
1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Architecture](#architecture)
4. [Data Flow](#data-flow)
5. [Setup](#setup)
6. [AWS Services Used](#aws-services-used)
7. [Usage](#usage)
8. [Visualization](#visualization)
9. [Contributing](#contributing)

## Installation
To set up the project locally, ensure you have the necessary AWS CLI and SDKs installed. Clone the repository and install required dependencies.

```bash
git clone https://github.com/phamtg/la-temperature-collection.git
cd la-temperature-collection
pip install -r requirements.txt

## Project Structure
la-temperature-collection/
├── images/
│   ├── architecture_diagram.png
├── lambda/
│   ├── ingest_lambda.py
├── glue/
│   ├── transform_glue_job.py
│   ├── data_quality_check_glue_job.py
├── terraform/
│   ├── main.tf
├── README.md
├── requirements.txt

Architecture
The following diagram illustrates the architecture of the Los Angeles temperature data collection project:


Data Flow
Data Ingestion: A Lambda function ingests daily temperature data for Los Angeles from the Open-Meteo API and sends it to a Kinesis Data Firehose stream.
Data Storage: Kinesis Data Firehose delivers the data to an S3 bucket.
Data Crawling: AWS Glue crawls the data in S3 to create a table in the AWS Glue Data Catalog.
Data Transformation: AWS Glue jobs transform the data, perform data quality checks, and save the cleaned data as Parquet files in S3.
Data Querying: The transformed data is available for querying in AWS Athena.
Data Visualization: Grafana is used to build a dashboard for visualizing the data.


