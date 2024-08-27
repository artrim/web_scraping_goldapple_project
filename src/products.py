from selenium import webdriver


class Products:
    url_gold_apple = 'https://goldapple.ru/parfjumerija'
    driver = webdriver.Chrome()

    def __init__(self, name, rating, price, url, description=None, instruction=None, country=None):
        self.name = name
        self.rating = rating
        self.price = price
        self.url = url
        self.description = description
        self.instruction = instruction
        self.country = country
