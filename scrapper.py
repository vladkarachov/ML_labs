from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

import time

def getViews(text):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.addArguments("window-size=1800x900")
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    views = 0
    try:
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)
        link = driver.find_element_by_css_selector("#rso > div:nth-child(1) > div > div.r > a")
        link.click()
        views = driver.find_element_by_class_name("post-item__views").text
    except BaseException:
        pass
    driver.close()
    driver.quit()
    return views


category_view = {}
category_iter = {}

list_of_files = pd.read_csv("res.csv", header=None)
list_of_files.head()
list_of_files=list_of_files[(list_of_files[3]=='Top/Showbiz/Music/Eurovision')]
list_of_files=list_of_files[(list_of_files[0].str.contains("Mus"))]
for index, row in list_of_files.iterrows():
    file = open('texts/' + row[0] + '.txt', "r", encoding='utf-8')
    text = file.read(100)+" korrespondent.net"
    category = row[3]
    if (category_iter.setdefault(row[3], 0) < 10):
        try:
            views = getViews(text)
            if views != 0:
                a=category_view.setdefault(row[3], 0)
                category_view[row[3]] = a+int(views)
                category_iter.update({row[3]: int(category_iter[row[3]]+ 1)})
        except BaseException:
            pass
        print(row[0])
res = {key: category_view[key] // category_iter.get(key, 0)
       for key in category_view.keys()}
print(res)
print(category_view)
print(category_iter)
