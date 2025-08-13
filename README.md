btw yes, i meant "refactor" in my commit messages. "refractor" just sounds cooler

# NotiChan – Email to Telegram Bot

NotiChan is a small Python tool that checks your Gmail and Outlook inbox for unread emails and sends them straight to your Telegram every morning. Perfect for when you don’t feel like opening your inbox first thing in the day.

---

## Features

- Fetch unread emails from **Gmail** and **Outlook**
- Sends them to your **Telegram** chat automatically
- Simple, lightweight, and easy to customize

---

## ⚙Setup

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/notichan.git
cd notichan
```

### 2. Create a virtual environment (recommended)

```bash
# Create venv
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Mac/Linux)
source venv/bin/activate
```

**Why:** Keeps dependencies isolated so they don’t mess with your other Python projects.

### 3. Install requirements

```bash
pip install -r requirements.txt
```

**Why:** `requirements.txt` lists every Python package this bot needs with exact versions for smooth setup.

---

## Environment Variables

Create a `.env` file in the root folder with:

```
IMAP_ADDRESS=outlook.office365.com
OUTLOOK_USER=you@outlook.com or your organisation's outlook id
OUTLOOK_PASSWORD=your_password
NOTNOTICHAN_TOKEN=telegram_bot_token
NOTNOTICHAN_ID=your_chat_id
```

---

## ▶️ Running the Bot

Run locally:

```bash
python main.py
```

## Automation

- **Local:** Use Windows Task Scheduler to run `main.py` at your desired time.
- **Cloud:** Use a VPS or Railway with a cron job to run the script automatically.

---

## File Structure

```
notichan/
│── handlers/
│   ├── gmail_handler.py
│   ├── outlook_handler.py
│── NotnotichanBot.py
|── main.py
│── requirements.txt
│── .env
│── credentials.json
```

## Final Notes

- For Gmail, you’ll need API credentials from Google Cloud Console.
- For Outlook, make sure IMAP is enabled and credentials are correct.
- Tested on Python 3.10+.
- Add your `credentials.json` for Gmail in the project root.
