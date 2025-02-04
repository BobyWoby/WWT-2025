#hackathon project
print("test")


from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='hackathontest619@gmail.com',
    MAIL_PASSWORD='mkbm rnju hdhx ulyc',
    MAIL_DEFAULT_SENDER=('HackathonProject', 'hackathontest619@gmail.com')
)

mail = Mail(app)



#this should send an email

def send_email():
    with app.app_context():  # Ensure we're in the application context
        print("in the app context")
        msg = Message(
            subject="Hello from Flask",
            recipients=["ethanbc2020@icloud.com", "2027.sraheja@jburroughs.org"],  # List of recipients
            body="This is another test email sent from the Hackathon team."
        )
        mail.send(msg)
        print("Email sent successfully!")

send_email()

