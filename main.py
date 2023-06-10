from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# pageNum = 1
oldDatas = []  # Datas until 2013(page 1 to 10)
newDatas = []  # Datas in 2023 (page 580 to 590)


def webscrape(start_page, end_page):
    datas = []
    driver = webdriver.Chrome()
    while start_page <= end_page:
        url = "https://eksisozluk1923.com/suriyeli-siginmacilar--3488850?p=" + str(start_page)
        driver.get(url)
        elements = driver.find_elements(By.CLASS_NAME, "content")

        for element in elements:
            datas.append(element.text)
        start_page = start_page + 1

    # Close the Selenium driver
    driver.quit()

    return datas


oldDatas = webscrape(1, 10)
newDatas = webscrape(580, 590)


def write_to_csv(filename, old_data, new_data):
    fieldnames = ['Old Data', 'New Data']

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for old, new in zip(old_data, new_data):
            writer.writerow({'Old Data': old, 'New Data': new})


write_to_csv('surian.csv', oldDatas, newDatas)
