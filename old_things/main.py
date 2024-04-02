import re
import numpy as np
import pandas as pd
from time import sleep
import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def getdata(url):
    print(url)

def time_convert(start, end):
    start = pd.Timestamp(start)
    end = pd.Timestamp(end)
    time = pd.date_range(start=start, end=end, freq='M')
    time = time.strftime('%Y%m')
    return time

def spider(url):
    pass

if __name__ == '__main__':
    # option = ChromeOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # option.add_experimental_option('useAutomationExtension', False)
    # browser = webdriver.Chrome(options=option)
    # browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    #     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    # })
    #
    #
    base_url = 'https://www.aqistudy.cn/historydata/monthdata.php?city='
    cities = ('北京','上海')
    # url = base_url + cities[0]
    time_setting = ('20200101', '20231231')
    time = time_convert(time_setting[0], time_setting[1])
    for city in cities:
        new_url = base_url + city
        time_range = time_convert(time_setting[0], time_setting[1])
    print(time)
    # browser.get(url)