import re
import csv
import time
import requests
import asyncio
import aiohttp
from random import choice
from datetime import datetime
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


def bs(text, param):
    pass


class Parser:
    def __init__(self):
        self.category_links = []
        self.page_links = []
        self.drink_links = []
        self.csv_rows = []
        self.csv_name = "test.csv"
        self.basic_url = "https://www.myheritage.com/site-1262049512"
        self.ua = UserAgent()
        self.headers = {
                "accept": "*/*",
                "user-agent": self.ua.random
        } 

    def parse_categories(self):
        response = requests.get(url=self.basic_url, headers=self.headers)
        soup = bs(response.text, "lxml")
        nav = soup.find("ul", class_="sidebar")
        li_s = nav.find_all('li', class_="item ng-scope")

        print(li_s)

    def main(self):
        pass

    if __name__ == '__main__':
        main()