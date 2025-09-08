from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Service автоматически найдет или скачает нужный chromedriver
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
link = "https://suninjuly.github.io/simple_form_find_task.html"

try:
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    print(button.id)

finally:
    browser.quit()