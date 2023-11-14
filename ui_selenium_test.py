import unittest
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlaskSeleniumTest(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        self.service = ChromeService()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def test_header(self):
        self.driver.get("http://localhost:8001")
        try:
            # Wait for the text to be present in the element
            element = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Go')
            )
            # Assertion to check if the text is found
            assert element, "Go"
            print(f"Text Go found!")
        except AssertionError as e:
            print(e)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
