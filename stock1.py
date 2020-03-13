import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Company:
    def __init__(self,url):
        self.url = url

    def fill(self,name,value,change,pchange):
        self.name = name
        self.value = value
        self.change = change
        self.pchange = pchange
    
    def getStock(self):
        # url = self.url
        try:
            print("uw")
            page = urlopen(self.url)
            soup = bs4.BeautifulSoup(page,"html.parser")
            name=soup.find('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find('h1').text
            value=soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
            s = value[1].text.split(' ')
            self.fill(name,value[0].text,s[0],s[1])
        except:
            print("Error opening the URL")



# url = 'https://in.finance.yahoo.com/quote/TITAN.NS?p=TITAN.NS'
# c1 = Company(url)
# c1.getStock()
# print(c1.name + "  " + c1.value + " " + c1.change + " " + c1.pchange)




















# url = 'https://in.finance.yahoo.com/quote/TITAN.NS?p=TITAN.NS'
# try:
#     page = urlopen(url)
#     soup = bs4.BeautifulSoup(page,"html.parser")
#     name=soup.find('div',{'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find('h1').text
#     print(name)
#     value=soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find_all('span')
#     print(value[0].text)
#     print(value[1].text)
# except:
#     print("Error opening the URL")
