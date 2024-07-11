# Create a decorator function login_required which when applied to a function, asks for password.
# If the provided password is "1234" then execute the function else return "Invalid Password. User not authenticated"
# Boilerplate

def login_required(func):
    def inner_fxn(*args, **kwargs):
        pw = input("Enter the password ")
        if pw == "1234":
            return func(*args, **kwargs)
        else:
            return "Invalid password. User not authenticated"
    return inner_fxn


@login_required
def addition(a, b, c):
    return a + b + c


result = addition(1, 2, 3)
print(result)


@login_required
def display(msg):
    return msg


result = display("Hello World")
print(result)
