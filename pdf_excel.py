import time
import pyautogui as pa
from selenium.webdriver.common.by import By

def converter_pdf_para_excel(driver):
    
    driver.get('https://www.ilovepdf.com/pt/pdf_para_excel')
    pa.click(x=1553, y=587)
    time.sleep(0.5)
    pa.click(x=1391, y=575)
    time.sleep(3)

    attach_button = driver.find_element(By.XPATH, '//*[@id="pickfiles"]')
    attach_button.click()
    time.sleep(1)

    pa.click(x=103, y=296)
    time.sleep(2)
    pa.click(x=349, y=232)
    pa.press('ENTER')
    time.sleep(2)

    convert_button = driver.find_element(By.XPATH, '//*[@id="processTask"]')
    convert_button.click()
    time.sleep(3)

    download_excel_button = driver.find_element(By.XPATH, '//*[@id="pickfiles"]')
    download_excel_button.click()
    time.sleep(5)