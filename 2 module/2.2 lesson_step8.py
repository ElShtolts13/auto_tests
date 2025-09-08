from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "2.2.8.txt"
file_path = os.path.join(current_dir, file_name)

try:
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    browser.get(link)
    time.sleep(2)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name = firstname]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name = lastname]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name = email]")
    input3.send_keys("test@mail.ru")

    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)



finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла