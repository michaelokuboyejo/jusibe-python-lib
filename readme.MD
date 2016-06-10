###jusibe-python-lib
A modular Python Library for interacting with the (Jusibe SMS HTTP API) <http://jusibe.com>

#####Usage
________

```python
public_key = 'python_public_key_here'
access_token = 'access_token__here'
jusibe = Jusibe(public_key, access_token)
response = jusibe.send_message(234812345678, "sender", "message to send")

```

The response will either be True or False depending on the outcome. 
