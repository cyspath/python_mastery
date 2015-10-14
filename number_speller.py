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
    set_x0 = ['', 1,'twenty','thirty','fourty','fifty','sixty', 'seventy','seven','eight','nine']
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
    a = to_a(num)

    if len(a)%3 != 0:
        n = 3-(len(a)%3)
        i = 0
        print(n)
        while i < n:
            a.insert(0, 0)
            i += 1
    print(a)

    result = []

    if len(a) <= 3:
        return read_three(a)
    elif len(a) <= 6:
        return


print(spell(5))

def move(n, a, c, b):
    if n > 0:
        move(n-1, a, b, c)
        print('move', n, 'to', c)
        move(n-1, b, c, a)


move(3, 'A', 'B', 'C')

#>>> ================================ RESTART ================================
#>>>
