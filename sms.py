# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'auth_token'
auth_token = 'auth_token_secret'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hey Rojan",
                     from_='+17148815659',
                     to='+9779814972105'
                 )

print(message.sid)
