import requests
from bs4 import BeautifulSoup

url = "https://humanbenchmark.com/tests/typing"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information from the HTML using BeautifulSoup methods
    # Example: Get the title of the website
    title = soup.title.text
    print("Title:", title)

    # Example: Get all the links on the page
    links = soup.find_all('a')
    print("Links:")
    for link in links:
        print(link['href'])

    # You can explore and extract more information based on the HTML structure

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
