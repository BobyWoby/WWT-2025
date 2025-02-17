#hackathon project

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from aiclient import hackedEmailPrompt
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

app = Flask(__name__)
CORS(app)


#configurations
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='hackathontest619@gmail.com',
    MAIL_PASSWORD= os.getenv("MAIL_PASS"),
    MAIL_DEFAULT_SENDER=('Hackathon Project', 'hackathontest619@gmail.com')
)

mail = Mail(app)



#this should send an email

@app.route('/send-email', methods=["POST"])
def send_email():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400
    
    recipient = data.get('recipient')
    subject = data.get("subject", "Default Subject")
    sender = data.get('sender')
    #body = data.get("body", "no body text provided")

    if not recipient:
        return jsonify({"error": "recipient email is required"}),  400
    
    print("sending email...")
    message = hackedEmailPrompt(sender, recipient)
    msg = Message(
        subject="Suspicious Email Alert",    #string for the header
        recipients=[recipient], #email adress array
        body=message #function for the AI generated message. It's just text.
    )
    mail.send(msg)
    print("msg: " + message)
    
    return jsonify({"message": "Email sent."}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)

