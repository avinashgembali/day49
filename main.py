from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
URL = (f"https://www.linkedin.com/jobs/search/?currentJobId=3980180947&f_AL=true&f_WT=2&keywords=python%20developer&orig"
       f"in=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(5)
username = driver.find_element(By.ID, value="username")
username.send_keys("YOUR MAIL")
password = driver.find_element(By.ID, value="password")
password.send_keys("YOUR PASSWORD")
password.send_keys(Keys.ENTER)

time.sleep(5)
easy_apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
easy_apply.click()

time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys("9928393241")

next_button = driver.find_element(By.CSS_SELECTOR, value=".artdeco-button")
next_button.click()

discard_button = driver.find_element(By.ID, value="ember369")
discard_button.click()
# I AM DISCARDING IT BECAUSE IT WAS JUST FOR TRIAL

