from jusibe import Jusibe

PUBLIC_KEY = "public_key"
ACCESS_TOKEN = "access_token"

jusibe = Jusibe(PUBLIC_KEY, ACCESS_TOKEN)

print(jusibe.check_available_credit())

print(jusibe.send_message('07016848962', 'LIMBO', 'Hello, World!'))
print(jusibe.check_delivery_status('message_id'))