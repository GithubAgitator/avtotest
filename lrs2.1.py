from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math




try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//div//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
    y_el.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    button = browser.find_element(By.XPATH, "//div//button[@type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
#
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     el = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
#     x_element = el.get_attribute("valuex")
#     # x = x_element.text
#     y = calc(x_element)
#     y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")
#     y_el.send_keys(y)
#     option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#     option1.click()
#     option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
#     option2.click()
#     button = browser.find_element(By.XPATH, "//div//button[@type='submit']")
#     button.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла