from selenium  import webdriver
import time

# this driver app to control in browser 
browser = webdriver.Chrome()
#browser = webdriver.firefox()
#here to get web site 
browser.get('http://127.0.0.1:8080/phpmyadmin/')
#determind element by id we can get element by name or class or xpath 
username = browser.find_element('id', 'input_username')
password = browser.find_element('id', 'input_password')
submite = browser.find_element('id' ,'input_go')
# send values to input feilds & we can send directly when declaar variable 
username.send_keys("root")
password.send_keys("hamzoooz")
# to waite some time to next action 
time.sleep(2)
# click on botton 
submite.click()

time.sleep(5)

#browser.quit()