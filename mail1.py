import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient_email,ue):
    sender_email = 'Sriswaminathcafe4@gmail.com'
    sender_password = "gfmc kjpx xdpd bhoq"  # Use an app-specific password if you have 2FA enabled
    subject = "This mail is to inform you that your booking at Sri Swaminath Cafe is confirmed.Have a fine Dining!"
    with open("Seat1.txt", 'r') as file:
        line = file.readline().strip()  # Read the first line and remove any leading/trailing whitespace
        ue,b=line.split(",")    # Split the line into two parts using comma as delimiter


    body = (
        f"Dear {ue},\n\n"
    f"We are delighted to confirm your booking at Sriswaminath Cafe. We trust you will have a wonderful experience with us and look forward to welcoming you .\n\n"
    f"Your booked table is confirmed, and your table number is: {b}.\n\n"
    f"Should you have any queries or wish to share feedback about any aspect of our restaurant, please do not hesitate to get in touch. We value your feedback and strive to make every visit memorable.\n\n"
    f"You can reach us via email at Sriswaminathcafe4@gmail.com or by phone at 9790901427.\n\n"
    f"Thank you for choosing Sriswaminath Cafe. We anticipate your visit and hope to exceed your expectations.\n\n"
    f"Warm regards,\n\n"
    f"Sriswaminath Cafe"
)
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()
        # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
    customer_email=recipient_email


    recipient_email = sender_email
    subject = "Table Booking"
          # Split the line into two parts using comma as delimiter

    body = (

        f"customer Name:{ue}\n"
        f"Customer Email :{customer_email}\n"
        f"Booked seat:{b}"

            )
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Add body to email
        message.attach(MIMEText(body, 'plain'))

        # Use Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login to the SMTP server
        text = message.as_string()  # Convert the message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()  # Close the connection
    except Exception as e:
        print(f'Failed to send email. Error: {e}')
