import os
import time
import functools
import logging
from boto3.dynamodb.conditions import Attr, Key
from src.main.resources.Storage import storage


class OperationTableRepository:

    def __init__(self):
        self.storage = storage(os.getenv('DYNAMO_TABLE_OPERATION_TYPES'))

    def operationTablePopulate(self):
        response = self.storage.put_item(
                        Item={
                            "OperationType_ID": 1,
                            "Description": "COMPRA A VISTA",
                            "ChargeOrder": 2
                        },
                    )
        print(response)
