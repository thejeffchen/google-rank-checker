from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
import random


# Import CSV of keywords to check rank for
keywords = []
errors = 0

with open('keywords.csv', 'rt', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        keywords.append(row)


for each_keyword in keywords:
    if errors > 5:
        browser.quit()
        break

    driver = webdriver.Chrome()
    driver.get("http://www.google.com")

    search_box = driver.find_element_by_name("q")
    search_box.send_keys(each_keyword)
    search_box.send_keys(Keys.RETURN)

    html = driver.page_source

    def listToStringWithoutBracketsOrQuotations(list1):
        return str(list1).replace('[','').replace(']','').replace('\'','')

    each_keyword = listToStringWithoutBracketsOrQuotations(each_keyword)
    
    with open("html/" + str(each_keyword) + ".html", "w") as file:
        file.write(html)

    time.sleep(random.randint(1,4))

