#!/usr/bin/env python3

import boto3, pandas as pd
import time, re
from fs import filesize
from tabulate import tabulate
from datetime import datetime, timedelta
from dateutil import parser

logs_client = boto3.client('logs')
lambda_client = boto3.client('lambda')

# READY TO MAKE THE TABLE FOR LAMBDA FUNCTIONS WITH PYTHON TO SHOW WHAT I NEED
def last_lambda_run(func_name):
    log_group = f'/aws/lambda/{func_name}'
    query = 'fields @timestamp, @message | sort @timestamp desc | limit 1'
    start_query_response = logs_client.start_query(
        startTime=int((datetime.today() - timedelta(days=30)).timestamp()),
        endTime=int(datetime.now().timestamp()),
        logGroupName=log_group, 
        queryString=query)
    query_id = start_query_response['queryId']
    time.sleep(1)
    return logs_client.get_query_results(queryId=query_id)

def parse_lambda_report(result):
    s1 = result['results'][0][1]['value']
    s2 = re.sub(r'^REPORT ','',s1).strip()
    l1 = s2.split('\t')
    l2 = [i.split(': ') for i in l1]
    d = {a:b for a,b in l2}
    
    s5 = result['results'][0][0]['value']
    d['last_run'] = parser.parse(s5).date()
    return d

def get_lambda_funcs_dates():
    funcs_result = lambda_client.list_functions()
    names_dates = [(f['FunctionName'], f['LastModified']) for f in funcs_result['Functions']]
    return names_dates

def last_lambda_table():
    df = pd.DataFrame()
    names_dates = get_lambda_funcs_dates()
    for name, date in names_dates:
        result = last_lambda_run(name)
        parsed = parse_lambda_report(result)
        parsed['modified'] = parser.parse(date).date()
        ser = pd.Series(parsed, name=name)
        df = df.append(ser) # ignore_index=True)
    df = df[['last_run', 'modified', 'Billed Duration']]
    df = df.rename(columns={'Billed Duration': 'billed_dur'})
    tbl_string = tabulate(df, headers='keys', tablefmt='psql')
    return tbl_string

print(last_lambda_table())
