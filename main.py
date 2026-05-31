from fastapi import FastAPI
from tasks import send_email
app = FastAPI()
@app.get("/")
def home():
    return {"message": "API Running"}
@app.post("/send-mail")
def send_mail(email: str):
    task = send_email.delay(email)
    return {
        "message": "Email task submitted",
        "task_id": task.id
    }
