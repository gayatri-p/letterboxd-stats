import csv
a = []


with open('data copy.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for row in r:
        a.append(row)
        # print(row)
# print(a[0])
with open('watched - Copy.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    i = 0
    for row in r:
        a[i].insert(0, row[3].split('/')[-1])
        i+=1

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(a)

# k = [2019, 2020, 2008, 2012, 2005, 2014, 2017, 2006, 2010, 2015, 1994, 2011, 2013, 2016, 2018, 2021, 2003, 2000, 1980, 1983, 1977, 2002, 1999, 2009, 2004, 2007, 2001, 1996, 1985, 1998, 1965, 1995, 1993, 1982, 1975, 1989, 2022, 1966, 1991]
# v = [23, 10, 5, 11, 6, 26, 26, 3, 9, 16, 2, 8, 16, 28, 22, 15, 3, 5, 1, 2, 1, 8, 4, 6, 7, 8, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1]

# import matplotlib.pyplot as plt

# plt.hist(v)
# plt.show()
# # # d = '''


# # #                                         147 mins  

# # #                                                 More at
# # #                                                 IMDb
# # # TMDb
# # # Report this film

# # # '''

# # # import regex as re

# # # f = re.findall("\d+ mins", d)
# # # time = f[0]
# # # print(time)

# # y = {}
# # a = [1, 1, 2, 3, 3]
# # # for i in a:
# # #         y[i] = y.get(i, 0) + 1 
# # print(a[:5])