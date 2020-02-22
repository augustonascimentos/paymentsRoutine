from src.main.schemas.ErrorSchema import ErrorSchema
from src.main.models import NotFoundException, ForbiddenAccessException


class ErrorResponse:

    @staticmethod
    def not_found(message, type, category='payments'):
        schema = ErrorSchema()
        body_response = schema.load({
            'error': {
                'status': 'Not found',
                'status_code': 404,
                'type': type,
                'category': category,
                'message': message
            }
        })

        return body_response.data

    @staticmethod
    def forbidden(message, type, category='payments'):
        schema = ErrorSchema()
        body_response = schema.load({
            'error': {
                'status': 'Forbidden',
                'status_code': 403,
                'type': type,
                'category': category,
                'message': message
            }
        })

        return body_response.data

    @staticmethod
    def internal_server_error(message, type, category='payments'):
        schema = ErrorSchema()
        body_response = schema.load({
            'error': {
                'status': 'Internal server error',
                'status_code': 500,
                'type': type,
                'category': category,
                'message': message
            }
        })

        return body_response.data

    @staticmethod
    def getResponseBuilder(error):
        typeOfError = type(error)

        errosDict = {
            NotFoundException: ErrorResponse.not_found,
            ForbiddenAccessException: ErrorResponse.forbidden
        }

        if typeOfError in errosDict:
            return errosDict[typeOfError]

        return ErrorResponse.internal_server_error

    @staticmethod
    def create(error, category):
        responseBuilder = ErrorResponse.getResponseBuilder(error)
        return responseBuilder(
            message=str(error),
            type=type(error),
            category=category
        )
