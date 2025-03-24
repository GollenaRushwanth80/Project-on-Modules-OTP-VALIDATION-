# OTP Verification using Python

## Description
This is a simple Python script to generate and send a One-Time Password (OTP) via email for verification. The script uses the `smtplib` module to send emails through Gmail's SMTP server and the `email.mime` module to format the email message. A randomly generated 4-digit OTP is sent to the user's email, which they must enter correctly to complete verification.

## Features
- Generates a random 4-digit OTP.
- Sends the OTP via email.
- Validates the OTP entered by the user.
- Secure login using an app password.

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
4. Enter the recipient's email when prompted.
5. Enter the OTP received in the email to verify.

## Code Explanation
1. **Generate OTP:** A random 4-digit OTP is generated using `random.randint(1111, 9999)`.
2. **Email Configuration:** The script uses `smtplib.SMTP` to connect to Gmail's SMTP server (`smtp.gmail.com` on port 587).
3. **Sending OTP:** The OTP is sent as a plain text email.
4. **User Validation:** The user enters the OTP received via email, and the script validates it.

## Security Note
- Never hardcode credentials in the script. Use environment variables or a config file.
- Use an **App Password** instead of your main Gmail password for security.
- Enable **Two-Factor Authentication (2FA)** on your Gmail account.


