from selenium import webdriver
# from selenium.webdriver.support.page_factory  import PageFactory
from pages.google_finance_page import GoogleFinancePage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.config import EXPECTED_SYMBOLS
import time

# Test data
# EXPECTED_SYMBOLS = ["NFLX", "MSFT", "TSLA"]

class TestGoogleFinance:
    """Test Suite for Google Finance"""

    def setup_method(self):
        """Setup method to initialize the Chrome driver."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.page = GoogleFinancePage(self.driver)

    def teardown_method(self):
        """Teardown method to close the browser after tests."""
        self.driver.quit()

    def test_verify_stock_symbols(self):
        """Test case to verify stock symbols on the Google Finance page."""
        # Step 1: Open Google Finance webpage
        self.page.load()
        
        # Step 2: Verify the page title
        self.page.verify_page_title()
        
        # Step 3: Retrieve stock symbols
        retrieved_symbols = self.page.get_interesting_stock_symbols()
        print("Retrieved Symbols:", retrieved_symbols)

        # Step 4: Compare retrieved symbols with the expected data
        # for symbol in EXPECTED_SYMBOLS:
        #     assert symbol in retrieved_symbols, f"Symbol {symbol} not found in retrieved symbols!"

        # Step 5:
        print("Cur - given", list(set(retrieved_symbols) - set(EXPECTED_SYMBOLS)))
        
        # Step 6:
        print("Given - Cur", list(set(EXPECTED_SYMBOLS) - set(retrieved_symbols)))


# Run the test
if __name__ == "__main__":
    test_suite = TestGoogleFinance()
    test_suite.setup_method()
    try:
        test_suite.test_verify_stock_symbols()
     
    finally:
        test_suite.teardown_method()