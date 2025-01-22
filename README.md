# Keylogger with Email Reporting

This project implements a basic keylogger with optional email reporting functionality. It records keypresses into a log file and can periodically send encrypted logs via email.

## Features
- **Key Logging**: Logs all keypresses to a file with rotation.
- **Encryption**: Uses Base64 encoding for log encryption.
- **Email Reporting**: Sends logs via email at regular intervals.
- **Stealth Mode**: Runs without displaying a console window on Windows.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - `pynput`
  - `smtplib`
  - `email`
  - `base64`
- A Gmail account for email reporting.

## Configuration
Modify the following configuration variables in the code:

### Logging Configuration
- `LOG_FILE`: Name of the log file.
- `LOG_MAX_SIZE`: Maximum size of the log file before rotation.
- `LOG_BACKUP_COUNT`: Number of backup log files to keep.

### Email Configuration
- `SMTP_SERVER`: Set to `'smtp.gmail.com'` for Gmail.
- `SMTP_PORT`: Set to `587` for Gmail.
- `SMTP_USER`: Your Gmail address (e.g., `arulsci@gmail.com`).
- `SMTP_PASSWORD`: Your Gmail password (ensure it is securely stored).
- `EMAIL_RECEIVER`: Recipient email address (e.g., `arulartad@gmail.com`).
- `EMAIL_INTERVAL`: Interval in seconds to send logs (default: 60).

### Additional Settings
- `ENCRYPT_LOG`: Enable or disable log encryption (default: `True`).
- `STEALTH_MODE`: Enable or disable stealth mode (default: `True`).

## Usage
1. Install the required libraries:
   ```bash
   pip install pynput
   ```

2. Run the script:
   ```bash
   python keylogger.py
   ```

3. Press the `ESC` key to stop the keylogger.

## Notes
- Use this code responsibly. Unauthorized use of keyloggers is illegal and unethical.
- Protect your email password. Use environment variables or secure credential storage.
- Modify and extend the encryption mechanism for better security in production.

## Disclaimer
This project is intended for educational purposes only. The author is not responsible for any misuse or legal consequences arising from the use of this code.

