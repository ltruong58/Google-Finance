from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.page_factory  import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from utils.config import GOOGLE_FINANCE_URL, EXPECTED_TITLE


class GoogleFinancePage:
    # Define locators 
    STOCK_SYMBOLS = (By.XPATH, "//div[contains(text(), 'You may be interested in')]/following-sibling::ul/descendant::div[contains(@class,'COaKTb')]")

    def __init__(self, driver):
        self.driver = driver
        self.url = GOOGLE_FINANCE_URL

        # Skip the following step since it is unnessessary in Selenium 4
        # Initializing elements with Page Factory
        # PageFactory.init_elements(self, driver)

    def load(self):
        """Navigates to Google Finance page"""
        self.driver.get(self.url)

    def verify_page_title(self):
        """Verifies that the page title is correct."""
        print('Page Title: ', self.driver.title)
        assert EXPECTED_TITLE in self.driver.title, "Page title does not match!"

    def get_interesting_stock_symbols(self):
        """Retrieves stock symbols from the 'You may be interested in' section."""
        
        # Wait for the elements to load
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.STOCK_SYMBOLS)
        )
        # Extract text (symbols) from the located elements
        symbols = [element.text for element in elements]
        return symbols