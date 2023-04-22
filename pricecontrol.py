from email import message
from turtle import title
from urllib import request
import requests
from bs4 import BeautifulSoup



website=requests.get("https://www.monsternotebook.com.tr/tulpar/monster-tulpar-t7-v22-2/")
res = website.content
req1 = BeautifulSoup(res, 'html.parser')
baslik =req1.find(class_="emos_H1").get_text()
fiyat1 =req1.find(id="ctl00_u21_ascUrunDetay_dtUrunDetay_ctl00_lblSatisFiyat").get_text().split(",")
fiyat=float(fiyat1[0])
print(baslik)
print(fiyat)
if fiyat<20.000:
    requests.get("https://api.telegram.org/bot<Token>?chat_id=<chat_id>&text=İstediğiniz:"+baslik +" fiyatı "+ str(fiyat)+" TL'ye düşmüştür.")
