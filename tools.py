from statistics import mean
import csv
import json

def get_username():
    with open('export/profile.csv', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            return row[1]

def get_rating(uri):
    with open('export/ratings.csv', encoding='utf-8') as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if uri == row[3].split('/')[-1]:
                try:
                    return float(row[4])
                except:
                    return 0
    return 0


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
    nl = list(filter(lambda x: x != 0, lst))
    if nl:
        return mean(nl) if len(nl) >= min_films else 0
    return 0

def highest_rated(dictionary, count, min_films=0):
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

def breakdown_charts(genres, countries, languages):
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

def map_data(countries):
    with open('static/mapping.json') as f:
        country_mapping=json.load(f)
    
    data = {}
    
    for country, details in country_mapping.items():
        print(country)
        data[details['code']] = {
            'count': countries.get(country, 0),
            'label': country,
            'url': details['url']
        }

    return data