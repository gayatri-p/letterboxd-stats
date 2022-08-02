from flask import Blueprint, render_template
import csv
import datetime
import tools

def get_film_info(name, release_year, year):
    film_info = {}

    with open('export/data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if name == row[2] and release_year == int(row[1]):

                uri = row[0]
                watches = eval(row[10])
                watches = list(filter(lambda x: x.year != str(year), watches))

                film_info = {
                    'uri': uri,
                    'name': name,
                    'release_year': release_year,
                    'director': row[3],
                    'runtime': int(row[4]),
                    'cast': eval(row[5]),
                    'countries': eval(row[7]),
                    'languages': eval(row[8]),
                    'genres': eval(row[9]),
                    'watches': watches,
                    'rating': tools.get_rating(row[0]),
                    'poster': row[6],
                }

                return film_info


def get_yearly_data(year):
    yearly_data = []
    diary_entries = 0
    rewatches = 0
    time = 0
    countries = {}
    genres = {}
    languages = {}
    actors = {}
    directors = {}

    with open('export/diary.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if str(year) != row[7][:4]:
                continue
            
            diary_entries += 1
            name, release_year = row[1], int(row[2])
            
            if row[5] == 'Yes':
                rewatches += 1
                if (name, release_year) in [(film['name'], film['release_year']) for film in yearly_data]:
                    continue
            
            film_info = get_film_info(name, release_year, year)

            time += film_info['runtime']*len(film_info['watches'])

            rating = film_info['rating']

            for c in film_info['countries']:
                countries[c] = countries.get(c, 0) + 1
            for c in film_info['genres']:
                genres[c] = genres.get(c, 0) + 1
            for c in film_info['languages']:
                languages[c] = languages.get(c, 0) + 1

            for c in film_info['cast']:
                actors.setdefault(c, []).append(rating)
            
            directors.setdefault(film_info['director'], []).append(rating)

            yearly_data.append(film_info)

    details = {
        'hours':time//60,
        'diary_entries': diary_entries,
        'rewatches': rewatches,
        'countries': countries,
        'genres': genres,
        'languages': languages,
        'directors': directors,
        'actors': actors,

    }

    return yearly_data, details


def highest_rated_films(data, year, max_current_year=8, max_older=16):

    sorted_by_ratings = sorted(data, key = lambda film: film['rating'], reverse=True)
    i,j = 0,0
    current_year = []
    older = []

    for film in sorted_by_ratings:
        if film['release_year'] == year:
            i+=1
            current_year.append(film)
            if i == 8:
                break

    for film in sorted_by_ratings:
        if film['release_year'] != year:
            j+=1
            older.append(film)
            if j == 16:
                break

    return current_year, older

def get_milestones(data):
    first, *_ = sorted(data, key = lambda film: sorted(film['watches'])[0])
    *_, last = sorted(data, key = lambda film: sorted(film['watches'])[-1])

    return first, last

def get_pie_info(data, year):
    older_releases = 0
    rewatches = 0

    for film in data:
        watches = film['watches']

        for date in watches:
            # print(film['name'])
            if date.year != year:
                older_releases += 1
            
        if len(watches) > 1:
            rewatches += len(watches) - 1

    return {'older_releases': older_releases, 'rewatches':rewatches}

def week_from_date(date_object):
    yday = (date_object - datetime.datetime(date_object.year, 1, 1)).days + 1
    return (yday // 7) + 1

def date_from_week(week, year):
    start = datetime.datetime(year, 1, 1) + datetime.timedelta(days=(week-1)*7)
    end = start + datetime.timedelta(days=6)
    dates = start.strftime('%b %d') + '—' + end.strftime('%b %d')
    return dates

def get_weekly_data(data):
    weeks = {i:0 for i in range(1, 52)}
    weekdays = {1:0, 2:0, 3:0, 4: 0, 5:0, 6:0, 7:0}
    
    for film in data:
        watches = film['watches']
        for day in watches:
            week = week_from_date(day)
            weeks[week] = weeks.get(week, 0) + 1
            weekdays[day.weekday() + 1] += 1

    return weeks, weekdays

yearly = Blueprint('yearly', __name__, template_folder='templates')

@yearly.route('/<year>')
def index(year):
    try:
        if int(year) in [2021, 2022]:
            year = int(year)

            yearly_data, details = get_yearly_data(year)

            highest_rated_of_year, highest_rated_older = highest_rated_films(yearly_data, year)
            milestones = get_milestones(yearly_data)
            most_watched = sorted(yearly_data, key=lambda x: len(x['watches']), reverse=True)[:5]

            actors = details['actors']
            directors = details['directors']
            actors_most_watched = tools.most_watched(actors, 10)
            directors_most_watched = tools.most_watched(directors, 10)
            actors_by_rating = tools.highest_rated(actors, 10, 3)
            directors_by_rating = tools.highest_rated(directors, 10, 2)

            breakdown_chart_info = tools.breakdown_charts(details['genres'], 
                details['countries'], details['languages'])

            pie_chart_info = get_pie_info(yearly_data, year)

            films_by_week, films_by_weekday = get_weekly_data(yearly_data)
            print(films_by_weekday)

            return render_template('yearly.html', YEAR=year, details=details,
                        highest_rated_of_year=highest_rated_of_year,
                        highest_rated_older=highest_rated_older, milestones=milestones,
                        most_watched=most_watched, actors_most_watched=actors_most_watched,
                        actors_by_rating=actors_by_rating, directors_most_watched=directors_most_watched,
                        directors_by_rating=directors_by_rating,
                        breakdown_charts=breakdown_chart_info, pie_chart_info=pie_chart_info,
                        films_by_week=films_by_week, films_by_weekday=films_by_weekday)

    except ValueError:
        return '<h1>404</h1>'
