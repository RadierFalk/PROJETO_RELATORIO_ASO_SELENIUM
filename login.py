from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(driver, email, user_esst, senha):
    driver.get('https://esst.com.br/login')
    time.sleep(1)

    email_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[1]/input')
    email_input.clear()
    email_input.send_keys(email)
    email_input.send_keys(Keys.TAB)

    user_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    user_input.clear()
    user_input.send_keys(user_esst)
    user_input.send_keys(Keys.TAB)

    senha_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[3]/input')
    senha_input.clear()
    senha_input.send_keys(senha)
    senha_input.send_keys(Keys.ENTER)