# from selenium import webdriver
# from selenium.webdriver.common.by import By

# import math
# from selenium.webdriver.support.ui import Select
#
#
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     def summa(a, b):
#         return a + b
#
#     a_el = browser.find_element(By.CSS_SELECTOR, "[id = 'num1']")
#     b_el = browser.find_element(By.CSS_SELECTOR, "[id = 'num2'")
#     a1 = a_el.text
#     b1 = b_el.text
#     a = int(a1)
#     b = int(b1)
#     y = summa(a, b)
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(str(y))
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


#**********************

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
#*************************

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")

    x1 = x_element.text
    x = int(x1)
    y = calc(x)

    y_el = browser.find_element(By.CSS_SELECTOR, "[id = 'answer']")

    y_el.send_keys(y)

    op1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", op1)
    op1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")

    option2.click()
    button = browser.find_element(By.XPATH, "//div//button[@type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()








