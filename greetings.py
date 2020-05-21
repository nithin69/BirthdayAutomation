import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json

def sendSMS(to):
    response = requests.post('https://www.sms4india.com/api/v1/sendCampaign', {"apikey":'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',"secret":'xxxxxxxxxxxxxxxxxxx',"usetype":'stage',"senderid":'xxxxxxxxxxxx',"phone":to,"message":'May you have all the love your heart can hold, all the happiness a day can bring, and all the blessings a life can unfold. Happy birthday!'})
    print(response.text)
    return (response.text)


def sendEmail(to, sub, msg):
    sender_email = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    receiver_email = to
    password = "xxxxxxxxxxxxxxx"

    message = MIMEMultipart("alternative")
    message["Subject"] = sub
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
                    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">

                    <head>
                        <meta name="viewport" content="width=device-width" />
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                        <title>Verify Your Email - FindGenie</title>
                                <style>img {
                                max-width: 100%;
                                }
                                body {
                                -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: none; width: 100% !important; height: 100%; line-height: 1.6em;
                                }
                                body {
                                background-color: #f6f6f6;
                                }
                                @media only screen and (max-width: 640px) {
                                body {
                                    padding: 0 !important;
                                }
                                h1 {
                                    font-weight: 800 !important; margin: 20px 0 5px !important;
                                }
                                h2 {
                                    font-weight: 800 !important; margin: 20px 0 5px !important;
                                }
                                h3 {
                                    font-weight: 800 !important; margin: 20px 0 5px !important;
                                }
                                h4 {
                                    font-weight: 800 !important; margin: 20px 0 5px !important;
                                }
                                h1 {
                                    font-size: 22px !important;
                                }
                                h2 {
                                    font-size: 18px !important;
                                }
                                h3 {
                                    font-size: 16px !important;
                                }
                                .container {
                                    padding: 0 !important; width: 100% !important;
                                }
                                .content {
                                    padding: 0 !important;
                                }
                                .content-wrap {
                                    padding: 10px !important;
                                }
                                .invoice {
                                    width: 100% !important;
                                }
                                }
                    </style></head>

                    <body itemscope="" itemtype="http://schema.org/EmailMessage" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: none; width: 100% !important; height: 100%; line-height: 1.6em; margin: 0;" bgcolor="#f6f6f6">

                        <table class="body-wrap" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; width: 100%; margin: 0;" bgcolor="#f6f6f6">
                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;" valign="top"></td>
                                <td class="container" width="600" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; display: block !important; max-width: 600px !important; clear: both !important; margin: 0 auto;" valign="top">
                                    <div class="content" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; max-width: 600px; display: block; margin: 0 auto; padding: 20px;">
                                        <table class="main" width="100%" cellpadding="0" cellspacing="0" itemprop="action" itemscope="" itemtype="http://schema.org/ConfirmAction" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; border-radius: 3px; margin: 0; border: 1px solid #e9e9e9;" bgcolor="#fff">
                                            <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                                <td class="content-wrap" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0; padding: 20px;" valign="top">
                                                    <meta itemprop="name" content="Confirm Email" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;" />
                                                    <table width="100%" cellpadding="0" cellspacing="0" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                                        
                                                        <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 30px; margin: 0;">
                                                            <td class="content-block" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 30px; margin: 0; padding: 0 0 20px;" valign="top">
                                                                <center>
                                                                    <span>&#128079;</span>
                                                                    <span>&#128079;</span>
                                                                        HAPPY BIRTHDAY!
                                                                    <span>&#127851;</span>
                                                                    <span>&#127874;</span>
                                                                </center>
                                                            </td>
                                                        </tr>

                                                        <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                                            <td class="content-block" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0; padding: 0 0 20px;" valign="top">
                                                                <b>“Wishing you a day filled with happiness and a year filled with joy. Happy birthday!” </b><br>
                                                                <b>“Sending you smiles for every moment of your special day…Have a wonderful time and a very happy birthday!”</b><br>
                                                            </td>
                                                        </tr>
                                                        <tr style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">
                                                            <td class="content-block" style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0; padding: 0 0 20px;" valign="top">
                                                                <img src="https://i.pinimg.com/736x/ee/f0/36/eef036f583e91a438896a377716ea85e.jpg" style="width: 250px, height: 250px"/>
                                                            </td>
                                                        </tr>

                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
                                <td style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;" valign="top"></td>
                            </tr>
                        </table>
                    </body>

                    </html>"""

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
