import itertools
from multiprocessing import Process
import time
import os

my_input = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 45, 89]

# task 1
def countUp(number):
    while number < 10:
        number += 1
        time.sleep(1)
        print("countUp = ", number)

def countDown(number):
    while number > 0:
        number -= 1
        time.sleep(1)
        print("countDown = ", number)


if __name__ == '__main__':

    procUp = Process(target=countUp, args=(5,))
    procDown = Process(target=countDown, args=(5,))
    procUp.start()
    procDown.start()


# task 2
#1


for i in my_input:
    if i < 5:
        print(i)
#2
print(*itertools.filterfalse(lambda x: x >= 5, my_input))

#3
print(*filter(lambda x: x < 5, my_input))

#3
print([x for x in my_input if x < 5])


# task 3
#1
print(*itertools.filterfalse(lambda x: x % 15 != 0, my_input))
#2
print(*filter(lambda x: x % 15 == 0, my_input))