from selenium import webdriver
from selenium.webdriver.support import ui
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://eduserver.nitc.ac.in/"
driver.get(url)

wait = ui.WebDriverWait(driver,10)
wait.until(page_loaded)


email = '*****'
passd = '*****'

driver.find_element_by_xpath('//*[@id="username"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(passd)
driver.find_element_by_xpath('//*[@id="region-main"]/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

print("logged in")
driver.implicitly_wait(5)
driver.find_element_by_link_text('Attendance').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('Go to activity').click()

driver.implicitly_wait(3)
driver.find_element_by_link_text('Submit attendance').click()

driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="id_status_3318"]').click()
driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()

print("attendance done")