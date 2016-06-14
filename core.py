__author__ = 'michaelokuboyejo'

import requests


class Jusibe:

    BASE_URL = 'http://jusibe.com/smsapi'

    def __init__(self, public_key, access_token):
        """
        Constructor for Jusibe Class
        :param public_key: Public Key gotten from the settings page on http://jusibe.com/
        :param access_token: Access Token gotten from the settings page on http://jusibe.com/
        :return:
        """
        if len(public_key) == 0 or public_key is None:
            raise JusibeException("The Public Key cannot be Empty. Please pass it to the constructor")
        if len(access_token) == 0 or access_token is None:
            raise JusibeException("The Access Token cannot be Empty. Please pass it to the constructor")
        self.public_key = public_key
        self.access_token = access_token

    def check_available_credit(self):
        """
        Checks Available Credit Units
        :return: available credits as a string
        """
        url = self.BASE_URL + "/get_credits"
        response = self.perform_get_request(url)
        return response['sms_credits']

    def check_delivery_status(self, message_id):
        """
        Checks Delivery Status of a particular Message
        :param message_id: message_id of the message in particular
        :return: Delivery Status from Sever response as a dictionary
        """
        payload = {'message_id': message_id}
        url = "/delivery_status/"
        if len(message_id) == 0:
            raise JusibeException("message_id cannot be empty")
        response = self.perform_get_request(url, payload)
        return {
            'message_id': response['message_id'],
            'status': response['status'],
            'date_sent': response['date_sent'],
            'date_delivered': response['date_delivered']
        }

    def send_message(self, recipient, sender, message):
        """
        Accepts the message details and sends sms
        :param recipient: mssidn for receiver
        :param sender: string name of sender
        :param message: message to be sent
        :return: response in JSON
        """
        if recipient is None:
            raise JusibeException("Recipient field cannot be null or empty")
        if sender is None:
            raise JusibeException("Sender Field cannot be null or empty")
        if message is None:
            raise JusibeException("Message Field cannot be empty or null")
        payload = {
            'to': recipient,
            'from': sender,
            'message': message
        }
        response =  self.perform_post_request("/send_sms", payload)
        return {
            'status': response['status'],
            'message_id': response['message_id'],
            'sms_credits_used': response['sms_credits_used']
        }

    def perform_post_request(self, url, payload={}):
        """
        Performs a POST request
        :param url:
        :param data: dictionary containing request parameters
        :return: HTTP response
        """
        uri = self.BASE_URL + url
        keys = (self.public_key, self.access_token)
        try:
            r = requests.post(uri, params=payload, auth=keys)
            return r.json()
        except requests.ConnectionError:
            raise JusibeException("Bad Connection")

    def perform_get_request(self, url, params={}):
        """
        Performs a GET request
        :param url: URL to get
        :return:
        """
        uri = self.BASE_URL + url
        keys = (self.public_key, self.access_token)
        try:
            r = requests.get(uri, params, auth=keys)
            return r.json()
        except requests.ConnectionError:
            raise JusibeException("Bad Connection")

class JusibeException(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message
