from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)


    (WebDriverWait(browser, "12").until
     (EC.text_to_be_present_in_element((By.ID, "price"), "100"))
     )

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    time.sleep(2)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    browser.find_element(By.CSS_SELECTOR,"#solve").click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


finally:

    browser.quit()

