from flask import Blueprint, render_template
import csv
from statistics import mean
from random import randint
import datetime

years = {}
acts = {}
directors = {}
countries = {}
genres = {}
languages = {}
rewatched_films = []
time = 0
films = 0

def get_rating(uri):
    with open('export/ratings.csv', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if uri == row[3].split('/')[-1]:
                try:
                    return float(row[4])
                except:
                    return None
    return None

with open('export/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        year, name, dir_, runtime, cast = int(row[1]), row[2], row[3], row[4], eval(row[5])
        rating = get_rating(row[0])

        country, language, genre= eval(row[7]), eval(row[8]), eval(row[9])
        for c in country:
            countries[c] = countries.get(c, 0) + 1
        for g in genre:
            genres[g] = genres.get(g, 0) + 1
        for l in language:
            languages[l] = languages.get(l, 0) + 1

        for c in cast:
            acts.setdefault(c, []).append(rating)
        
        directors.setdefault(dir_, []).append(rating)
        years.setdefault(year, []).append(rating)
        films += 1

        watches = eval(row[10])
        times_watched = 1 if len(watches) == 0 else len(watches)
        if times_watched > 1:
            poster = row[6]
            rewatched_films.append({'name': name, 'times': times_watched, 'poster': poster})

        time += int(runtime)*times_watched

def most_watched(dictionary, count):
    integer_value = True if isinstance(list(dictionary.values())[0], int) else False

    if integer_value:
        top = sorted(dictionary.items(), key=lambda x: x[1])
    else:
        top = sorted(dictionary.items(), key=lambda x: len(x[1]))

    top.reverse()
    top_count = {}

    for i, item in enumerate(top):
        if i >= count:
            break
        top_count[item[0]] = item[1] if integer_value else len(item[1])

    return top_count

def average(lst, min_films=0):
    nl = list(filter(None, lst))
    if nl:
        return mean(nl) if len(nl) >= min_films else 0
    return 0

def highest_rated(dictionary, count, min_films):
    ''' atleast <min_films> films watched AND rated '''

    top = sorted(dictionary.items(), 
        key=lambda x: average(x[1], min_films))
    top.reverse()

    top_count = []

    try:
        for i in range(count):
            avg = average(top[i][1], min_films)
            top_count.append((top[i][0], round(avg, 2)))
    except:
        return top_count
    return top_count

def films_by_year_chart(chartID = 'films-by-release-year-chart', chart_type = 'column'):
    miny, maxy = min(years), max(years)
    bins = [i for i in range(miny, maxy+1)]
    count = []
    ratings = []
    for year in bins:
        if year in years:
            ratings.append(average(years[year]))
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
    top_genres = most_watched(genres, 10)
    top_countries = most_watched(countries, 10)
    top_languages = most_watched(languages, 10)
    return {
        'genre_keys': list(top_genres.keys()),
        'genre_vals': list(top_genres.values()),
        'country_keys': list(top_countries.keys()),
        'country_vals': list(top_countries.values()),
        'language_keys': list(top_languages.keys()),
        'language_vals': list(top_languages.values()),
    }


lifetime_stats = {
    'tot_time' : f'{time//60}',
    'tot_films' : str(films),
    'tot_directors' : f'{len(directors)}',
    'tot_countries' : f'{len(countries)}'
}

actors_most_watched = most_watched(acts, 10)
directors_most_watched = most_watched(directors, 10)
actors_by_rating = highest_rated(acts, 10, 4)
directors_by_rating = highest_rated(directors, 10, 2)
films_most_watched = sorted(rewatched_films, key=lambda x: x['times'], reverse=True)

# print(most_watched(acts, 10))
alltime = Blueprint('alltime', __name__, template_folder='templates')

@alltime.route('alltime')
@alltime.route('/')
def index():
    return render_template('index.html', lifetime_stats=lifetime_stats,
                            actors_most_watched=actors_most_watched, actors_by_rating=actors_by_rating,
                            directors_most_watched=directors_most_watched, directors_by_rating=directors_by_rating,
                            films_most_watched=films_most_watched,
                            films_by_year_chart=films_by_year_chart(),
                            breakdown_charts=breakdown_charts(),
                            countries=countries)
