import time
import pyautogui as pa
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Componente responsável por acessar o centro de custo e o periodo solicitado

def acessar_centro_custo(driver, cc, dt_inicial, dt_final):
    driver.get('https://esst.com.br/eSST/asosgerenciados')
    time.sleep(1)

    cc_input = driver.find_element(By.XPATH, '//*[@id="select2-fltr_local-container"]')
    cc_input.click()
    time.sleep(1)
    pa.write(cc)
    time.sleep(1)
    pa.press('ENTER')
    time.sleep(1)

    per_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div/div[1]/span[4]/div/button[1]')
    per_input.click()
    time.sleep(0.5)
    per_input = driver.find_element(By.XPATH, '//*[@id="op_rel6"]')
    per_input.click()
    time.sleep(0.5)

    date_input = driver.find_element(By.XPATH, '//*[@id="rel_dtInicial6"]')
    date_input.send_keys(dt_inicial)
    date_input.send_keys(Keys.TAB)

    date_input_final = driver.find_element(By.XPATH, '//*[@id="rel_dtFinal6"]')
    date_input_final.clear()
    date_input_final.send_keys(dt_final)
    time.sleep(2)

    download_button = driver.find_element(By.XPATH, '//*[@id="relOK_rel6"]')
    download_button.click()
    time.sleep(4)
    pa.click(x=1791, y=215)
    time.sleep(2)
    pa.press('ENTER')
    time.sleep(2)
    pa.hotkey('ctrl', 'w')