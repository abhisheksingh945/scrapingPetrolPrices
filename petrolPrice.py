import requests
from bs4 import BeautifulSoup
from csv import writer

response_petrol = requests.get(
    'https://www.mypetrolprice.com/petrol-price-in-india.aspx')

soup_petrol = BeautifulSoup(response_petrol.text, 'html.parser')
mydivs_petrol = soup_petrol.findAll("div", {"class": "SF"})

print("petrol_prices")
# printing petrol prices
for div in mydivs_petrol:
    price = div.find("div", {"class": "txtC"}).text[2:8]
    city = div.find("div", {"class": "CH"}).find_all(
        "a")[1]["href"].split('/')[4].split('-')[3].replace('_', ' ')
    print(city, price)


response_diesel = requests.get(
    'https://www.mypetrolprice.com/diesel-price-in-india.aspx')

soup_diesel = BeautifulSoup(response_diesel.text, 'html.parser')
mydivs_diesel = soup_diesel.findAll("div", {"class": "SF"})

print("diesel_prices")
# printing diesel prices
for div in mydivs_diesel:
    price = div.find("div", {"class": "txtC"}).text[2:8]
    city = cost = div.find("div", {"class": "CH"}).find_all(
        "a")[1]["href"].split('/')[4].split('-')[3].replace('_', ' ')
    print(city, price)
