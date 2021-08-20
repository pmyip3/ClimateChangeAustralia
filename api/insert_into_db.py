import boto3
import json


def insert(table, data):
    # example: [{year: 1976, month: 6, value: 328.988}]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    for d in data:
        print(d)
        table.put_item(
            Item = {
                "year": d["year"],
                "month": d["month"],
                "value": d["value"]
            }
        )


def lambda_handler(event, context):
    data = event['data']
    table = event['table']
    insert(table, data)

data = "[{\"year\": \"1976\", \"month\": \"6\", \"value\": \"328.988\"}]"
insert("ghg_data", json.loads(data))