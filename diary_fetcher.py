from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import regex as re
import csv
# from datetime import datetime

MAX_CAST_LIMIT = 15

data = []

with open('diary.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

for row in data:
    day = row[7]
    name = row[1]
    year = row[2]
    url = row[3]
    rat = row[4]
    rewatch = True if row[5] == 'Yes' else False

    try:
        page = requests.get(url).text
    except ConnectionError:
        print('No internet connection.')
        break

    soup = BeautifulSoup(page, 'lxml')

    director = soup.find(id='featured-film-header').find('span').string

    cast = []
    s = soup.find(class_='cast-list').find_all('a')
    for i, m in enumerate(s):
        if i == MAX_CAST_LIMIT or m.string.startswith("Show All"):
            continue
        else:
            cast.append(m.string)

    d = soup.find('p', class_='text-footer')
    time = re.findall("\d+", str(d))[0]

    with open('diary_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        row = [url[-6:], day, name, year, director, time, cast, rat, rewatch]
        writer.writerow(row)

    print(name)

