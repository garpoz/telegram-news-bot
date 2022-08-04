#! /usr/bin/python
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
chrome_options.add_argument(f"user-agent={agent}")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
d = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
d.set_window_size(1080, 1080)
d.get("file:///root/telegram-news-bot/index.html")
d.find_element("xpath", "//img[@id='img-id']").screenshot("./output.png")
d.quit()
