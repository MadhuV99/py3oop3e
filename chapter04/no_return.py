# no_return.py

def call_exceptor():
    print("call_exceptor starts here...\n")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")

def no_return():
    
    print("I am about to raise an exception\n")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


def main():
    # no_return()

    # call_exceptor()

    try:
        no_return()
    except:
        print("I caught an exception")
    
    print("executed after the exception")


if __name__ == '__main__':
    main()
