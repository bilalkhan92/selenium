from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open website
driver = webdriver.Chrome()
driver.get('https://auth.s1.exacttarget.com/hub-cas/login?service=https%3a%2f%2fmc.s4.exacttarget.com%2fcloud%2flogin.html%3fhash%3dOrEn1bG9nZ2VkLWluSXc9PQ2')

usr = driver.find_element_by_name("username")
usr.send_keys("USER")

pwd = driver.find_element_by_name("password")
pwd.send_keys("PASS")

driver.find_element_by_id("submit-btn").click()

driver.get("https://mc.s4.exacttarget.com/cloud/#app/Email")

driver.get("https://mc.s4.exacttarget.com/cloud/#app/Email/C12/Default.aspx?entityType=none&entityID=0%23Tracking")

time.sleep(10)

iframes = driver.find_elements_by_tag_name("iframe")

print(len(iframes))

print(iframes)

driver.switch_to_frame(driver.find_element_by_class_name("mc-app-iframe"))

driver.switch_to_frame(driver.find_element_by_id("fraContent"))

print(driver.find_element_by_xpath('//*[@id="breadcrumbLabel"]').text)

