from selenium import webdriver
from seleniumbase import Driver

class Browser:
    driver=Driver()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)

    def close(self):
        self.driver.quit()
