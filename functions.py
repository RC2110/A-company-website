import smtplib, ssl


def send_email(message):
    global host, port, password
    host = "smtp.gmail.com"
    port = 465
    context1 = ssl.create_default_context()
    user_email = "rajaachandramohan@gmail.com"
    password = "xyqy mith nmpd dlaz"
    receiver = "rajaachandramohan@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context1) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)

