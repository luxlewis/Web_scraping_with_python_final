from bs4 import BeautifulSoup

import requests
import pandas as pd

url = "https://www.programmableweb.com/category/tools/api"
api_no = 0

while True:

    response = requests.get(url)
    print(response)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    results = soup.find_all('tr', {'class': ['odd', 'even']})
    print(results)

    for result in results:
        description_tag = result.find('td', {'class': 'views-field views-field-field-api-description'})
        description = description_tag.text if description_tag else "N/A"
        name = result.find('td', {'class': "views-field-title"}).text
        category = result.find('td', {'class': 'views-field views-field-field-article-primary-category'}).text
        link = result.find('a').get('href')
        print("Name:", name, "\nDescription:", description, "\nCategory:", category, "\nLink:", link)
        api_no += 1
    url_tag = soup.find('li', {'class': 'pager-next'})
    if url_tag.find('a'):
        url = "https://www.programmableweb.com/" + url_tag.find('a').get('href')
    else:
        break

print("Total APIs:", api_no)
