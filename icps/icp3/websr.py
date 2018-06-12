
import requests
import urllib.request
import os
from bs4 import BeautifulSoup

html_page = requests.get("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India")



soup = BeautifulSoup(html_page.text, "html.parser")


print(soup.title.string)

for i in soup.find_all('a'):
    print(i.get('href'))




th_list = [ ]

titles = []




for rows in soup.find_all('table', class_='wikitable sortable plainrowheaders') :

    rows_1 = rows.find_all('tr')
    for row in rows_1:
        td = row.find_all("td")
        for i in td:
            print(i.text)

            th = row.find("th")
            if th.text not in th_list:
                th_list.append(th.text)
                print("State or Union Territory:  ", th.text)


print(titles)