import os
from src.main.resources.Storage import storage


class Tables:

    def __init__(self):
        self.storage = storage(os.getenv('DYNAMO_TABLE_OPERATION_TYPES'))

    def createOperationTypes(self):
        self.storage.create_table(
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
                {
                    'AttributeName': 'Description',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'ChargeOrder',
                    'AttributeType': 'N'
                },
            ]
        )
