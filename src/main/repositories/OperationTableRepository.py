import os
import time
import functools
import logging
from boto3.dynamodb.conditions import Attr
from src.main.resources.Storage import storage


class OperationTableRepository:

    def __init__(self):
        self.storage = storage(os.getenv('DYNAMO_TABLE_OPERATION_TYPES'))

    def operationTablePopulate(self, id, description, chargeOrder):
        data = {"OperationType_ID": id, "Description": description, "ChargeOrder": chargeOrder}

        response = self.storage.put_item(Item=data, ConditionExpression=Attr('OperationType_ID').not_exists())
