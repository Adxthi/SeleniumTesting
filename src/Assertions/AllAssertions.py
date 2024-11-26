import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAssertions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        service = Service("/usr/bin/chromedriver")  # Update this to your ChromeDriver path
        options = Options()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get("https://demoqa.com/checkbox")
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_assertions(self):
        # Test for assertEqual and assertNotEqual
        title = self.driver.title
        self.assertEqual(title, "DEMOQA", "Title does not match expected value")
        self.assertNotEqual(title, "WrongTitle", "Title unexpectedly matches 'WrongTitle'")

        # Test for assertTrue and assertFalse
        checkbox_label = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='tree-node-home']")))
        self.assertTrue(checkbox_label.is_displayed(), "Checkbox label should be displayed")
        self.assertFalse(checkbox_label.is_selected(), "Checkbox label should not be selected before clicking")

        # Test for assertIsNotNone and assertIsNone
        self.assertIsNotNone(checkbox_label, "Checkbox label should not be None")
        # Try finding a non-existent element to test assertIsNone
        non_existent_element = self.driver.find_elements(By.ID, "nonExistent")
        self.assertIsNone(non_existent_element[0] if non_existent_element else None, "Element should be None as it doesn't exist")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
