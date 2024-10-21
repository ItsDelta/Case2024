# app.py
from flask import Flask, render_template, request
import json
import os
from flask_mail import Mail, Message
from config import Config  # Import the configuration

app = Flask(__name__)

# Apply configuration from config.py
app.config.from_object(Config)

mail = Mail(app)  # Initialize Flask-Mail

# Path to store the onboarding data
DATA_FILE = 'onboarding-data.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data
    formData = {
        'fornavn': request.form['fornavn'],
        'etternavn': request.form['etternavn'],
        'e-post': request.form['e-post'],
        'stilling': request.form['stilling'],
        'adresse': request.form['adresse'],
        'kontonummer': request.form['kontonummer'],
        'pårørende': request.form['pårørende'],
        'startdato': request.form['startdato']
    }

    # Save form data to a JSON file
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = []

    data.append(formData)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

    # Send an email with the form data to HR
    try:
        msg = Message(
            subject=f"Ny Ansatt: {formData['fornavn']} {formData['etternavn']}",
            recipients=["andreas.norway2@gmail.com"],  # HR email address
            body=f"""
            Ansatt Informasjon:
            - Fornavn: {formData['fornavn']}
            - Etternavn: {formData['etternavn']}
            - E-post: {formData['e-post']}
            - Stilling: {formData['stilling']}
            - Adresse: {formData['adresse']}
            - Kontonummer: {formData['kontonummer']}
            - Pårørende: {formData['pårørende']}
            - Startdato: {formData['startdato']}
            """
        )
        mail.send(msg)
        return 'Form submitted successfully and email sent!'
    except Exception as e:
        return f"Form submitted successfully, but failed to send email. Error: {str(e)} Please Contact IT"

if __name__ == '__main__':
    app.run()