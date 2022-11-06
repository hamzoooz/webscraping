from selenium  import webdriver
import time

# this driver app to control in browser 
browser = webdriver.Chrome()
#browser = webdriver.firefox()
#here to get web site 
browser.get('https://google.com/')
#determind element by id we can get element by name or class or xpath 
input = browser.find_element('name', 'q')

#submite = browser.find_element('tag name' ,'submite')
# send values to input feilds & we can send directly when declaar variable 
input.send_keys("@hamzoooz")
#submite.click()
input.click()
time.sleep(5)