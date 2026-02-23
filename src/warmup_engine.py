import yaml
from video_navigator import VideoNavigator
from search_engine import SearchEngine
from rate_controller import RateController

class WarmupEngine:
    def __init__(self, driver):
        self.driver = driver
        self.navigator = VideoNavigator(driver)
        self.search = SearchEngine(driver)
        self.rate = RateController()

    def load_config(self):
        with open("config/warmup.yaml", "r") as f:
            return yaml.safe_load(f)

    def run(self):
        config = self.load_config()
        max_videos = config["warmup"]["max_videos_per_session"]
        min_watch = config["warmup"]["min_watch_seconds"]
        max_watch = config["warmup"]["max_watch_seconds"]

        for _ in range(max_videos):
            self.navigator.open_home_video()
            self.navigator.watch_video(min_watch, max_watch)
            self.driver.back()
            self.rate.wait()