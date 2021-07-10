from driver.listener import Listener
from driver.driver_with_options import DriverWithOptions
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By as by
import pickle  # for Coocies
from time import sleep


class Driver(EventFiringWebDriver):
    def __init__(self, driver=DriverWithOptions(), event_listener=Listener()):
        super().__init__(driver, event_listener)

    def quit_time(self, s: float):
        sleep(s)
        self.quit()

    def wait_el(self, value, sec, by=by.ID):
        WebDriverWait(self, sec).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_el_class_name(self, value, sec):
        self.wait_el(value, sec, by.CLASS_NAME)

    def wait_el_css_selector(self, value, sec):
        self.wait_el(value, sec, by.CSS_SELECTOR)
