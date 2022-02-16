
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://www.youtube.com/')
time.sleep(5)

signin = web.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
signin.click()

Email = "sagar.sws2000@gmail.com"
first = web.find_element_by_xpath('//*[@id="identifierId"]')
first.send_keys(Email)

Submit = web.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
Submit.click()

