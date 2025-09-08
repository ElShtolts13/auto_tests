from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(2)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button2.click()





finally:
    print(browser.switch_to.alert.text)

    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()

