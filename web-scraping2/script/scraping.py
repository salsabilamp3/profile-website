from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import json
from datetime import datetime
import time

PATH = "C:/xampp/htdocs/profile-website/web-scraping2/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/list/ls063868899/")

serieslist = []
waktu = datetime.now()
i = 1
for series in driver.find_elements_by_class_name("lister-item"):
    driver.execute_script(f'window.scrollBy(0, 250)')
    header = series.find_element_by_class_name("lister-item-header")
    try:
        judul = header.find_element_by_tag_name("a").text
    except NoSuchElemenException as e:
        judul = "No title"

    try:
        tahun = header.find_element_by_class_name("lister-item-year").text
    except NoSuchElemenException as e:
        tahun = "No year"

    try:
        durasi = series.find_element_by_class_name("runtime").text
    except NoSuchElementException as e:
        durasi = "No runtime"
    
    try:
        genre = series.find_element_by_class_name("genre").text
    except NoSuchElementException as e:
        genre = "No genre"

    try:
        rating = series.find_element_by_class_name("ipl-rating-star").text
    except NoSuchElementException as e:
        rating = "No rating"
        
    try:
        img = series.find_element_by_class_name("lister-item-image")
        gambar = img.find_element_by_tag_name('img').get_attribute("src")
        urllib.request.urlretrieve(gambar, "assets/images/"+ str(i)+".jpg")
    except NoSuchElementException as e:
        gambar = "No image"

    print(i)
    print(judul)
    print(tahun)
    print(durasi)
    print(genre)
    print(rating)
    print(gambar)

    serieslist.append(
        {
            "no": i,
            "judul": judul,
            "tahun": tahun,
            "durasi": durasi,
            "genre": genre,
            "rating": rating,
            "image": gambar,
            "waktu_scrap": waktu.strftime("%Y-%m-%d %H:%M:%S")
        }
    )
    i = i + 1
hasil_scraping = open("scrapHBO.json", "w")
json.dump(serieslist, hasil_scraping, indent = 6)
hasil_scraping.close()
time.sleep(0.5)
driver.quit()