import smtplib
import email.message

import Speak
from Speech_Recognition import voice_recognizer

message = email.message.Message()
password = "FoxAlive123"
s = smtplib.SMTP('smtp.gmail.com: 587')


def send_email():
    s.starttls()
    s.login(message['From'], password)
    s.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
    print("Email enviado")


def send_email_to(content, somone):
    email_body = """
        <p> Lembrando que, </p>
        <p>""" + content + """</p>
        <p>Luis.</p>
        """

    message['Subject'] = "Email Automatico"
    message['From'] = "trudynhafox@gmail.com"
    message['To'] = somone
    message.add_header('Content-Type', 'text/html')
    message.set_payload(email_body)

    send_email()

def send_email_to_myself(content):
    email_body = """
    <p> Lembrando que, </p>
    <p>"""+content+"""</p>
    <p>Luis.</p>
    """

    message['Subject'] = "Email Automatico"
    message['From'] = "trudynhafox@gmail.com"
    message['To'] = "trudynhafox@gmail.com"
    message.add_header('Content-Type', 'text/html')
    message.set_payload(email_body)

    send_email()


if __name__ == "__main__":
    text = voice_recognizer()
    print(text)
    if text == "mande um e-mail":
        send_email_to_myself("Olaaaa")