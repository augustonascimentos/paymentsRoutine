import boto3
import os


def storageClient():
    dynamodbClient = boto3.client(
        'dynamodb',
        region_name=os.getenv('DYNAMO_AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        endpoint_url=os.getenv('DYNAMO_ENDPOINT_URL'),
    )
    return dynamodbClient


def storageResource():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=os.getenv('DYNAMO_AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        endpoint_url=os.getenv('DYNAMO_ENDPOINT_URL'),
    )

    dynamodb.meta.client.meta.config.connect_timeout = 10
    dynamodb.meta.client.meta.config.read_timeout = 25

    return dynamodb


def storage(table):
    dynamo = storageResource()

    return dynamo.Table(table)
