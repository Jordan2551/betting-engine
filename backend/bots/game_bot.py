import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pprint import pprint
from decouple import config 

class GameBot():
    def __init__(self, url, game_category):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.browser.maximize_window()
        self.browser.get('https://orbitexch.com/customer/inplay/highlights/1')

        self.sign_in(config('ORBITX_USERNAME'), config('ORBITX_PASSWORD'))

        self.get_in_play_sports_table()
  

    def sign_in(self, username, password):
        username_element = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        username_element.click()
        username_element.send_keys(username)
        
        password_element = self.browser.find_element(By.NAME, 'password')
        password_element.click()
        password_element.send_keys(password)

        login_button = self.browser.find_element(By.CLASS_NAME, 'biab_login-submit')
        login_button.click()

        tos_element = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'biab_btn-continue'))
        )

        tos_element.click()


    def get_in_play_sports_table(self):
        bet_element = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'biab_bet-amount'))
        )

        in_play_table_element = self.browser.find_element(By.CLASS_NAME, 'js-markets-list')

        print(in_play_table_element.get_attribute('innerHTML'))



game_bot = GameBot('', '')
