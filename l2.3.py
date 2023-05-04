

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

    x1 = x_element.text
    x = int(x1)
    y = calc(x)
    y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    y_el.send_keys(y)


    button3 = browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    time.sleep(30)


    # button1 = browser.find_element(By.TAG_NAME, "button")

finally:

    browser.quit()