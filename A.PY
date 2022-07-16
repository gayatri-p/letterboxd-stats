import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('_mpl-gallery')

# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

d = [(2013, 3.25), (2019, 3.5952380952380953), (2012, 4.15), (2010, 4.125), (2020, 3.5625), (2018, 3.4444444444444446), (2005, 3.9), (2014, 3.9523809523809526), (2017, 3.825), (2006, 3.5), (2015, 3.769230769230769), (1994, 3.25), (2008, 3.8333333333333335), (2011, 3.75), (2016, 3.925), (2021, 3.857142857142857), (2003, 4.833333333333333), (2000, 3.875), (1980, 4.0), (1983, 4.25), (1977, 3.0), (2002, 4.0), (1999, 3.5), (2009, 3.75), (2004, 4.75), (2007, 4.2), (2001, 4.375), (1996, 3.3333333333333335), (1985, 4.0), (1998, 4.0), (1965, 4.0), (1995, 4.5), (1993, 4.0), (1982, 4.0), (1975, 3.5), (1989, 
4.5), (2022, 4.333333333333333), (1966, 4.5), (1991, 5.0)]

x = [s[0] for s in d]
y = [s[1] for s in d]
# plot.

plt.bar(x, y, width=1, edgecolor='black')

# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

# from statistics import mean
# from numpy.lib.nanfunctions import nanmean
# from numpy import nan as NaN
# print(nanmean([1, 2, 3, NaN]))