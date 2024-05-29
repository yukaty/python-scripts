from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
from pprint import pprint

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# New instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Access to simple HTTP Request & Response Service
driver.get('https://httpbin.org')

# Click on the HTML form link
driver.find_element(By.LINK_TEXT, "HTML form").click()
print(f"Current URL: {driver.current_url}")

# Input fields
driver.find_element(By.NAME, "custname").send_keys("John Doe")
driver.find_element(By.NAME, "custtel").send_keys("1234567890")
driver.find_element(By.NAME, "custemail").send_keys("john.doe@example.com")
driver.find_element(By.CSS_SELECTOR, "input[name=size][value='medium']").click()
driver.find_element(By.CSS_SELECTOR, "input[name=topping][value='cheese']").click()
driver.find_element(By.NAME, "delivery").send_keys("13:00")
driver.find_element(By.NAME, "comments").send_keys("Please leave it at the front door.")

# Submit form
driver.find_element(By.CSS_SELECTOR, "button").click()
print(f"Current URL: {driver.current_url}")
pprint(driver.page_source)

driver.quit()