from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"

try:
    # Открываем страницу
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

# Находим элементы с числами
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

# Получаем текст из элементов и преобразуем в числа
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

# Складываем числа
    total = num1 + num2

# Находим выпадающий список
    dropdown = browser.find_element(By.ID, "dropdown")

# Создаем объект Select для работы со списком
    select = Select(dropdown)

# Выбираем вариант, равный сумме (преобразуем в строку!)
    select.select_by_value(str(total))  # Важно: передаем строку, а не число!

# Находим и нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
finally:
    # Даем время увидеть результат перед закрытием
    time.sleep(10)
    browser.quit()