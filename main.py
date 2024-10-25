def simple_function():
    print("simple_function")


simple_function()
# calling siple function in another function


def call_another_function():
    return simple_function()


call_another_function()
