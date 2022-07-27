from re import A
from flask import Blueprint, render_template
import csv
from statistics import mean
from random import randint

years = {}
acts = {} #'actor': [rat1, rat2, rat3]
directors = {} #'director': [rat1, rat2, rat3]
countries = {}
genres = {}
languages = {}
time = 0
films = 0

# vals = [chr(i) for i in range(65, 75)]

def get_rating(uri):
    with open('export/ratings.csv', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if uri == row[3].split('/')[-1]:
                return float(row[4])

    return None

with open('export/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        year, name, dir_, runtime, cast = int(row[1]), row[2], row[3], row[4], eval(row[5])
        rating = get_rating(row[0])

        country = genre = language = chr(randint(65, 75))

        if len(row) > 10:
            cast = eval(row[:10])

        for c in cast:
            if c.startswith("Show All"):
                continue
            acts.setdefault(c, []).append(rating)
        
        directors.setdefault(dir_, []).append(rating)
        years.setdefault(year, []).append(rating)
        time += int(runtime)
        films += 1

        countries[country] = countries[country] + 1 if country in countries else 1
        genres[genre] = genres[genre] + 1 if genre in genres else 1
        languages[language] = languages[language] + 1 if language in languages else 1

tot_time = f'{time//(60)}'
tot_films = str(films)
tot_directors = f'{len(directors)}'

def most_watched(lst, count):
    s = sorted(lst.items(), key=lambda x: len(x[1]))
    s.reverse()
    r = []
    for i, a in enumerate(s):
        if i >= count:
            break
        r.append((a[0], len(a[1])))
    return r

def w_avg(lst, min_films=0):
    nl = list(filter(None, lst))
    return mean(nl) if len(nl) >= min_films else 0

def highest_rated(lst, count, min_films):
    ''' atleast <min_films> films watched AND rated '''

    s = sorted(lst.items(), 
        key=lambda x: w_avg(x[1], min_films))
    s.reverse()

    r = []

    try:
        for i in range(count):
            avg = w_avg(s[i][1], min_films)
            r.append((s[i][0], round(avg, 2)))
    except:
        return r
    # print(r)
    return r


actors_most_watched = most_watched(acts, 10)
directors_most_watched = most_watched(directors, 10)
actors_by_rating = highest_rated(acts, 10, 4)
directors_by_rating = highest_rated(directors, 10, 2)


def films_by_year_chart(chartID = 'films-by-release-year-chart', chart_type = 'column'):
    miny, maxy = min(years), max(years)
    bins = [i for i in range(miny, maxy+1)]
    count = []
    ratings = []
    for year in bins:
        if year in years:
            ratings.append(w_avg(years[year]))
            count.append(len(years[year]))
        else:
            count.append(0)
            ratings.append(0)

    height = 200
    chart = {"renderTo": chartID, "type": chart_type, "height": height, "backgroundColor": 'transparent'}

    chart_info = {'chartID':chartID, 
            'chart':chart, 
            'bins': bins,
            'count': count,
            'ratings': ratings,
            'miny': miny,
            'maxy': maxy,
        }

    return chart_info

def breakdown_charts():

    return {
        'genre_keys': list(genres.keys()),
        'genre_vals': list(genres.values()),
        'country_keys': list(countries.keys()),
        'country_vals': list(countries.values()),
        'language_keys': list(languages.keys()),
        'language_vals': list(languages.values()),
    }

alltime = Blueprint('alltime', __name__, template_folder='templates')

@alltime.route('alltime')
@alltime.route('/')
def index():
    return render_template('index.html', tot_time=tot_time, tot_films=tot_films, tot_directors=tot_directors,
                            actors_most_watched=actors_most_watched, actors_by_rating=actors_by_rating,
                            directors_most_watched=directors_most_watched, directors_by_rating=directors_by_rating,
                            films_by_year_chart=films_by_year_chart(),
                            breakdown_charts=breakdown_charts())
