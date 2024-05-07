import os
import csv
import time
import random
import requests
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ../data_formatting/data_file_creation.py import *


class OnePieceCrawler:
    name = 'one_piece'

    def crawl(self):
        URL = 'https://www.tcgplayer.com/search/one-piece-card-game/product?productLineName=one-piece-card-game&page=1&view=grid'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
        driver.get(URL)
        # driver.implicitly_wait(4)
        time.sleep(4)

        page = 1
        card_items = []
        while True:
            product_frames = driver.find_elements(By.CLASS_NAME, 'search-result__product')
            print(product_frames)
            for frame in product_frames:
                # Card link
                link = frame.find_element(By.TAG_NAME, 'a').get_attribute('href')
                print(link)
                # Card image
                image = frame.find_element(By.TAG_NAME, 'img').get_attribute('src')
                print(image)
                # Card Info
                product_container = frame.find_element(By.CLASS_NAME, 'product-card__product')
                category = product_container.find_element(By.CLASS_NAME, 'product-card__category-name').text
                card_set = product_container.find_element(By.CLASS_NAME, 'product-card__subtitle').text
                rarity = product_container.find_element(By.CLASS_NAME, 'product-card__rarity').text
                title = product_container.find_element(By.CLASS_NAME, 'product-card__title.truncate').text
                # Pricing
                market_price = product_container.find_element(By.CLASS_NAME, 'product-card__market-price--value').text
                # Aggregate data
                item = [category, card_set, rarity, title, market_price]
                card_items.append(item)

                print(item)
                print('----------')
                time.sleep(random.randint(1,2))


            print('paginate')
            next_page = page + 1
            wait = WebDriverWait(driver, timeout=2)
            # Pagination
            try:
                next_page_url = f'https://www.tcgplayer.com/search/one-piece-card-game/product?productLineName=one-piece-card-game&page={next_page}&view=grid'
                driver.get(next_page_url)
                driver.implicitly_wait(5)
            except NoSuchElementException:
                print('No more pages available')
                break

        return card_items

    # def store_to_csv(self):
    #     # Create file name
    #     tz = timezone('America/Toronto')
    #     current_date = datetime.now(tz).strftime('%Y%m%d_%H%M%S')
    #     name = 'one_piece'
    #     file_name = f'{current_date}_{name}'
    #     print(file_name)

    #     # Create a csv file to store the data
    #     with open(f'../dataset/{file_name}', 'w') as file:
    #         reader = csv.reader(file)
    #         next(reader)
    #         pass




if __name__ == '__main__':
    opc = OnePieceCrawler()
    data = opc.crawl()
    store_to_csv(opc.name, data)
