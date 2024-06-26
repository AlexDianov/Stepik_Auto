from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 13). until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID,'book')
    button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    answer1 = browser.find_element(By.ID, "answer")
    y = calc(x)
    print(y)
    answer1.send_keys(y)
    submit = browser.find_element(By.ID,'solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()


