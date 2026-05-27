import random
from datetime import *
import pandas as pd
from smtplib import *


now = datetime.now()
today_month=now.month
today_day=now.day
today=(today_month,today_day)
data=pd.read_csv("birthdays.csv")

birthdays_dict= {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    bd_person=birthdays_dict[today]
    filepath=f"letter_{random.randint(1,3)}.txt"
    with open(filepath) as f:
        content=f.read()
        content=content.replace("[NAME]",bd_person["name"])

    my_email="kdark8276@gmail.com"
    pass1="pnmkbdhkdfngozsv"
    with SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=pass1)
        connection.sendmail(from_addr=my_email,
                            to_addrs=bd_person["email"],
                            msg=f"Subject:Happy Birthday! \n\n{content}")






