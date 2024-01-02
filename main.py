from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui


url = "https://humanbenchmark.com/tests/typing"
browser = webdriver.Chrome()

browser.get(url)
time.sleep(5)
browser.implicitly_wait(10)
# Open Chrome in debug mode
source = browser.page_source

# Now, use BeautifulSoup to extract information from the website
soup = BeautifulSoup(source, 'html.parser')

# Find all <span> elements within the 'letters notranslate' class
spans = soup.find_all('span', class_='incomplete')
text = ''.join([span.get_text() for span in spans])

pyautogui.write(text,interval=0)
time.sleep(10000)

