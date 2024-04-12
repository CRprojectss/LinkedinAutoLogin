from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

LOGIN_MAIL = "c.rath@live.com"
LOGIN_PW = "4yU43NR5"
SEARCH_INPUT = "Python Developer"  # Type your Job Keywords between the ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://www.linkedin.com/")

time.sleep(3)  # wait 3 secs to load the entire page

# login button
div_element = driver.find_element(By.CLASS_NAME, 'nav__cta-container')
link_element = div_element.find_element(By.CLASS_NAME, 'nav__button-secondary')
link_element.click()

login_mail = driver.find_element(By.ID, "username")
login_mail.send_keys(f"{LOGIN_MAIL}")
login_pw = driver.find_element(By.ID, "password")
login_pw.send_keys(f"{LOGIN_PW}")


# actual login
div_log_element = driver.find_element(By.CLASS_NAME,"login__form_action_container")
login_btn = div_log_element.find_element(By.TAG_NAME, "button")
login_btn.click()
time.sleep(2)

# 1. click jobs
job_element = driver.find_element(By.XPATH,"//a[@href='https://www.linkedin.com/jobs/?']")
job_element.click()
time.sleep(2)

# 2. input keywords for jobs to search for
job_search_bar = driver.find_element(By.TAG_NAME, "input")
job_search_bar.send_keys(f"{SEARCH_INPUT}",Keys.ENTER)
time.sleep(2)

# dropdown select company type
company_type_filer_dropdown = driver.find_element(By.ID, "searchFilter_workplaceType")
company_type_filer_dropdown.click()
time.sleep(3)
remote_filter = driver.find_element(By.ID, 'workplaceType-2')
driver.execute_script("arguments[0].click();", remote_filter)
remote_filter.send_keys(Keys.ESCAPE)

# apply the "apply easy" filter
easy_apply_btn = driver.find_element(By.XPATH, '//button[text()="Easy Apply"]')
easy_apply_btn.click()


