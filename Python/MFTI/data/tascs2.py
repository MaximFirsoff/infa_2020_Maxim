from itertools import product, permutations, combinations, combinations_with_replacement, groupby, starmap, accumulate

olist = [1,2,3,4,5,6]

def decarmltp(a: list, b: list):
    fg = product(a, b)
    print(*fg)

def get_combinations(a: str, b: int):
    lst = ()
    for i in range(b+1):
        fg = combinations(a, i)
        lst += (*fg,)
    print(lst)


class Fibonachin:

    def __init__(self, chprint):
        for i in range(chprint+1):
            print(f"Fibonachi for {i} is {self.fibona(i)}")

    def fibona(self, chislo):
        if chislo == 1:
            return 1
        if chislo == 0:
            return 0
        tg = self.fibona(chislo-1) + self.fibona(chislo-2)
        return tg



def fhy(k):
    if(k == 1):
        return k
    return fhy(k-1) + k

t = [1,2,3,4,5,6]
f = [1,2,3,4,5,6]

decarmltp(t, f)

gf = permutations("1234", 4)
print(*gf)

get_combinations("1234", 4)

gf = combinations_with_replacement("1234", 4)
print(*gf)

s = 'AAAAATTTTAA'
for key, group in groupby(s, lambda x: x[0]):
    print("Char %s is %s times." % (key, len(list(group))))

def tws(a):
    return a**2

def zipanalog(fistlist: list, secondlist: list):
    """
    analog zip-function
    """
    ziptuple = []
    minlenth = min(len(fistlist), len(secondlist))
    fistlist = list(fistlist)
    secondlist = list(secondlist)
    for x in range(minlenth):
        ziptuple.append((fistlist[x], secondlist[x]))
    return ziptuple

def mapanalog(fisfunction, secondlist: list):
    """
    analog map-function
    """
    secondlist = list(secondlist)
    maplist = []
    for x in secondlist:
        maplist.append(fisfunction(x))
    return maplist

def sumtt(a):
    return a+a


def enumanalog(secondlist: list):
    """
    analog enumerate-function
    """
    secondlist = list(secondlist)
    enlist = []
    for x in range(len(secondlist)):
        enlist.append((x, secondlist[x]))
    return enlist

print(enumanalog("ffff"))


print(mapanalog(sumtt, "ffff"))


print(zipanalog("dddd", "ffff"))

a = [8,-11,4,2,-5]
print(max(a,key=tws))

gh = starmap(max, [(2,5), (3,2), (10,3)])
gh = [i**2 for i in gh]
print(*gh)
gh = accumulate(list(gh))
print(list(gh)[-1:])

fibmord = Fibonachin(6)

print(fhy(10))

list_of_fibonachi = [x for x in range(6)]
print(list_of_fibonachi)