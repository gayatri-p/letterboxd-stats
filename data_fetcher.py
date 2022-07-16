from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import regex as re
import csv

# data = [['2022-03-01','Mulholland Drive',2001,'https://boxd.it/297o'],
        # ['2022-07-11','Videodrome',1983,'https://boxd.it/29uC']]

data = []
with open('watched.csv') as f:
    reader = csv.reader(f)
    # next(reader)
    for row in reader:
        data.append(row)

for row in data:
    name = row[1]
    year = row[2]
    uri = row[3]

    try:
        page = requests.get(uri).text
    except ConnectionError:
        print('No internet connection.')
        break

    soup = BeautifulSoup(page, 'lxml')

    director = soup.find(id='featured-film-header').find('span').string

    cast = []
    s = soup.find(class_='cast-list').find_all('a')
    for m in s:
        if m.string.startswith("Show All"):
            continue
        else:
            cast.append(m.string)

    d = soup.find('p', class_='text-footer')
    # print(d)
    # print(type(d))
    time = re.findall("\d+", str(d))[0]
    # print(time)

    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        row = [uri.split('/')[-1], year, name, director, time, cast]
        # print(row)
        writer.writerow(row)
        # for season in info:
        #     writer.writerows(info[season])

    print(name)