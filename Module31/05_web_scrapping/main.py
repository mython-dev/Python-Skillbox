# TODO здесь писать код
import requests
from bs4 import BeautifulSoup

url = 'http://www.columbia.edu/~fdc/sample.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

contents = soup.find_all('h3')

for content in contents:
    result = [content.text]
    print(result)
