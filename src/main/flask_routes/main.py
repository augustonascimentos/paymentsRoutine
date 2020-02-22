import logging
from flask import jsonify
from src.main.resources.ErrorResponse import ErrorResponse
from src.main.repositories.OperationTableRepository import OperationTableRepository
from src.main.resources.CreateTables import CreateTables


def Main(app):
    @app.route('/v1/accounts/<string:account_id>', methods=['PATCH'])
    def account(account_id):
        try:

            return jsonify(), 200

        except Exception as e:
            logging.warning('Error: {}'.format(str(e)))
            response = ErrorResponse().create(e, category='payments')
            return jsonify(response), response['error']['status_code']
