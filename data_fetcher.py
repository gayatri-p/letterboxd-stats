from datetime import datetime
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import regex as re
import csv
from tqdm import tqdm

total_films = 0

data = []
with open('export/watched.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)
        total_films += 1

def get_film_data(film):
    name = film[1]
    year = film[2]
    uri = film[3]

    try:
        page = requests.get(uri).text
    except ConnectionError:
        print('No internet connection.')
        return

    soup = BeautifulSoup(page, 'lxml')

    # director
    try:
        director = str(soup.find('meta', attrs={'name':'twitter:data1'}).attrs['content'])
    except:
        director = ''

    # cast
    cast = []
    s = soup.find(class_='cast-list').find_all('a')
    for m in s:
        if m.string.startswith("Show All"):
            break
        elif m.string.startswith('Stan Lee'):
            continue
        else:
            cast.append(m.string)

    # country, langs
    no_details = False
    countries=[]
    langs=[]
    try:
        span = soup.find('div', attrs={'id':'tab-details'}).select("span")
    except:
        no_details = True

    if not no_details:
        for s in span:
            if s.contents[0]=="Countries" or s.contents[0]=="Country":
                d1 = s.find_next('div')
                countries = [str(c.contents[0]) for c in d1.find_all('a')]
            if s.contents[0]=="Languages" or s.contents[0]=="Language":
                d1 = s.find_next('div')
                langs = [str(c.contents[0]) for c in d1.find_all('a')]
    
    # genre
    genres=[]
    no_genre = False
    try:
        span = soup.find('div', attrs={'id':'tab-genres'}).select("span")
    except:
        no_genre = True
        
    if not no_genre:
        for s in span:
            if s.contents[0]=="Genres" or s.contents[0]=="Genre":
                d1 = s.find_next('div')
                genres = [str(c.contents[0]) for c in d1.find_all('a', href=True)]

    # runtime
    d = soup.find('p', class_='text-footer')
    time = re.findall("\d+", str(d))[0]

    # times watched
    rewatched = False
    with open('export/diary.csv', encoding='utf-8') as f:
        diary = csv.reader(f)
        next(diary)
        watches = []
        for film in diary:
            if film[1] == name and film[2] == str(year):
                watches.append(datetime.strptime(film[7], '%Y-%m-%d'))
        if len(watches) > 1:
            rewatched = True

    # poster
    if rewatched:
        poster = str(soup.find('div', attrs={'id':'js-poster-col'}).find('img').attrs['src'])
    else:
        poster = ''

    details = [uri.split('/')[-1], year, name, director, time, cast, poster, countries, langs, genres, watches]
    return details

with open('export/data.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['uri', 'Year', 'Name', 'Director', 'Runtime', 'Cast', 'Poster', 'Countries', 'Languages', 'Genres', 'Watches'])
    for i in tqdm(range(total_films), desc="Loading film data..", ascii=False, ncols=75):
        try:
            film_data = get_film_data(data[i])
            writer.writerow(film_data)
        except:
            print(f'\n\nError occured at {data[i][1]} ({data[i][2]})')
            break
