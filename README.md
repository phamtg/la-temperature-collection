# Los Angeles Daily Temperature Collection Project

## Description
This project collects daily temperature data for Los Angeles from the Open-Meteo API for April through May 2024 and ingests it into an AWS data pipeline. The data is processed and stored in AWS S3, transformed and cleaned using AWS Glue, and made available for querying in AWS Athena. A Grafana dashboard is created to visualize the data, providing insights.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Architecture](#architecture)
3. [Data Flow](#data-flow)
4. [Setup](#setup)
5. [AWS Services Used](#aws-services-used)
6. [Steps](#steps)
7. [Visualization](#visualization)
8. [Acknowledgements](#acknowledgements)

## 1. Prerequisites
- AWS account: [Sign up for AWS](https://aws.amazon.com/)
- Grafana Lab account: [Sign up for Grafana](https://grafana.com/)

## 2. Architecture
![LA_Temperature_de_project](https://github.com/phamtg/la-temperature-collection/assets/148672438/2e4d54a7-3db4-4929-8359-8888c64a0b07)

## 3. Data Flow
1. **Data Ingestion**: A Lambda function ingests weather data from the Open-Meteo API and sends it to a Kinesis Data Firehose stream.
2. **Data Storage**: Kinesis Data Firehose delivers the data to an S3 bucket.
3. **Data Crawling**: AWS Glue crawls the data in S3 to create a table in the AWS Glue Data Catalog.
4. **Data Transformation**: AWS Glue jobs transform the data, perform data quality checks, and save the cleaned data as Parquet files in S3.
5. **Data Querying**: The transformed data is available for querying in AWS Athena.
6. **Data Visualization**: Grafana is used to build a dashboard for visualizing the data.

## 4. AWS Services Used
- **AWS Lambda**: To run the function that ingests data from the Open-Meteo API.
- **AWS Kinesis Data Firehose**: To deliver the ingested data to S3.
- **AWS S3**: To store raw and transformed data.
- **AWS Glue**: To crawl, transform, and clean the data.
- **AWS Athena**: To query the transformed data.
- **Grafana**: To visualize the data.
  
## 5. Setup
1. **AWS Lambda**: Deploy the `LA_weather_lambda_put_record_batch.py` Lambda function in the `lambda/` directory using the AWS Lambda Console or CLI.
2. **AWS Kinesis Data Firehose**: Create a Kinesis Data Firehose delivery stream to deliver data to your S3 bucket.
- Example configuration:
  . Source: Direct PUT or other sources
. Destination: S3 bucket
. S3 bucket ARN: arn:aws:s3:::your-bucket-name
3. **AWS Glue**:
   - Create a Glue Crawler to crawl the data in your S3 bucket and create a Glue Data Catalog table.
   - Create and run Glue jobs using the scripts in the `glue/` directory to transform data and perform data quality checks.
4. **AWS Athena**: Configure Athena to query the data stored in your S3 bucket.
5. **Grafana**: Set up Grafana to visualize the data.

## 6. Pipeline
1. Trigger the Lambda function to start data ingestion.
2. Verify that the data is being delivered to your S3 bucket via Kinesis Data Firehose.
3. Run the Glue crawler to update the Glue Data Catalog.
4. Execute Glue jobs to transform and clean the data.
- <img width="1500" alt="glue_orchestration" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/6cc96f75-192c-40b3-a6fe-666dc7cb40cc">
5. Query the transformed data in Athena to verify the data quality and structure.
- <img width="585" alt="query" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/94fce06b-f974-4f7b-9544-222dd07c2cbf">
- <img width="1367" alt="result" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/2583bd02-c91e-408f-86fa-5e118c3baa44">
6. Use Grafana to visualize the data.
- <img width="614" alt="grafana query" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/08c4afe8-eebf-4b69-8a0e-4409842e6f24">

## 7. Visualization
<img width="1839" alt="visualization" src="https://github.com/phamtg/la-temperature-collection/assets/148672438/0874c40b-5d6d-4b4d-a455-3abd5807302f">

#### Troubleshooting

```markdown
## 8. Troubleshooting

- **Lambda Function Errors:**
  - Check CloudWatch logs for detailed error messages.
  - Verify the IAM role has the necessary permissions.

- **Kinesis Data Firehose Issues:**
  - Ensure the Firehose stream is properly configured with the correct S3 bucket.
  - Check Firehose monitoring metrics for delivery failures.

- **Glue Job Failures:**
  - Review Glue job logs for errors.
  - Ensure the Glue job script paths and S3 bucket permissions are correct.

- **Athena Query Problems:**
  - Verify the Glue Data Catalog table is correctly configured.
  - Check for syntax errors in your SQL queries.


## 9. Acknowledgements
Special thanks to:
- [David Freitag](https://github.com/dkfreitag) for his course on [Maven: Build Your First Serverless Data Engineering Project](https://maven.com/david-freitag/first-serverless-de-project)

Data source:
- [Weather Data Open Meteo API](https://api.open-meteo.com/)
