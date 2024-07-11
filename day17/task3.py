"""
WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
# import time
#
# # @time_taken
# def long_loop():
#     for i in range(100000000):
#         pass
#
# start = time.time()
# long_loop()
# end = time.time()
#
# print("Taken time is", end-start)

"""
WAP to create a decorator function which when applied to a function gives the execution time
of the function
"""
import time


def time_taken(func):
    def inner_fxn(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        end = time.time()
        print("Time execution is", end-start)
        return x
        # return end

    return inner_fxn


# @time_taken
# def long_loop():
#     for i in range(100000000):
#         pass


@time_taken
def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)
