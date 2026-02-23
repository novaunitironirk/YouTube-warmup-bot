from selenium.webdriver.common.by import By
import time
import random

class VideoNavigator:
    def __init__(self, driver):
        self.driver = driver

    def open_home_video(self):
        videos = self.driver.find_elements(By.ID, "video-title")
        if videos:
            random.choice(videos).click()
            time.sleep(5)

    def watch_video(self, min_seconds, max_seconds):
        watch_time = random.randint(min_seconds, max_seconds)
        time.sleep(watch_time)