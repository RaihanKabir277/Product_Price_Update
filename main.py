# ----------------- Day 47 starts here ---------------
from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup.title)

