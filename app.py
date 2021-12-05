from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

oth_number = os.getenv('oth_sandbox')

client = Client(account_sid, auth_token)

# message body
body_msg = input('Escriba el mensaje: ')
from_number = os.getenv('from_number')
to_number = os.getenv('to_number')
 
message = client.messages.create( 
                              from_='whatsapp:{}'.format(from_number),
                              body=body_msg,
                              to='whatsapp:{}'.format(to_number)
                          )
 
print(message.sid)