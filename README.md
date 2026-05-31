# fastapi_celery_email_project
# FastAPI + Celery Email Service

## Overview

This project demonstrates how to send emails asynchronously using:

* FastAPI
* Celery
* Redis
* Gmail SMTP

The API accepts an email address, pushes the task to Redis, and Celery processes the email in the background.

---

## Project Structure

```text
fastapi_celery_email_project/
│
├── main.py
├── celery_worker.py
├── tasks.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

### Software Required

* Python 3.11+
* Redis Server (or Memurai on Windows)
* Gmail Account
* Google App Password

---

## Installation

### Clone or Extract Project

```bash
cd fastapi_celery_email_project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Gmail Configuration

### Enable Two-Step Verification

1. Open https://myaccount.google.com/security
2. Enable "2-Step Verification"

### Generate App Password

1. Open https://myaccount.google.com/apppasswords
2. Create a new App Password
3. Copy the generated 16-character password

Example:

```text
abcd efgh ijkl mnop
```

---

## Update Email Credentials

Open `tasks.py`.

Replace:

```python
sender_email = "YOUR_GMAIL@gmail.com"
app_password = "YOUR_APP_PASSWORD"
```

with:

```python
sender_email = "yourgmail@gmail.com"
app_password = "your_google_app_password"
```

---

## Redis Setup

### Option 1: Redis

Install Redis and ensure it runs on:

```text
localhost:6379
```

### Option 2: Memurai (Windows)

Install Memurai Developer Edition.

Verify:

```bash
redis-cli ping
```

Expected Output:

```text
PONG
```

---

## Running the Application

### Step 1: Start Redis

Verify Redis is running.

```bash
redis-cli ping
```

Expected:

```text
PONG
```

---

### Step 2: Start Celery Worker

Open a terminal:

```bash
celery -A tasks worker --pool=solo --loglevel=info
```

Expected Output:

```text
Connected to redis://localhost:6379/0
ready.
```

---

### Step 3: Start FastAPI

Open another terminal:

```bash
uvicorn main:app --reload
```

Expected Output:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI will be available.

---

## Test Email Endpoint

### Request

```http
POST /send-mail?email=receiver@gmail.com
```

### Response

```json
{
  "message": "Email task submitted",
  "task_id": "xxxxxxxx"
}
```

---

## How It Works

1. User calls `/send-mail`.
2. FastAPI receives the request.
3. Celery pushes the task to Redis.
4. Redis stores the task.
5. Celery Worker reads the task.
6. Gmail SMTP sends the email.
7. User receives the email.

### Architecture

```text
Client
  |
  v
FastAPI
  |
  v
Redis
  |
  v
Celery Worker
  |
  v
Gmail SMTP
  |
  v
Receiver Inbox
```

---

## Troubleshooting

### Error: Cannot connect to Redis

```text
Error 10061 connecting to localhost:6379
```

Cause:

Redis is not running.

Solution:

Start Redis or Memurai and verify:

```bash
redis-cli ping
```

---

### Gmail Authentication Error

```text
SMTPAuthenticationError
```

Cause:

Using Gmail password instead of App Password.

Solution:

Generate and use a Google App Password.

---

### Celery Stuck on Windows

Run:

```bash
celery -A tasks worker --pool=solo --loglevel=info
```

instead of:

```bash
celery -A tasks worker --loglevel=info
```

---

## Future Improvements

* Environment variables using `.env`
* Email templates (HTML)
* Celery task monitoring
* Retry mechanism
* Scheduled emails using Celery Beat
* Docker support
* Deployment to AWS or Azure

---

## Author

Demo project for learning FastAPI, Celery, Redis, and asynchronous email processing.
