import math

#10731

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
    set_1x = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
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

    result = []

    if len(a) == 3:
        list_with_name = prefix + read_three(a)
    elif len(a) == 6:
        list_with_name = prefix + read_three(a[0:3]) + ['thousand'] + read_three(a[3:len(a)])
    elif len(a) == 9:
        thousand = []
        for el in a[3:6]:
            if el != 0:
                thousand = ['thousand']
        list_with_name = prefix + read_three(a[0:3]) + ['million'] + read_three(a[3:6]) + thousand + read_three(a[6:len(a)])

    return " ".join(list_with_name)

print(spell(211000000))
print(spell(-999999999))


def move(n, a, c, b):
    if n > 0:
        move(n-1, a, b, c)
        print('move', n, 'to', c)
        move(n-1, b, c, a)


move(3, 'A', 'B', 'C')

#>>> ================================ RESTART ================================
#>>>
