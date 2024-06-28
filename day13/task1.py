# Create a student dictionary.
# Create a function which takes dictionary key (string) as argument and return the value of that key



def get_value(x):
    print(student, "<----------")
    r = student.get(x, "The info is not available")
    return r

student = {"name": "Alex", "age": 30, "address": "KTM", "roll": 31}

key = input("Enter the key you want to access ")
result = get_value(key)
print(result)



student = {"name": "Ram", "age": 30}
key = "name"
roll = student.get(key, 21)
print(roll)