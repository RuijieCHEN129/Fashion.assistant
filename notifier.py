import smtplib
from email.message import EmailMessage

class EmailNotifier:
    def __init__(self, config):
        self.config = config.get('email_settings', {})

    def send_email(self, prefs, suggestions):
        msg = EmailMessage()
        msg['Subject'] = 'Fashion Suggestions'
        msg['From'] = self.config.get('username', '')
        msg['To'] = self.config.get('recipient', '')
        body = f"Based on your preferences {prefs}, here are suggestions:\n"
        for idx, o in enumerate(suggestions, 1):
            body += f"{idx}. {o['top']}, {o['bottom']}, {o['shoes']}\n"
        msg.set_content(body)
        with smtplib.SMTP(self.config.get('smtp_server', 'localhost'), self.config.get('smtp_port', 25)) as s:
            s.send_message(msg)

