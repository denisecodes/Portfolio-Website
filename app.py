from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib
app = Flask(__name__)

load_dotenv()

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        send_email(name=name, email=email, phone=phone, message=message)
        return render_template("index.html", msg_sent=True)
    else:
        return render_template("index.html", msg_sent=False)

def send_email(name, email, phone, message):
    my_email = os.environ.get("MY_EMAIL")
    my_password = os.environ.get("MY_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Make connection secure and encrypts email
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{my_email}",
            msg=f"Subject:New Message From Portfolio Website\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )

if __name__ == "__main__":
    app.run(debug=True)