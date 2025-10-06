# ----------------- Day 47 starts here ---------------
from bs4 import BeautifulSoup
import requests
import smtplib
import os

live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
response = requests.get("https://appbrewery.github.io/instant_pot/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.title)
price = soup.find(name="p", class_ = "a-spacing-none").get_text().split("$")[1]
# print(price.get_text())
# print(price)
product_title = soup.find(id="productTitle").get_text().strip()
# print(product_title)

if float(price) < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="****@gmail.com", msg=f"Subject:Amazon Price Alert!\n\n {product_title} is in sale for {price}\n{live_url}".encode("utf-8"))





