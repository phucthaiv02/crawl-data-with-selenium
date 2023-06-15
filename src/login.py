from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

import json

# define browser
browser = webdriver.Chrome()

# Open website
browser.get("https://app.software.com/login")

# Load username and password from account.json
with open("json/account.json") as f:
    data = json.load(f)
username = data["username"]
password = data["password"]

# Login
textUser = browser.find_element(By.ID, 'email')
textUser.send_keys(username)
textPassword = browser.find_element(By.ID, 'password')
textPassword.send_keys(password)
textPassword.send_keys(Keys.ENTER)

sleep(10)
browser.quit()