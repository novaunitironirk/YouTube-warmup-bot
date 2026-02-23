from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchEngine:
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)