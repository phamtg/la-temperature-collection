
import json
import boto3
import urllib3
import datetime

# REPLACE WITH YOUR DATA FIREHOSE NAME
FIREHOSE_NAME = 'PUT-S3-8xnFi'

def lambda_handler(event, context):
    
    http = urllib3.PoolManager()
    
    r = http.request("GET", "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&daily=temperature_2m_max&timezone=America%2FLos_Angeles&start_date=2024-04-01&end_date=2024-06-01")
    
    # turn it into a dictionary
    r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))
    
    time_list = []
    for val in r_dict['daily']['time']:
        time_list.append(val)
    
    temp_list = []
    for temp in r_dict['daily']['temperature_2m_max']:
        temp_list.append(temp)
    
    # extract pieces of the dictionary
    processed_dict = {}
    
    # append to string running_msg
    running_msg = ''
    for i in range(len(time_list)):
        # construct each record
        processed_dict['latitude'] = r_dict['latitude']
        processed_dict['longitude'] = r_dict['longitude']
        processed_dict['time'] = time_list[i]
        processed_dict['temp_f'] = temp_list[i]
        processed_dict['row_ts'] = str(datetime.datetime.now())
    
        # add a newline to denote the end of a record
        # add each record to the running_msg
        running_msg += str(processed_dict) + '\n'
        
    # cast to string
    running_msg = str(running_msg)
    fh = boto3.client('firehose')
    
    reply = fh.put_record_batch(
        DeliveryStreamName=FIREHOSE_NAME,
        Records = [
                {'Data': running_msg}
                ]
    )

    return reply