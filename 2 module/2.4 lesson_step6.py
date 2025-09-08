from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"

try:
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    browser.get(link)

    browser.implicitly_wait(5)

    browser.find_element(By.ID, "button")

finally:
    browser.quit()




