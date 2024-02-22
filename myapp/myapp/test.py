import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Generate OTP
def generate_otp():
    otp = ""
    for _ in range(6):  # 6-digit OTP
        otp += str(random.randint(0, 9))
    return otp

# Send OTP via Email
def send_otp(email, otp):
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Password Reset OTP"

    body = f"Your OTP for password reset is: {otp}"
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Verify OTP
def verify_otp(user_input, generated_otp):
    return user_input == generated_otp

# Example usage
def main():
    # Step 1: Generate OTP
    otp = generate_otp()

    # Step 2: Send OTP via Email
    user_email = "recipient@example.com"
    send_otp(user_email, otp)
    print("OTP sent successfully!")

    # Simulate user input
    user_input = input("Enter the OTP you received: ")

    # Step 3: Verify OTP
    if verify_otp(user_input, otp):
        print("OTP verified successfully. Proceed with password reset.")
        # Call your password reset function here
    else:
        print("OTP verification failed. Please try again.")

if __name__ == "__main__":
    main()
