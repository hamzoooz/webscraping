from selenium import webdriver
import time
import datetime

browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8080/phpmyadmin/')

username = browser.find_element('id', 'input_username')
password = browser.find_element('id', 'input_password')
submite = browser.find_element('id' ,'input_go')

username.send_keys("root")
password.send_keys("hamzoooz")
# time.sleep(.5)
submite.click()

browser.save_screenshot(str(datetime.datetime.now()) + ".png")
time.sleep(5)
browser.quit()



