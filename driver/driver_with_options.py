import pickle
from selenium.webdriver.chrome.webdriver import WebDriver
from driver.options import options

PATH = ''


class DriverWithOptions(WebDriver):
    def __init__(self):
        super().__init__(executable_path=PATH, options=options)
        # self.implicitly_wait(4)

    def save_coo(self):
        with open(r"C:\Users\User\Documents\html\selen\_cookies", "wb") as file:
            pickle.dump(self.get_cookies(), file)

    def load_coo(self):
        with open(r"C:\Users\User\Documents\html\selen\_cookies", "rb") as file:
            for cookie in pickle.load(file):
                self.add_cookie(cookie)
