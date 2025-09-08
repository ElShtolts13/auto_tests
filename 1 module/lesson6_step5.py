from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import  time

link = "http://suninjuly.github.io/find_link_text"
linkText = str(math.ceil(math.pow(math.pi, math.e)*10000))
#realLink = 'http://suninjuly.github.io/find_link_text_redirect13.html'
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

try:
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, linkText)
    link.click()

    time.sleep(2)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


# не забываем оставить пустую строку в конце файла