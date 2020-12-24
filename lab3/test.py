from operator import itemgetter

def myFunc(e):
  return e[1]

cars = [
    ('score', 2005),
    ('score', 2000),
    ('score', 2019),
    ('score', 2011)
]

cars.sort(key=lambda x:x[1])

print(cars)