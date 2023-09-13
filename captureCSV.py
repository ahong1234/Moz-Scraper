import time

import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def captureCSV_(choice):
    print("Fetching Keyword Report CSV from Moz....")
    driver = uc.Chrome()
    driver.set_window_size(400, 500)
    driver.get("http://www.moz.com/login")
    print("Logging in...")
    driver.find_element(By.NAME, "email").send_keys("gdstest54@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("GDS2022!")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(2)
    print("Navigating menus...")
    driver.get("https://analytics.moz.com")
    time.sleep(2)
    if choice == 1:
        driver.find_element(By.LINK_TEXT, 'globaldentalshop').click()
    elif choice == 2:
        driver.find_element(By.LINK_TEXT, 'Campaigns').click()
        time.sleep(3.5)
        driver.find_element(By.LINK_TEXT, 'vitality-product').click()
    time.sleep(4.75)
    print("Accessing keyword rankings...")
    driver.find_element(By.LINK_TEXT, 'Rankings').click()
    time.sleep(4.75)
    driver.execute_script("window.scrollTo(350,document.body.scrollHeight)")
    time.sleep(4.75)
    print("Downloading CSV...")
    elem = driver.find_element(By.XPATH, '//*[contains(text(), "CSV")]')
    elem.click()
    time.sleep(10)
    print("Keyword Report CSV Download Complete.\n")
    driver.quit()
