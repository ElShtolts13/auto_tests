from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from faker import Faker
import time
fake = Faker()
word = fake.word()
link = "http://suninjuly.github.io/huge_form.html"



try:
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    link = browser.find_elements(By.TAG_NAME, "input")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
# закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла