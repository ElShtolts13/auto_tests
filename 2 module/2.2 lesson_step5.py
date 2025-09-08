from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#тест с ошибкой, вызванной тем, что мы пытаемся обратиться к элементу (кнопке), который прекрыт другим объектом. Но на 8 строчке мы добавили скролл странички с помощью внедрения js-кода и все стало по кайфу