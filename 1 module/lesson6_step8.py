from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/registration2.html"



try:
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)

    browser.get(link)
    time.sleep(2)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
    input3.send_keys("test@mail.ru")


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(30)
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла