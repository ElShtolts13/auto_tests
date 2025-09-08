from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math
# Функция для вычисления значения

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    # Открываем страницу
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    time.sleep(2)

# Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text # Получаем текст элемента
    y = calc(x)  # Вычисляем значение функции
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule_radio)
    robots_rule_radio.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    # Даем время увидеть результат перед закрытием
    time.sleep(10)
    browser.quit()