import time
import yagmail
from imapclient import IMAPClient
import email
import requests
import os

# Configuration (replace with your actual credentials or use environment variables)
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'your_gmail@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_app_password')
IMAP_SERVER = os.getenv('IMAP_SERVER', 'mail.naasbd.com')
IMAP_PORT = int(os.getenv('IMAP_PORT', '993'))
SMTP_SERVER = os.getenv('SMTP_SERVER', 'mail.naasbd.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '465'))
CHATBOT_API_URL = os.getenv('CHATBOT_API_URL', 'http://localhost:8000/ask')

CHECK_INTERVAL = 20  # seconds


def get_unread_emails():
    with IMAPClient(IMAP_SERVER, port=IMAP_PORT, use_uid=True, ssl=True) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.select_folder('INBOX')
        messages = server.search(['UNSEEN'])
        for uid, message_data in server.fetch(messages, ['RFC822']).items():
            msg = email.message_from_bytes(message_data[b'RFC822'])
            yield uid, msg, server


def process_email(msg):
    subject = msg.get('Subject', '')
    from_addr = email.utils.parseaddr(msg.get('From'))[1]
    message_id = msg.get('Message-ID')
    in_reply_to = msg.get('In-Reply-To')
    references = msg.get('References')
    # Get plain text body
    body = ''
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True).decode(errors='ignore')
                break
    else:
        body = msg.get_payload(decode=True).decode(errors='ignore')
    return subject, from_addr, body, message_id, in_reply_to, references


def get_chatbot_reply(question, sender):
    # Call your chatbot API endpoint
    response = requests.post(CHATBOT_API_URL, json={"query": question, "user": sender})
    if response.ok:
        return response.json().get('response', 'Sorry, I could not process your question.')
    return 'Sorry, there was an error contacting the chatbot.'


def reply_email(to_addr, subject, body, in_reply_to, references):
    yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD, host=SMTP_SERVER, port=SMTP_PORT, smtp_ssl=True)
    headers = {}
    if in_reply_to:
        headers['In-Reply-To'] = in_reply_to
    if references:
        headers['References'] = references
    yag.send(
        to=to_addr,
        subject=subject,
        contents=body,
        headers=headers
    )


def main():
    print('Starting email bot...')
    while True:
        try:
            for uid, msg, server in get_unread_emails():
                subject, from_addr, body, message_id, in_reply_to, references = process_email(msg)
                print(f'Processing email from {from_addr} with subject: {subject}')
                answer = get_chatbot_reply(body, from_addr)
                reply_email(
                    to_addr=from_addr,
                    subject=f"Re: {subject}",
                    body=answer,
                    in_reply_to=message_id,
                    references=references
                )
                # Mark as read
                server.add_flags(uid, [b'\\Seen'])
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
