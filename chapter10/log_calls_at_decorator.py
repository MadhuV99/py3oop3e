# log_calls_at_decorator.py
import time

def new_test1(*ar, **ark):
    print("You got hacked!")

def log_calls(func):
    return new_test1
    # def wrapper(*args, **kwargs):
    #     now = time.time()
    #     print(
    #         "Calling {0} with {1} and {2}".format(
    #             func.__name__, args, kwargs
    #         )
    #     )
    #     return_value = func(*args, **kwargs)
    #     print(
    #         "Executed {0} in {1}ms".format(
    #             func.__name__, time.time() - now
    #         )
    #     )
    #     return return_value

    # return wrapper


@ log_calls
def test1(a, b, c):
    print(f"\ttest1 called with {a}, {b} and {c}")

@ log_calls
def test2(a, b):
    print(f"\ttest2 called with {a} and {b}")

@ log_calls
def test3(a, b):
    print(f"\ttest3 called with {a} and {b}")
    time.sleep(1)

# new_test1 = log_calls(test1)
# new_test2 = log_calls(test2)
# new_test3 = log_calls(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)
