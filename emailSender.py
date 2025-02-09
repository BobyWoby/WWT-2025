#hackathon project

from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#configurations
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='hackathontest619@gmail.com',
    MAIL_PASSWORD='mkbm rnju hdhx ulyc',
    MAIL_DEFAULT_SENDER=('Hackathon Project', 'hackathontest619@gmail.com')
)

mail = Mail(app)



#this should send an email

@app.route('/send-email', methods=["POST"])
def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get("subject", "Default Subject")
    body = data.get("body", "no body text provided")

    if not recipient:
        return jsonify({"error": "recipient email is required"}),  400
    
        
    with app.app_context():  # Ensure we're in the application context
        print("in the app context")
        msg = Message(
            subject=subject,    #string for the header
            recipients=[recipient], #email adress array
            body=body #this is where we'll add the AI generated message. It's just text.
        )
        mail.send(msg)

        return jsonify({"message": "Email sent."})

if __name__ == "__main__":
    app.run(debug=True)
