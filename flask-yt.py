from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    bot_resp= MessagingResponse()
    msg = bot_resp.message()

    # implement a hash map with keywords and responses
    if 'hello' in user_msg:
        msg.body("Hi there! How may I help you?")
    else:
        msg.body("Sorry, I didn't get what you have said!")

    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)