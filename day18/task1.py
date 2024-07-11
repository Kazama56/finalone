"""
Check whether an input number prime or composite
"""
# Positive integer which have only two factors, 1 and the number itself


def check_prime(num):
    count = 0
    if num <= 1:
        return "Neither prime nor composite"
    else:
        for i in range(1, num//2 + 1):  # 1, 2, 3, 4, 5, 6, 7, 8
            if num % i == 0:
                count += 1   # > 2
        if count >= 2:
            return "Composite"
        return "Prime"


result = check_prime(13)
print(result)

result = check_prime(7)
print(result)

result = check_prime(2)
print(result)

result = check_prime(4)
print(result)

result = check_prime(10)
print(result)
