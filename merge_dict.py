# Mike Li
# CS 21A

# In this program, function merge() will take in
# a list of dictionaries and merge them.

# When there are multiple copies of the same key,
# all possible values will be stored in a list in
# the resulting dictionary.

a1 = {1:'a',  2:'b', 3:'c', 4:'d'}
a2 = {10:'i', 20:'j', 3:'k', 40:'l'}
a3 = {100:'s', 200:'t', 3:'u', 400:'v'}
a4 = { 3: "fourth!"}

# expected result {400: 'v', 1: 'a', 2: 'b', 3: ['c', 'k', 'u', 'fourth!'],
#                  4: 'd', 100: 's', 40: 'l', 20: 'j', 10: 'i', 200: 't'}


d1 = {
    'Andrew': 56,
    'Colin': 88,
    'Alan': 95,
    'Mary': 76,
    'Tricia': 99,
    'Tom' : 100
}
d2 = {
    'Andrew': 79,
    'Colin':62,
    'Alan': 88,
    'Mary': 88,
    'Tricia': 92,
    'John' : 100,
    'Tom' : 99
}
d3 = {
    'Andrew': 90,
    'Colin': 60,
    'Alan': 92,
    'Mary': 85,
    'Tricia': 95,
    'Bob' : 100
}

#  expected result {'Bob': 100, 'Tom': [100, 99], 'Alan': [95, 88, 92],
#                   'Andrew': [56, 79, 90], 'Mary': [76, 88, 85], 'John': 100,
#                   'Tricia': [99, 92, 95], 'Colin': [88, 62, 60]}


def merge(alist):
    combined = {}
    for dic in alist:
        for key in dic:
            if key not in combined:
                combined[key] = dic[key]
            elif key in combined and type(combined[key]) != list:
                value = [combined[key]]
                value.append(dic[key])
                combined[key] = value
            else:
                combined[key].append(dic[key])
    return combined

# following print commands will print out merged result of
print(merge([a1, a2, a3, a4]))
print(merge([d1, d2, d3]))


# Output of this module in IDLE.
'''
>>> ================================ RESTART ================================
>>>
{400: 'v', 1: 'a', 2: 'b', 3: ['c', 'k', 'u', 'fourth!'], 4: 'd', 100: 's',
40: 'l', 20: 'j', 10: 'i', 200: 't'}

{'Bob': 100, 'Andrew': [56, 79, 90], 'Alan': [95, 88, 92], 'Mary': [76, 88, 85],
'Colin': [88, 62, 60], 'Tom': [100, 99], 'John': 100, 'Tricia': [99, 92, 95]}

>>>
'''
