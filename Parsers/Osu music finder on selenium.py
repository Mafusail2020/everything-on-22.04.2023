import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import time

song_name = input("Please enter a song name: ")

options = webdriver.ChromeOptions()

options.add_argument('dom.webdriver.disabled')
options.add_argument('dom.webnotifications.disabled')
options.add_argument('media.volume_off')
options.headless = False

browser = webdriver.Chrome(options=options)
browser.get(url="https://osu.ppy.sh/beatmapsets")

# print(b[0].text.split("\n")[0])
for _ in range(100):
    browser.find_element(by=By.XPATH, value='/html').send_keys(Keys.DOWN)
b = browser.find_elements(by=By.CLASS_NAME, value='beatmapsets__item')
# print(b)

errors = 0
n = 0
while n < len(b):
    try:
        if song_name.lower() in str(b[n].text.split('\n')[0]).lower():
            print(b[n].text.split('\n')[0])
            n += 1
    except selenium.common.StaleElementReferenceException:
        print("Error")
        n -= 1
        errors += 1
print(f"Error count: {errors}")
browser.close()
