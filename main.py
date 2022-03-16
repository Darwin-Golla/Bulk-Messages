import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code:')
time.sleep(5)
sleep_time = 1

data = pd.read_excel('Contacts.xlsx', sheet_name='Sheet1', engine='openpyxl')
names = data['name']
# numbers = data['wa_number']

for name in names:
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    time.sleep(sleep_time)
    search_box.clear()
    search_box.send_keys(name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(sleep_time)
    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    time.sleep(sleep_time)
    # message_box.send_keys('hi, testing' + Keys.RETURN)
    message_box.clear()
    # message_box.send_keys(Keys.CONTROL, "v")
    # time.sleep(sleep_time)
    attach = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    time.sleep(sleep_time)
    attach.send_keys("Greetings of the Day ...! This is to intimate that for both 100% Qatari and non-Qatari companies filing of tax returns for the financial year 2021  began from 01st January 2022 onwards. To submit the tax returns please do contact us . Thank you ,Mr.Hafiz , AK & Partners. Mobile:  30947609 ")
    attach.send_keys(Keys.ENTER)
    time.sleep(sleep_time)
    print(name)