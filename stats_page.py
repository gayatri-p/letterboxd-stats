from flask import Blueprint, render_template, url_for
import csv
from statistics import mean
from random import randint
import datetime
# import json
import tools

USERNAME = tools.get_username()

years = {}
acts = {}
directors = {}
countries = {}
genres = {}
languages = {}
rewatched_films = []
time = 0
films = 0

with open('export/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        year, name, dir_, runtime, cast = int(row[1]), row[2], row[3], row[4], eval(row[5])
        rating = tools.get_rating(row[0])

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

def films_by_year_chart():
    miny, maxy = min(years), max(years)
    bins = [i for i in range(miny, maxy+1)]
    count = []
    ratings = []
    for year in bins:
        if year in years:
            ratings.append(tools.average(years[year]))
            count.append(len(years[year]))
        else:
            count.append(0)
            ratings.append(0)

    chart_info = {
            'bins': bins,
            'count': count,
            'ratings': ratings,
            'miny': miny,
            'maxy': maxy,
        }

    return chart_info

# def map_data(countries):
#     with open('static/mapping.json') as f:
#         country_mapping=json.load(f)
    
#     data = {}
    
#     for country, details in country_mapping.items():
#         print(country)
#         data[details['code']] = {
#             'count': countries.get(country, 0),
#             'label': country,
#             'url': details['url']
#         }

#     return data

breakdown_chart_info = tools.breakdown_charts(genres, countries, languages)

lifetime_stats = {
    'tot_time' : f'{time//60}',
    'tot_films' : str(films),
    'tot_directors' : f'{len(directors)}',
    'tot_countries' : f'{len(countries)}'
}

actors_most_watched = tools.most_watched(acts, 10)
directors_most_watched = tools.most_watched(directors, 10)
actors_by_rating = tools.highest_rated(acts, 10, 4)
directors_by_rating = tools.highest_rated(directors, 10, 2)
films_most_watched = sorted(rewatched_films, key=lambda x: x['times'], reverse=True)

alltime = Blueprint('alltime', __name__, template_folder='templates')

@alltime.route('alltime')
@alltime.route('/')
def index():
    return render_template('index.html', USERNAME=USERNAME, lifetime_stats=lifetime_stats,
                            actors_most_watched=actors_most_watched, actors_by_rating=actors_by_rating,
                            directors_most_watched=directors_most_watched, directors_by_rating=directors_by_rating,
                            films_most_watched=films_most_watched,
                            films_by_year_chart=films_by_year_chart(),
                            breakdown_charts=breakdown_chart_info,
                            countries=countries, map_data=tools.map_data(countries))
