
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://web.whatsapp.com/')
time.sleep(10)

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="pane-side"]/div[2]/div/div/div[11]/div/div/div/div[2]/div[1]/div[1]/span') 
RadioButtonPeriod.click()


Answer = "Hello Vicks..."
last = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
last.send_keys(Answer)

Submit = web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
Submit.click()
