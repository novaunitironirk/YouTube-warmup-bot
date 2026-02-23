import random
import time
import yaml

class RateController:
    def __init__(self):
        with open("config/pacing.yaml", "r") as f:
            pacing = yaml.safe_load(f)["pacing"]
        self.min_delay = pacing["min_delay_seconds"]
        self.max_delay = pacing["max_delay_seconds"]

    def wait(self):
        time.sleep(random.randint(self.min_delay, self.max_delay))