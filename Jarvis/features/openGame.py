from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a new browser session
webdriver_service = Service('.\\driver\\chromedriver.exe')
def start():
    driver = webdriver.Chrome(service=webdriver_service)



    # Open the webpage
    driver.get("https://poki.com/en/g/temple-run-2")

    # Find the button by class name

    driver.fullscreen_window()