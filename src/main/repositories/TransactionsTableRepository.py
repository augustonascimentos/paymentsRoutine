import os
from boto3.dynamodb.conditions import Attr
from src.main.resources.Storage import storage


class OperationTableRepository:

    def __init__(self):
        self.storage = storage(os.getenv('DYNAMO_TABLE_TRANSACTIONS'))

    def transactionTablePopulate(self, id, accountId, operationTypeId, amount, balance, eventDate, dueDate):
        data = {"Transaction_ID": id,
                "Account_ID": accountId,
                "OperationType_ID": operationTypeId,
                "Amount": amount,
                "Balance": balance,
                "EventDate": eventDate,
                "DueDate": dueDate}

        self.storage.put_item(Item=data, ConditionExpression=Attr('Transaction_ID').not_exists())
