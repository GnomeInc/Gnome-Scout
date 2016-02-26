"""
Error classes for the rest_client module
"""


class Error(Exception):
    pass


class ApiError(Error):
    """
    Exception for REST Api Errors

    Attributes:
        http_code -- anything other than 200
        message -- Explanation
    """
    def __init__(self, http_code, message):
        self.http_code = http_code
        self.message = message
