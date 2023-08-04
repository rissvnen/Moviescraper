import requests
from bs4 import BeautifulSoup

import Graph

nimet = []
leffat = []
sija = []
numero = 0

for page in range(1, 3):
    if page == 1:
        url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
    else:
        url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    items = soup.find_all("span", class_="lister-item-year text-muted unbold")
    headers = soup.select('.lister-item-header')

    for header in headers:
        title = header.a.text
        nimet.append(title)

    string = "1234567890"

    for item in items:
        year = item.text.strip("()")
        filtered_year = "".join(char for char in year if char in string)
        intyear = int(filtered_year)
        print(filtered_year)
        leffat.append(intyear)
        print(nimet[numero])
        sija.append(numero)
        numero = numero +1

Graph.graph(leffat, sija)

