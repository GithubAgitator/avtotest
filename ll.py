from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

    x1 = x_element.text
    x = int(x1)

    y = calc(x)
    y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    y_el.send_keys(y)

    button3 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button3.click()

finally:
    time.sleep(30)
    browser.quit()