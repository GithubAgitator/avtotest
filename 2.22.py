from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

from work import element

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    op1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    op1.send_keys("Мой ответ")
    op2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    op2.send_keys("Мой ответ")
    op3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    op3.send_keys("Мой ответ")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    fil_name = "t.txt"
    file_path = os.path.join(current_dir, fil_name)
    el = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
    el.send_keys(file_path)
    button = browser.find_element(By.XPATH, "//div//button[@type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
