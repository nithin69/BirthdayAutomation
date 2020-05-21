import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from greetings import sendEmail


if __name__ == "__main__":
    df = pd.read_excel('data.xlsx')
    today = datetime.datetime.now().strftime("%d-%m")
    yearnow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if (today == bday) and yearnow not in str(item['Year']):
            sendEmail(item["Email"], "Happy Birthday", item["Dialogue"])
            sendSMS(item["Phone"])
            writeInd.append(index)

    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i,'Year'] = str(yr) + ',' + str(yearnow)

    df.to_excel('data.xlsx')