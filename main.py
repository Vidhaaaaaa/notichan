from handlers.gmail_handler import get_gmail_service, fetch_unread_emails, mark_as_read

service  = get_gmail_service()
emails  = fetch_unread_emails(service)