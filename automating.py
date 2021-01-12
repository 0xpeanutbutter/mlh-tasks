from selenium import webdriver
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager

def page_loaded(driver):
    return driver.find_element_by_tag_name("body")!=None

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://eduserver.nitc.ac.in/"
driver.get(url)

wait = ui.WebDriverWait(driver,10)
wait.until(page_loaded)


popup = driver.find_element_by_class_name('eupopup-buttons')
popup.click()
print("popup taken care")

email = input("enter mail")

user = driver.find_element_by_id('username')
user.send_keys = email
print("username")

passd = input("ente pwd")
pwd = driver.find_element_by_id('password')
pwd.send_keys = passd
print("password")

submit = driver.find_element_by_tag_name('button')
submit.click()
print('logging in')