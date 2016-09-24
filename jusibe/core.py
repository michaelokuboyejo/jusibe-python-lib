from jusibe.exceptions import BadRequestError, ConnectionError, ServiceError
from jusibe.settings import BASE_URL

__author__ = 'michaelokuboyejo'

import requests


class Jusibe:

    def __init__(self, public_key, access_token):
        """
        Constructor for Jusibe Class
        :param public_key: Public Key gotten from the settings page on http://jusibe.com/
        :param access_token: Access Token gotten from the settings page on http://jusibe.com/
        :return:
        """
        if len(public_key) == 0 or public_key is None:
            raise BadRequestError("The Public Key cannot be Empty. Please pass it to the constructor")
        if len(access_token) == 0 or access_token is None:
            raise BadRequestError("The Access Token cannot be Empty. Please pass it to the constructor")
        self.public_key = public_key
        self.access_token = access_token

    def check_available_credit(self):
        """
        Checks Available Credit Units
        :return: available credits as a string
        """
        url = BASE_URL + "/get_credits"
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
            raise BadRequestError("message_id cannot be empty")
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
            raise BadRequestError("Recipient field cannot be null or empty")
        if sender is None:
            raise BadRequestError("Sender Field cannot be null or empty")
        if message is None:
            raise BadRequestError("Message Field cannot be empty or null")
        payload = {
            'to': recipient,
            'from': sender,
            'message': message
        }
        response = self.perform_post_request("/send_sms", payload)
        return {
            'status': response['status'],
            'message_id': response['message_id'],
            'sms_credits_used': response['sms_credits_used']
        }

    def perform_post_request(self, url, payload={}):
        """
        Performs a POST request
        :param url: URL to perform POST request
        :param data: dictionary containing request parameters
        :return: HTTP response
        """
        uri = BASE_URL + url
        keys = (self.public_key, self.access_token)
        try:
            r = requests.post(uri, params=payload, auth=keys)
        except requests.RequestException:
            raise ConnectionError("The request failed because it wasn't able to reach the Jusibe Service. This is most likely due to a networking error of some sort")
        if r.status_code != 200:
            raise ConnectionError("Your request received an invalid status from Jusibe " + str(r.status_code) + ". Something went wrong")
        return r.json()

    def perform_get_request(self, url, params={}):
        """
        Performs a GET request
        :param url: URL to get
        :return: JSON response
        """
        uri = BASE_URL + url
        keys = (self.public_key, self.access_token)
        try:
            r = requests.get(uri, params, auth=keys)
        except requests.RequestException:
            raise ServiceError("The request failed because it wasn't able to reach the Jusibe service. This is most likely due to a networking error of some sort")
        if r.status_code != 200:
            raise ServiceError("Your request received an invalid status from Jusibe " + str(r.status_code) + ". Something went wrong")
        return r.json()

