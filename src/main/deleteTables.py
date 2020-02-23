import boto3


def deleteTables():

    tables = ["operationTypes", "accounts", "transactions"]
    for i in tables:
        dynamodbClient = boto3.client('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

        response = dynamodbClient.list_tables()
        if i in response['TableNames']:
            table = dynamodb.Table(i)
            table.delete()

deleteTables()
