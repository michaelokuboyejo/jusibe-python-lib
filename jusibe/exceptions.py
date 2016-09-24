__author__ = 'michaelokuboyejo'

class JusibeException(Exception):
    """
    There was an ambiguous exception that occurred while attempting to fetch
    your machine's public IP address from the Jusibe service.
    """
    pass

class ServiceError(JusibeException):
    """
    The request failed because the Jusibe service is currently down or
    experiencing issues.
    """
    pass

class ConnectionError(JusibeException):
    """
    The request failed because the Jusibe service is currently down or
    experiencing issues.
    """
    pass

class BadRequestError(JusibeException):
    """
    The request could not be completed because one or all of the parameters
     needed for the request is invalid or incorrect
    """
    pass
