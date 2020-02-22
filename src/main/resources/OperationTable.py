import os
from src.main.resources.Storage import storageResource


class Tables:

    @staticmethod
    def createTables():
        storageResource().create_table(
            TableName=os.getenv('DYNAMO_TABLE_OPERATION_TYPES'),
            KeySchema=[
                {
                    'AttributeName': 'OperationType_ID',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'OperationType_ID',
                    'AttributeType': 'N'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            })
