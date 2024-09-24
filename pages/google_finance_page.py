from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.page_factory  import PageFactory
from selenium.webdriver.support import expected_conditions as EC
from utils.config import GOOGLE_FINANCE_URL

class GoogleFinancePage:
    # Define locators 
    STOCK_SYMBOLA = (By.XPATH, "//div[contains(text(), 'You may be interested in')]/following-sibling::ul/descendant::div[contains(@class,'COaKTb')]")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"

        # Skip the following steps since it is unnessessary in Selenium 4
        # Initializing elements with Page Factory
        # PageFactory.init_elements(self, driver)

    def load(self):
        self.driver.get(self.url)

    def verify_page_title(self):
        """Verifies that the page title is correct."""
        print(self.driver.title)
        assert "Google Finance" in self.driver.title, "Page title does not match!"

    def get_interesting_stock_symbols(self):
        """Retrieves stock symbols from the 'You may be interested in' section."""
        # Locator for the section containing stock symbols (adjust this based on actual page layout)
        # stock_symbols_locator = (By.XPATH, "//div[contains(text(), 'You may be interested in')]/following-sibling::ul/descendant::div[contains(@class,'COaKTb')]")
        # Wait for the elements to load
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.STOCK_SYMBOLA)
        )
        # Extract text (symbols) from the located elements
        symbols = [element.text for element in elements]
        return symbols