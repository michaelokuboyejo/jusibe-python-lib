__author__ = 'michaelokuboyejo'


class JusibeException(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message
