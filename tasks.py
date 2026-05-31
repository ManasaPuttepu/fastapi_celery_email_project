from celery_worker import celery_app
import smtplib
from email.mime.text import MIMEText

@celery_app.task
def send_email(receiver_email):
    sender_email = "manasaputtepu@gmail.com"
    app_password = "fogm nyoj qdvn nkre"

    msg = MIMEText("Hello! This email was sent using FastAPI + Celery.")
    msg["Subject"] = "FastAPI Celery Test"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

    return "Email sent successfully"
