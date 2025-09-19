import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Nishant Tripathi'
email['to'] = 'tripathinishant498@gmail.com'
email['subject'] = 'This is a test email'
email.set_content("Hello! This is the content of the email sent from Python 😊")

# ✅ Connect to Gmail SMTP server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # Secure the connection
    smtp.login("tripathivijay020@gmail.com", "Nishant@123")
    smtp.send_message(email)
    print("✅ Email sent successfully!")
