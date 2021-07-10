from time import sleep
from ebay_parser import Parser
from driver.driver import Driver
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def main():
    # url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=sonu&_sacat=0&LH_TitleDesc=0&_sop=13'
    url = 'https://google.com'

    # parser = Parser()
    # # parser.parse(url)
    # parser.parse_many(url, 2)
    dr = Driver()
    dr.get(url)
    sleep(10)
    # con = presence_of_element_located(dr.find_elements_by_class_name('lnXdpd'))
    # con.locator[0].click()
    pass


if __name__ == '__main__':
    main()
