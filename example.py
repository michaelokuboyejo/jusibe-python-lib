__author__ = 'michaelokuboyejo'

from core import Jusibe

PUBLIC_KEY = "public_key"
MY_PUBLIC_KEY = "e0944f19741ef2cdb4992691b3296dce"
MY_ACCESS_TOKEN = "7d85f20ea31a5d3487386281e158822e"
ACCESS_TOKEN = "access_token"

jusibe = Jusibe(MY_PUBLIC_KEY,MY_ACCESS_TOKEN)

print jusibe.check_available_credit()
