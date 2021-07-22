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

from bs4 import BeautifulSoup

class GameBot():
    def __init__(self, url, game_category):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.browser.maximize_window()
        self.browser.get('https://orbitexch.com/customer/inplay/2/1')

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

        # in bs look for <span>In-Play</span>
        # Not suspended? or is that accounted for already



        soup = BeautifulSoup(in_play_table_element.get_attribute('innerHTML'))

        # Find the big table of In-Play
        soup = soup.find('div', {'class': 'js-inplay-sport-region biab_inplay-sport-competitions-list'})
        
        # Each table body corresponds to an in-play game
        in_play_table_bodies = soup.findAll('tbody')

        import pdb
        pdb.set_trace()
        # Extract the needed information from each individual table body (score for home away, odds, etc)
        # TODO:: NOTE THAT THIS IS TENNIS SPECIFIC
        for in_play_table_body in in_play_table_bodies:
            # If there is a <tbody> as the first element in a table then it holds the scores 
            game_and_set_scores = in_play_table_body.find('tbody')

            if game_and_set_scores:
                game_and_set_scores = game_and_set_scores.findall('td')
                home_sets = game_and_set_scores[0].text
                home_games = game_and_set_scores[1].text
                away_sets = game_and_set_scores[2].text
                away_games = game_and_set_scores[3].text


            # Get the rest of the info (odds, arbitrage, etc)

                # home_tennis_games_sets = (home_tennis_games_sets)

            # if in_play_table_body.findAll('tr', {'class': 'biab_tennis-sets biab_home-tennis-sets'})
            # home_tennis_games_sets = in_play_table_body
            # print(in_play_table_body.prettify())




game_bot = GameBot('', '')
