from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class SessionManager:
    def __init__(self):
        self.driver = None

    def start(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.youtube.com")
        print("Please log in manually if required.")
        time.sleep(20)