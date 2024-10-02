from datetime import datetime
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText

# Get today's date
today = datetime.now()
Date = (today.month, today.day)

# Gmail credentials
MY_EMAIL = "MAIL@gmail.com"
PASSWORD = "PASS"  # Replace with your actual app-specific password if 2FA is enabled

# Read the birthdays.csv file
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# If today's date matches a birthday
if Date in birthdays_dict:
    # Choose a random letter template
    Number = random.randint(1, 3)
    file_path = f"letter_templates/letter_{Number}.txt"

    # Get birthday person's details
    birthday_person = birthdays_dict[Date]

    # Open and customize the letter template
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Email sending setup
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secures the connection
        connection.login(MY_EMAIL, PASSWORD)  # Logs in to Gmail

        # Send the email
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],  # Assuming the email field exists in the CSV
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        print("Email sent successfully!")
