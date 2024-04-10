from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LOGIN_MAIL = "YOUR_EMAIL_HERE"
LOGIN_PW = "YOUR_PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://www.linkedin.com/")

time.sleep(5)

# login button
div_element = driver.find_element(By.CLASS_NAME, 'nav__cta-container')
link_element = div_element.find_element(By.CLASS_NAME, 'nav__button-secondary')
# time.sleep(10)
link_element.click()

login_mail = driver.find_element(By.ID, "username")
login_mail.send_keys(f"{LOGIN_MAIL}")
login_pw = driver.find_element(By.ID, "password")
login_pw.send_keys(f"{LOGIN_PW}")
# time.sleep(5)

# actual login
div_log_element = driver.find_element(By.CLASS_NAME,"login__form_action_container")
login_btn = div_log_element.find_element(By.TAG_NAME, "button")
login_btn.click()

