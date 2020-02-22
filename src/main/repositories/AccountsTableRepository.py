import os
from boto3.dynamodb.conditions import Attr
from src.main.resources.Storage import storage


class OperationTableRepository:

    def __init__(self):
        self.storage = storage(os.getenv('DYNAMO_TABLE_ACCOUNTS'))

    def accountTablePopulate(self, id, availableCreditLimit, availableWithdrawalLimit):
        data = {"Account_ID": id,
                "AvailableCreditLimit": availableCreditLimit,
                "AvailableWithdrawalLimit": availableWithdrawalLimit}

        self.storage.put_item(Item=data, ConditionExpression=Attr('Account_ID').not_exists())
