###jusibe-python-lib
A modular Python Library for interacting with the (Jusibe SMS HTTP API) <http://jusibe.com>

#####Usage
________

```python
public_key = 'python_public_key_here' #change this
access_token = 'access_token__here' #change this
jusibe = Jusibe(public_key, access_token)
response = jusibe.send_message('234812345678', 'sender, 'message to send')
jusibe.check_available_credit()


```

The response will either be True or False depending on the outcome. 
