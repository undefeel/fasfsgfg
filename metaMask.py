from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import logging


def add_wallet(data=None, exstention_path: str = '10.25.0_0.crx', id: str = 'nkbihfbeogaeaoehlefnkodbefgpgknn'):
    opts = webdriver.ChromeOptions()
    opts.add_extension(exstention_path)
    opts.add_argument(r'--user-data-dir=/home/kodokuus/.config/chromium/Profile 2')
    opts.add_argument(r'--profile-directory=/home/kodokuus/.config/chromium/Profile 2')
    # 110.0.5481.100 (Official Build) Arch Linux (64-bit) 
    # 110.0.5481.100 (Official Build) (64-bit) 
    serv = Service(r'/usr/lib/chromium/chromium',port=8000)
    # ['--verbose', '--log-path=/home/kodokuus/Code/python/Tests/MnemonicExport/loggg.log', '--port=9500']
    with webdriver.Chrome(options=opts, service=serv) as driver:
        wait = WebDriverWait(driver, 1000)
        driver.get(f'chrome-extension://{id}/home.html#initialize/create-password')
        driver.switch_to.window(driver.window_handles[1])
        print(driver.window_handles)
        wait.until(presence_of_element_located((By.CLASS_NAME, 'onboarding-app-header__contents')))
        # wait.until(presence_of_element_located((By.CLASS_NAME, '____onboarding-app-header__contents')))
        driver.find_element(By.CSS_SELECTOR, '.onboarding-welcome .btn-secondary').click()
        driver.find_element(By.CSS_SELECTOR, '.onboarding-metametrics__buttons .btn-secondary').click()
        inputs = driver.find_elements(By.ID, 'import-srp__srp-word-0')
        
        # for input in inputs:
        #     input.send_keys()
        wait.until(presence_of_element_located((By.CLASS_NAME, '____onboarding-app-header__contents')))
        

add_wallet()
# button btn--rounded 