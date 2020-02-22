import os
from src.main.resources.Storage import storageResource, storage, storageClient

tableName = os.getenv('DYNAMO_TABLE_OPERATION_TYPES')


class CreateTables:

    @staticmethod
    def createOperationTypesTables():

        response = storageClient().list_tables()

        if tableName not in response['TableNames']:

            storageResource().create_table(
                TableName=tableName,
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
