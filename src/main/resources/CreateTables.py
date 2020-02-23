import os
from src.main.resources.Storage import storageResource, storageClient

operationTableName = os.getenv('DYNAMO_TABLE_OPERATION_TYPES')
accountTableName = os.getenv('DYNAMO_TABLE_ACCOUNTS')
transactionTableName = os.getenv('DYNAMO_TABLE_TRANSACTIONS')


class CreateTables:

    @staticmethod
    def createOperationTypesTable():

        response = storageClient().list_tables()

        if operationTableName not in response['TableNames']:

            storageResource().create_table(
                TableName=operationTableName,
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

    @staticmethod
    def createAccountTable():

        response = storageClient().list_tables()

        if accountTableName not in response['TableNames']:

            storageResource().create_table(
                TableName=accountTableName,
                KeySchema=[
                    {
                        'AttributeName': 'Account_ID',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'Account_ID',
                        'AttributeType': 'N'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                })

    @staticmethod
    def createTransactionTable():

        response = storageClient().list_tables()

        if transactionTableName not in response['TableNames']:

            storageResource().create_table(
                TableName=transactionTableName,
                KeySchema=[
                    {
                        'AttributeName': 'Transaction_ID',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'Transaction_ID',
                        'AttributeType': 'N'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                })
