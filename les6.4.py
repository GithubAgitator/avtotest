import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
    input1.send_keys("Мой ответ")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input2.send_keys("Мой ответ")
    input3 = browser.find_element(By.CLASS_NAME, "second_block")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input4.send_keys("Мой ответ")
    button = browser.find_element(By.XPATH, "//div//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
