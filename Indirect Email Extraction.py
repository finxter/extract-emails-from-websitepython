from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
from tld import get_fld
import time

user_keyword = input("Enter the Website Name: ")

user_keyword = str('"@') + user_keyword +'"'
print(user_keyword)
page = 0
list_email = set()
while page <= 100:
    print("Searching Emails in page No " + str(page))
    time.sleep(10.00)
    google = "https://www.google.com/search?q=" + user_keyword + "&ei=dUoTY-i9L_2Cxc8P5aSU8AI&start=" + str(page)
    response = requests.get(google)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    new_emails = ((re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", soup.text, re.I)))
    list_email.update(new_emails)
    print("Email Extracted: " + str(len(list_email)))
    page = page + 10

n = len(user_keyword)-1
base_url = "https://www." + user_keyword[2:n]
col = "List of Emails " + user_keyword[2:n]
df = pd.DataFrame(list_email, columns=[col])
s = get_fld(base_url)
print(s)
df = df[df[col].str.contains(s) == True]
df.to_csv('email3.csv', index=False)
