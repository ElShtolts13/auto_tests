import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        time.sleep(2)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input3.send_keys("test@mail.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(5)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        time.sleep(2)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        # Это поле отсутствует на странице, что вызовет NoSuchElementException
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
        input3.send_keys("test@mail.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(5)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()