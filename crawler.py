from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# crawler class


class Crawler:
    # initialize the crawler
    def __init__(self):
        self.service = ChromeService(ChromeDriverManager().install())
        # open chrome in headless mode
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=self.service, options=options)
        
    # close the driver
    def __del__(self):
        self.driver.close()
        
    def load_page(self, url):
        self.driver.get(url)
        return

    # get the page source
    def get_page_source(self):
        return self.driver.page_source

    # load all table data
    def load_table_data(self):
        # button to select all data
        all_semester_button = self.driver.find_element(
            by=By.ID, value="RadioList_Termin3")
        all_semester_button.click()
        # button to start loading selected data
        search_button = self.driver.find_element(
            by=By.XPATH, value="//*[@id='aspnetForm']/table/tbody/tr[2]/td[3]/a")
        search_button.click()

        # wait for the loading spinner to show up
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(by=By.ID, value="gridViewPlanyGrup_LPV"))
        # wait for the loading spinner to disappear
        WebDriverWait(self.driver, 10).until_not(
            lambda driver: driver.find_element(by=By.ID, value="gridViewPlanyGrup_LPV"))

        # data is now loaded
        return
