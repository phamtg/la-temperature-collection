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
10. [License](#license)

## Installation
To set up the project locally, ensure you have the necessary AWS CLI and SDKs installed. Clone the repository and install required dependencies.

```bash
git clone https://github.com/phamtg/la-temperature-collection.git
cd la-temperature-collection
pip install -r requirements.txt
