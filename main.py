def simple_function(p, n):
    print("simple_function")


simple_function(1, 2)
# calling siple function in another function


def call_another_function():
    l = "string"
    return simple_function(1, 2)


print("THIS IS ADDED IN FEATURE BRANCH")
call_another_function()
