# store even numbers in a list in range 0-50

result = []
for i in range(51):
    if i % 2 == 0:
        result.append(i)

print(result)   # [0, 2,....50]
