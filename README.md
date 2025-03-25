# Bulk OTP Verification using Python

## Description
This Python script allows sending One-Time Passwords (OTPs) to multiple email recipients for verification. It uses the `smtplib` module to send emails via Gmail's SMTP server and the `email.mime` module to format email messages. Each recipient receives a unique OTP that must be entered correctly for verification.

## Features
- Sends OTPs to multiple recipients.
- Generates a unique 4-digit OTP for each recipient.
- Secure email transmission using TLS.
- Validates OTP input from users.

## Requirements
- Python 3.x
- A Gmail account with an app password

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/otp-verification.git
   cd otp-verification
   ```
2. Install required dependencies (if necessary):
   ```sh
   pip install smtplib email
   ```

## Usage
1. Enable **Less Secure Apps** or generate an **App Password** for Gmail authentication.
2. Modify the script to include your Gmail credentials:
   ```python
   server.login("your-email@gmail.com", "your-app-password")
   ```
3. Run the script:
   ```sh
   python otp_verification.py
   ```
4. Enter the number of recipients.
5. Input email addresses one by one.
6. Each recipient will receive a unique OTP.
7. Enter the OTP received in the email to validate.

## Code Explanation
1. **Collect Emails:** The script prompts the user to enter multiple email addresses.
2. **Generate OTP:** A random 4-digit OTP is generated using `random.randint(1111, 9999)`.
3. **Email Configuration:** The script connects to Gmail's SMTP server (`smtp.gmail.com` on port 587) using `smtplib.SMTP`.
4. **Sending OTP:** Each email address receives a unique OTP in a formatted email.
5. **User Validation:** The user must enter the received OTP for verification.

## Security Note
- Never hardcode credentials in the script. Use environment variables or a config file.
- Use an **App Password** instead of your main Gmail password for security.
- Enable **Two-Factor Authentication (2FA)** on your Gmail account.



