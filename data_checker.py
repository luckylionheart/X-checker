import re

import requests
from bs4 import BeautifulSoup
from dateutil import parser
import time
import random

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_event_name_and_date(url):
    if 'axs.' in url:
        return check_axs(url)


def open_driver(self, 
                    use_proxy=False,
                    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36.',
                    headless=False):
        random_proxy = random.choice(self.proxies)
        auth, ip_port = random_proxy.split('@')
        user, pwd = auth.split(':')
        ip, port = ip_port.split(':')
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                  singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                  },
                  bypassList: ["localhost"]
                }
              };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (ip, port, user, pwd)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if headless:
            pass
            # chrome_options.add_argument('--headless')

        if use_proxy:
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            chrome_options.add_extension(pluginfile)
            time.sleep(1)
        if user_agent:
            chrome_options.add_argument('--user-agent=%s' % user_agent)
        try:
            driver = webdriver.Chrome(
                'chromedriver', chrome_options=chrome_options)
        except Exception as E:
            return self.open_driver()

        # Check if it's working
        driver.get('https://www.google.com/')
        try:
            driver.find_element_by_id("L2AGLb").click()
            time.sleep(0.5)
        except:
            pass

        try:
            driver.find_element_by_css_selector('input[name="q"]')
        except:
            driver.quit()
            return self.open_driver()
        return driver

def make_request(url):
    headers = {
        # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36.',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0.'
    }
    r = requests.get(url, headers=headers)
    if r.status_code == 200 or r.status_code == 506:
        return BeautifulSoup(r.content, 'html.parser')
    print(r.status_code, url)


def check_axs(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_class_name('btn--single btn btn-default').click()
    time.sleep(3000)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return name, date

# for url in ['https://basscanyonfestival.frontgatetickets.com/event/i8co6kruzz405we8',
#             'https://www.ticketfly.com/purchase/event/1803134/tfly',
#             'https://www.eventbrite.com/e/casablanca-the-montalban-rooftop-movies-tickets-54783106747?aff=erelexpmlt#tickets',
#             'https://www.etix.com/ticket/p/3379234/hartmut-sauers-musikkabinettduosassoninocturne-wandel-durch-die-nacht-dresdensch%C3%B6nfeld-deutschlands-zauberschloss?partner_id=430',
#             'https://www.ticketweb.com/event/lords-of-acid-with-special-brick-by-brick-tickets/9072935?REFERRAL_ID=twflash']:
#     print('for url', url)
#     print(get_event_name_and_date(url))
