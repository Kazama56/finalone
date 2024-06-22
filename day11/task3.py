students = [
    {"name": "Alex", "age": 10, "address": "KTM"},
    {"name": "Jane", "age": 19, "address": "KTM"},
    {"name": "Ram", "age": 27, "address": "KTM"},
    {"name": "Sita", "age": 30, "address": "KTM"},
]


result = [student for student in students if student["age"] < 20]

print(result)  # [{"name": "Alex", "age": 10, "address": "KTM"}, {"name": "Jane", "age": 19, "address": "KTM"}]
