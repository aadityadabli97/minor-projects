# This project is to Send email on a particular day using python
# Here I have use datetime module for date and time , smtplib module for email , and random module to perform random choice  

import datetime, smtplib, random

now = datetime.datetime.now()
day = now.weekday()

# Monday is 0 in daytime module

if day == 5:
    with open("quotes.txt", encoding="utf8") as quote:
        lines = quote.readlines()
        quote_of_the_day = random.choice(lines)
    my_email = "ananddabli@gmail.com"
    password = "ftih mwkj dgrz uuyf"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rkbaby6@gmail.com",
                            msg=f"Subject:quote_of_the_day\n\n{quote_of_the_day}".encode("utf8"))
