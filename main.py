def simple_function(p):
    print("simple_function")


simple_function(1)
# calling siple function in another function


def call_another_function():
    l = "string"
    return simple_function(1)


print("THIS IS ADDED IN FEATURE BRANCH")
call_another_function()
