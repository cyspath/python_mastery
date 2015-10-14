# Mike Li
# CS 21A

# In this program, function spell() takes in a int from -999,999,999 to 999,999,999
# and outputs a string of the number spelled out in English.
# spell() will uses two helper function to_a() and read_three()

import math
import random

# convert num to a list
def to_a(num):
    result = []
    while num > 0:
        result.insert(0, num%10)
        num = math.floor(num/10)
    return result

# read upto three digits in a list
def read_three(a):
    set_x = ['','one','two','three','four','five', 'six','seven','eight','nine']
    set_1x = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
                'seventeen','eighteen','ninteen']
    set_x0 = ['', 1,'twenty','thirty','fourty','fifty','sixty', 'seventy','eighty','ninety']
    result = []

    if a[0]!= 0:
        result.append(set_x[a[0]])
        result.append('hundred')

    if a[1] == 1:
        result.append(set_1x[a[2]])
        return result
    else:
        result.append(set_x0[a[1]])

    result.append(set_x[a[2]])
    return result


# converts a number to english representation
def spell(num):
    prefix = []
    if num < 0:
        prefix = ['negative']

    a = to_a(abs(num))

    if len(a)%3 != 0:
        n = 3-(len(a)%3)
        i = 0
        while i < n:
            a.insert(0, 0)
            i += 1

    if len(a) == 3:
        list_with_name = prefix + read_three(a)
    elif len(a) == 6:
        list_with_name = prefix + read_three(a[0:3]) + ['thousand'] + read_three(a[3:len(a)])
    elif len(a) == 9:
        thousand = []
        for el in a[3:6]:
            if el != 0:
                thousand = ['thousand']
        p1 = read_three(a[0:3])
        p2 = read_three(a[3:6])
        p3 = read_three(a[6:len(a)])
        list_with_name = prefix + p1 + ['million'] + p2 + thousand + p3

    return " ".join(list_with_name)

#### Now, testing the results with random numbers:
number1 = random.randint(0, 20)
number2 = random.randint(-999, 0)
number3 = random.randint(0,999999)
number4 = random.randint(-999999,0)
number5 = random.randint(0,999999999)
number6 = random.randint(-999999999,0)

for number in [number1, number2, number3, number4, number5, number6]:
    print(str(number), 'is', spell(number))


# >>> ================================ RESTART ================================
# >>>
# 15 is fifteen
# -875 is negative eight hundred seventy five
# 738205 is seven hundred thirty eight thousand two hundred  five
# -122635 is negative one hundred twenty two thousand six hundred thirty five
# 332453257 is three hundred thirty two million four hundred fifty three thousand two hundred fifty seven
# -310565933 is negative three hundred  million five hundred sixty five thousand nine hundred thirty three
# >>>
