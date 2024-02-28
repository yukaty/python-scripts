import requests
from bs4 import BeautifulSoup

# GET request to CBC News article
url = "https://www.cbc.ca/news/canada/toronto/international-student-study-permits-data-1.7125827"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get title text
title_element = soup.find('title')
title_text = title_element.text
print(title_text)
print("-----")

# Get first paragraph text
first_p = soup.select_one('#detailContent > div > .story > p')
print(first_p.text)

# Get all h2 text
all_h2 = soup.select('#detailContent > div > .story > h2')
for h2 in all_h2:
    print("- " + h2.text)
