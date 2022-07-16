# from datetime import datetime
import matplotlib.pyplot as plt
import csv

YEAR = 2021
years = [] #{}
acts = {}
directors = {}
time = 0
films = 0

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    for row in reader:
        # uri, day, name, year, director, time, cast, rat, rewatch...


        if len(row) > 10:
            cast = eval(row[:10])

        for c in cast:
            if c.startswith("Show All"):
                continue
            acts[c] = acts.get(c, 0) + 1
        
        directors[dir_] = directors.get(dir_, 0) + 1
        # years[year] = years.get(year, 0) + 1
        years.append(year)
        time += int(runtime)
        films += 1


def top10(lst):
    s = sorted(lst.items(), key=lambda x: x[1])
    s.reverse()
    for i in range(20):
        print(f'{s[i][0]} ({s[i][1]})') 

total_runtime = f'{time//(24*60)} days {time//(60) - 24*(time//(24*60))} hrs'

print()
print('Broke Letterboxd Pro')
print()
print(films, 'Films')
print(total_runtime)
print(len(directors), 'directors')
print()
top10(acts)
print()
top10(directors)
# print()
# top10(years)

bins = [i for i in range(min(years), max(years)+1)]
# x = []
# for y, n in years.items():
#     for _ in range(n): x.append(y)

plt.hist(years, bins, edgecolor='black')
plt.xlabel('Release Years')
plt.ylabel('Films Watched')
plt.title('Films watched based on release year')
plt.show()