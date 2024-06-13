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

## 1. Installation
To set up the project locally, ensure you have the necessary AWS CLI and SDKs installed. Clone the repository and install required dependencies.
git clone https://github.com/yourusername/weather-data-collection.git
cd weather-data-collection
pip install -r requirements.txt

## 2. Project Structure
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


## 3. Architecture


## 4. Data Flow
1. Data Ingestion: A Lambda function ingests weather data from the Open-Meteo API and sends it to a Kinesis Data Firehose stream.
2. Data Storage: Kinesis Data Firehose delivers the data to an S3 bucket.
3. Data Crawling: AWS Glue crawls the data in S3 to create a table in the AWS Glue Data Catalog.
4. Data Transformation: AWS Glue jobs transform the data, perform data quality checks, and save the cleaned data as Parquet files in S3.
5. Data Querying: The transformed data is available for querying in AWS Athena.
6. Data Visualization: Grafana is used to build a dashboard for visualizing the data.

## 5. Setup
1. AWS Lambda: Deploy the ingest_lambda.py Lambda function using AWS Lambda Console or CLI.
2. AWS Kinesis Data Firehose: Create a Kinesis Data Firehose delivery stream to deliver data to your S3 bucket.
3. AWS Glue:
  - Create a Glue Crawler to crawl the data in your S3 bucket and create a Glue Data Catalog table.
  - Create and run Glue jobs using the scripts in the glue/ directory to transform data and perform data quality checks.
4. AWS Athena: Configure Athena to query the data stored in your S3 bucket.
5. Grafana: Set up Grafana to visualize the data.

## 6. AWS Services Used
- AWS Lambda: To run the function that ingests data from the Open-Meteo API.
- AWS Kinesis Data Firehose: To deliver the ingested data to S3.
- AWS S3: To store raw and transformed data.
- AWS Glue: To crawl, transform, and clean the data.
- AWS Athena: To query the transformed data.
- Grafana: To visualize the data.

## 7. Usage
1. Trigger the Lambda function to start data ingestion.
2. Verify that the data is being delivered to your S3 bucket via Kinesis Data Firehose.
3. Run the Glue crawler to update the Glue Data Catalog.
4. Execute Glue jobs to transform and clean the data.
5. Query the transformed data in Athena to verify the data quality and structure.
6. Use Grafana to visualize the data.

## 8. Visualization
<img width="1839" alt="visualization" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/3dca59fe-5dad-4aab-9d0d-7696350a5792">


## 9. Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.


