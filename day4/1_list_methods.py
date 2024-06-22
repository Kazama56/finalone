# clear()
# index()
# count()
# sort()
# reverse()
# copy()
# insert()

vowels = ["a", "e", "i", "o", "u"]
vowels.clear()
print(vowels)  # []

vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("o")
print(result)  # 3

# result = vowels.index("x")  # It gives error
vowels = ["a", "e", "i", "o", "u", "a", "e", "a", "u", "i", "a"]
result = vowels.index("a", 3)
print(result)  # 5

result = vowels.index("a", 6, 9)
print(result)  # 7

result = vowels.index("a", -5, -1)
print(result)  # 7


# count()
vowels = ["a", "e", "i", "o", "u", "a", "e", "a", "u", "i", "a"]
result = vowels.count("i")
print(result)  # 2


# sort()
a = [10, 3, 12, 1, 100, 49, 21]
a.sort()
print(a)  # [1, 3, 10, 12, 21, 49, 100]

a = ["b", "a", "c", "f"]
a.sort()
print(a)
# a = [[1, 2, 3], 1, 2]  # This raises error
# a.sort()
print(a)
# while using sort() method data must be homogenous

a = [10, 3, 12, 1, 100, 49, 21]
a.sort(reverse=True)
print(a)  # [100, 49, 21, 12, 10, 3, 1]


a = [(1, 12), (4, 1), (12, 10), (3, 0)]


def get_second_element(x):  # (1, 12)  12  1  10  0
    return x[1]


a.sort(key=get_second_element)
print(a)  # [(3, 0), (4, 1), (12, 10), (1, 12)]


data = [(1, 2, 12), (3, 1, 14), (1, 1), (5, 2, 0)]

# sort the above list based on last item of the each tuple


def get_last_element(x):
    return x[-1]


data.sort(key=get_last_element)
print(data)  # [(5, 2, 0), (1, 1), (1, 2, 12), (3, 1, 14)]

data.sort(key=get_last_element, reverse=True)
print(data)  # [(3, 1, 14), (1, 2, 12), (1, 1), (5, 2, 0)]


# reverse()
a = [10, 12, 11, 1, 0, 13]
a.reverse()
print(a)  # [13, 0, 1, 11, 12, 10]


# insert()
a = [3, 2, 4, 1, 5]
a.insert(3, "hello")
print(a)  # [3, 2, 4, 'hello', 1, 5]
