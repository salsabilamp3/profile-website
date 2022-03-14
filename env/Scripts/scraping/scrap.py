import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

page = requests.get("https://republika.co.id/")

obj = BeautifulSoup(page.text,'html.parser')

data = []
time = datetime.now()
f = open('env\Scripts\scraping\\headline.json', 'w')
for headline in obj.find_all('div', class_='conten1'):
    data.append({"judul": headline.find('h2').text,"kategori": headline.find('a').text,
    "waktu_publish": headline.find('div',class_='date').text,"waktu_scraping": time.strftime("%Y-%m-%d %H:%M:%S")})
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close

# print('Menampilkan Objek html')
# print('======================')
# print(obj)

# print('Menampilkan title dengan tag')
# print('======================')
# print(obj.title)

# print('Menampilkan title dengan tag')
# print('======================')
# print(obj.title.text)

# print('Menampilkan semua tag h2')
# print('======================')
# print(obj.find_all('h2'))

# print('Menampilkan semua teks h2')
# print('======================')
# for headline in obj.find_all('h2'):
#     print(headline.text)

# print('Menampilkan headline berdasarkan div class')
# print('======================')
# print(obj.find_all('div', class_='bungkus_txt_headline_center'))

# print('Menampilkan headline berdasarkan div class')
# print('======================')
# for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
#     print(headline.find('h2').text)

# print('Menyimpan headline pada file text')
# print('======================')
# f = open('F:\\headline.txt', 'w')
# for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
#     f.write(headline.find('h2').text)
#     f.write('\n')
# f.close()

