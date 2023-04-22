import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver

headers2 = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

request = requests.get('https://www.guru99.com/chrome-options-desiredcapabilities.html', headers=headers2, allow_redirects=True)

print()
with open('site_code.txt', 'r') as f:
    with open('saf.txt', 'r') as f2:
        if f.read() == f2.read():
            print(True)
        else:
            print(False)
