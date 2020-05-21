# BirthdayAutomation

# way2sms

create a account at sms4india.com and get keys

# gmail

enable less secure connection in gmail settings

##### install requirments
pip install -r requirments.txt

### running code
Add details in data.xlsx

Add api key, api secret, userType: 'prod' or 'stage' (for test it is stage and for live keys it is prod) and senderid in sendSMS function

Add gmail user name and password in sendEmail function

and run python bdayMain.py

##
to run automatically push the code to server and create a cron job that runs at 12:00 AM every day
