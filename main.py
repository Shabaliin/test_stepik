from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))
    button = browser.find_element(By.ID, 'solve')
    button.click()
finally:
    browser.quit()
