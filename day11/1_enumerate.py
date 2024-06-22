# Enumerate is used to count the for loop in python

vowels = ("a", "e", "i", "o", "u")
result = enumerate(vowels)
print(result)
print(list(result))  # [(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')]


result = enumerate(vowels, start=1)
print(list(result))  # [(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')]

result = enumerate(vowels, start=5)
print(list(result))  # [(5, 'a'), (6, 'e'), (7, 'i'), (8, 'o'), (9, 'u')]


data = [(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')]
for index, value in data:
    print(index)
    print(value)


data = [6, 2, 1, 9, 40, 12, 21, 100]

result = []
for index, value in enumerate(data):
    if value % 2 == 0:
        result.append(index)
print(result)  # [0, 1, 4, 5, 7]


result = []
for each in data:  # [6, 2, 1, 9, 40, 12, 21, 100]
    if each % 2 == 0:
        each_index = data.index(each)
        result.append(each_index)
print(result)  # [0, 1, 4, 5, 7]
