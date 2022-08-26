from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
 
app = Flask(__name__)
 
@app.route("/wa")
def wa_hello():
    return "Hello, World!"
 
@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    
    msg = request.form.get('Body').lower() # Reading the message from the whatsapp
 
    print("msg-->",msg)
    resp = MessagingResponse()
    reply=resp.message()
    # Create reply
    if msg == "hi":
       reply.body("hello!")
 
 
    return str(resp)
 
if __name__ == "__main__":	
    app.run(debug=True)