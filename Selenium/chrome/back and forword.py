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
dbfield = browser.find_element('id', 'text_create_db')



time.sleep(2)
browser.forward()

#time.sleep(2)
#browser.quit()



