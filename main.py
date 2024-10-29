def simple_function(p, n, o):
    print("simple_function")


simple_function(1, 2, 3)
# calling siple function in another function


def call_another_function():
    return simple_function(1, 2, 5)


print("THIS IS ADDED IN FEATURE BRANCH")
call_another_function()


def stash_check():
    print("stash check function")


def push_check():
    print("push check function")
