import os
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def scrap(coin: str = 'eth', count_wallets: int = 1):
    if platform.system() == 'Windows':
        disable_connect = 'ipconfig/release'
        enable_connect = 'ipconfig/renew'
    elif platform.system() == 'Linux':
        disable_connect = 'nmcli networking off'
        enable_connect = 'nmcli networking on'
    
    opts = webdriver.ChromeOptions()
    opts.add_argument('--incognito')
    
    with webdriver.Chrome(options=opts) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get(f"https://cointool.app/createWallet/{coin}")
        driver.find_element(By.CLASS_NAME, 'input').send_keys(count_wallets)
        
        os.system(disable_connect)
        
        driver.find_element(By.CLASS_NAME, 'el-icon-right').click()
        wait.until(presence_of_element_located((By.CSS_SELECTOR, '.inputBox')))
        value_field = driver.find_elements(By.CSS_SELECTOR, '.inputBox input.el-input__inner')
        name_field = driver.find_elements(By.CSS_SELECTOR, '.inputBox .el-input-group__prepend')
        res = []
        for i in range(count_wallets):
            res.append({i.get_property('textContent').strip(): j.get_property('value') for i, j in zip(name_field, value_field)})
        
        os.system(enable_connect)
        
        driver.close()
    
    return res