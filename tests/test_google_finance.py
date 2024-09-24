from selenium import webdriver
# from selenium.webdriver.support.page_factory  import PageFactory
from pages.google_finance_page import GoogleFinancePage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.config import GIVEN_SYMBOLS
import argparse

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

    def test_verify_stock_symbols_full(self):
        """Full test cases to verify stock symbols on the Google Finance page."""
        # Step 1: Open Google Finance webpage
        self.page.load()
        
        # Step 2: Verify the page title
        self.page.verify_page_title()
        
        # Step 3: Retrieve stock symbols
        retrieved_symbols = self.page.get_interesting_stock_symbols()
        # print("Given Symbols:", GIVEN_SYMBOLS)
        print("Retrieved Symbols:", retrieved_symbols)

        # Step 4: Compare retrieved symbols with the expected data
        # In case of multiple 'INDEX' symbols, the list will be converted to set to remove duplicates
        # Compare the 2 lists to see if they are the same or not (ignoring order)
        # TODO: consider the case the retrieved or given list is empty/ or both

        are_equal = sorted(list(set(retrieved_symbols))) == sorted(GIVEN_SYMBOLS)
        if (are_equal):
            print("The given list and the retried list are the identical")
        else:
            print("The given list and the retried list are not the identical")

        # for symbol in EXPECTED_SYMBOLS:
        #     assert symbol in retrieved_symbols, f"Symbol {symbol} not found in retrieved symbols!"

        # Step 5:
        print("All stock symbols that are in (3) but not in given test data", list(set(retrieved_symbols) - set(GIVEN_SYMBOLS)))
        
        # Step 6:
        print("All stock symbols that are in given test data but not in (3)", list(set(GIVEN_SYMBOLS) - set(retrieved_symbols)))

    def test_verify_stock_symbols_case_5_6(self):
        """Test cases 5 and 6 to verify stock symbols on the Google Finance page"""
        # Step 1: Open Google Finance webpage
        self.page.load()
        
        # Step 3: Retrieve stock symbols
        retrieved_symbols = self.page.get_interesting_stock_symbols()

        # Step 5:
        print("All stock symbols that are in (3) but not in given test data", list(set(retrieved_symbols) - set(GIVEN_SYMBOLS)))
        
        # Step 6:
        print("All stock symbols that are in given test data but not in (3)", list(set(GIVEN_SYMBOLS) - set(retrieved_symbols)))


# Run the test
if __name__ == "__main__":

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Select which test suite to run.")
    
    # Add an argument to select the test suite
    parser.add_argument(
        '--test-suite', 
        choices=['full', 'test_5_6'], 
        default='full',
        help='Select which tests to run: full (default) or test_5_6'
    )
    
    # Parse the command-line arguments
    args = parser.parse_args()

    test_suite = TestGoogleFinance()
    test_suite.setup_method()
    try:
        # Determine which test suite to run based on the argument
        if args.test_suite == 'full':
            test_suite.test_verify_stock_symbols_full()
        elif args.test_suite == 'test_5_6':
            test_suite.test_verify_stock_symbols_case_5_6()

    finally:
        test_suite.teardown_method()