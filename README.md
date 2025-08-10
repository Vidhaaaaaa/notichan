
# 📬 Notichan

*A FastAPI-based Gmail && Outlook automation tool*

## Overview

Noti-chan is a simple backend service that connects to your Gmail and Outlook account, fetches unread emails, and gives you a summary every morning, even before you wake up.
Currently in active development, features and integrations will expand over time.

---

## Current Tech Stack (will be updated as progressed)

* **Python**
* **FastAPI**
* **Google Gmail API**
* **Outlook API**

---

## Setup (Development)

1. Enable Gmail API in Google Cloud Console and download `credentials.json`.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the API:

   ```bash
   uvicorn app.main:app --reload
   ```
4. Open docs at:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## Status

🚧 **Work in progress** — features may change.
