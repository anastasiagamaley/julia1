
from flask import Flask, render_template, request
import smtplib

OWN_EMAIL = "anastasiagamaley@gmail.com"
OWN_PASSWORD = "Armagedon1"
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')



@app.route('/portfolio')
def portfolio():
    return render_template('portfolio-2.html')


@app.route('/videos')
def videos():
    return render_template('portfolio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data['email']
        subject = data['subject']
        text = data['message']
        send_email(name, email, subject, text)
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

def send_email(name, email, subject, text):
    email_message = f"Subject: {subject}\n\nName: {name}\nEmail: {email}\nMessage:{text}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
