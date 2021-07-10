import os
from time import sleep

import pandas as pd
from driver.driver import Driver
from selenium.common.exceptions import TimeoutException


class Parser():
    _driver = Driver()

    def __init__(self) -> None:
        pass

    def parse_many(self, url, pages):
        for i in range(pages):
            self.parse(f"{url}&_pgn={i+1}")
        sleep(2)
        self._driver.quit()

    def parse(self, url):
        driver = self._driver
        driver.get(url)
        data = self.get_data()
        self.output(data)
        sleep(2)

    def get_data(self):
        driver = self._driver
        el = 'ul.srp-results li.s-item'

        el_list = driver.find_elements_by_css_selector(el)
        if len(el_list) == 0:
            try:
                driver.wait_el_css_selector(el, 200)
                sleep(3)
                self.get_data()
            except TimeoutException:
                print("Timeout and The element Not find")
                driver.quit()
        else:
            return self.set_prod_list(el_list)

    def set_prod_list(self, el_list):
        prod_list = []
        for el in el_list:
            prod = {
                'title': el.find_element_by_css_selector('h3.s-item__title').text,
                'price': el.find_element_by_css_selector('span.s-item__price').text
            }
            prod_list.append(prod)
        return prod_list

    def output(self, data):
        df = pd.DataFrame(data)

        if os.path.exists('output.csv'):
            df.to_csv('output.csv', mode='a',
                      header=False, index=False)
        else:
            df.to_csv('output.csv', index=False)

        print('Saved to CSV')
