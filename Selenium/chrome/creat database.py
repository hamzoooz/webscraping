from selenium  import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8080/phpmyadmin/')

username = browser.find_element('id', 'input_username')
password = browser.find_element('id', 'input_password')
submite = browser.find_element('id' ,'input_go')
username.send_keys("root")
password.send_keys('hamzoooz')

time.sleep(1)
submite.click()

time.sleep(1)
navbar = browser.find_element('xpath', '//*[@id="topmenu"]/li[1]/a').click()

time.sleep(1)
#browser.back()

# Creat database 
#dbfield = browser.find_element('id', 'text_create_db')
new_db = browser.find_element('id', 'text_create_db')
input_db = input('enter name new date base')
#new_db.send_keys('hamzoooz')
new_db.send_keys(input_db)
time.sleep(2)
buttonGo = browser.find_element('id', 'buttonGo').click()
browser.forward()
