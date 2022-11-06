from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8080/phpmyadmin/')

username = browser.find_element('id', 'input_username')
password = browser.find_element('id', 'input_password')
submite = browser.find_element('id' ,'input_go')

username.send_keys("root")
password.send_keys("hamzoooz")
time.sleep(1)
submite.click()


print(browser.get_cookies())
print(browser.get_cookie("phpMyAdmin"))
browser.delete_cookie("phpMyAdmin")
browser.delete_all_cookies()
print(browser.get_cookies())
time.sleep(5)
browser.quit()
