# from datetime import time
import matplotlib.pyplot as plt
import csv
from statistics import mean
from tabulate import tabulate
import os

years = {}
acts = {} #'actor': [rat1, rat2, rat3]
directors = {} #'director': [rat1, rat2, rat3]
time = 0
films = 0

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

def most_watched(lst, count):
    s = sorted(lst.items(), key=lambda x: len(x[1]))
    s.reverse()
    r = []
    for i in range(count):
        r.append(f'{s[i][0]} ({len(s[i][1])})') 
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

    for i in range(count):
        avg = w_avg(s[i][1], min_films)
        r.append(f'{s[i][0]} ({round(avg, 2)})')

    return r




''' Display '''

tot_time = f'{time//(60)}'
tot_films = f'{films} Films'
tot_directs = f'{len(directors)} directors'

print()
print(tabulate([['A Life in Film']], tablefmt="grid"))
print()
print(tabulate([[tot_time, tot_films, tot_directs], 
                ['hours', 'films', 'directors']], tablefmt='simple', stralign='center'))
print()

t1 = [(a, b) for a, b in zip(most_watched(acts, 10), most_watched(directors, 10))]
t1 = tabulate(t1, headers=('Most watched actors', 'Most watched directors'))
print(t1)

print()
print()

t2 = [(a, b) for a, b in zip(highest_rated(acts, 8, 4), highest_rated(directors, 8, 2))]
t2 = tabulate(t2, headers=('Highest rated actors', 'Highest rated directors'))
print(t2)



''' Graphing '''

bins = [i for i in range(min(years), max(years)+1)]
x_count = []
y_average = []

for year, rats in years.items():
    x_count.extend([year for _ in range(len(rats))])
    y_average.append(w_avg(rats, 0))

f1 = plt.figure(1)
plt.hist(x_count, bins, edgecolor='black')
plt.xlabel('Release Years')
plt.ylabel('Films Watched')
plt.title('Films watched based on release year')

f2 = plt.figure(2)
plt.bar(years.keys(), y_average, edgecolor='black', width=1)
plt.xlabel('Release Years')
plt.ylabel('Average rating')
plt.title('Avgerage ratings vs release year')

plt.show()