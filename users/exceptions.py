from rest_framework.exceptions import APIException, ValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    NotAuthenticated, AuthenticationFailed, ErrorDetail
)

from .constants import UNAUTHORIZED, SESSION_EXPIRED


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    data_response = {}
    if response is not None:
        data_response['error_code'] = response.status_code

    if isinstance(exc, ValidationError):
        errors = response.data
        if 'phones' in errors:
            error_phones = errors['phones']
            errors = error_phones[0]
        if type(errors) is ErrorDetail:
            data_response['message'] = str(errors)
        else:  
            key, error_list = errors.popitem()
            data_response['message'] = error_list[0]
    elif isinstance(exc, NotAuthenticated):
        data_response['message'] = UNAUTHORIZED
    elif isinstance(exc, AuthenticationFailed):
        data_response['message'] = SESSION_EXPIRED

    response.data = data_response
    return response


