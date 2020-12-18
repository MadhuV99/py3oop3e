# passing_functions.py

def my_function():
    print("The Function Was Called")

my_function.description = "A silly function"

def second_function():
    print("The second was called")

second_function.description = "A sillier function."

def another_function(the_function):
    print("The description:", end=" ")
    print(the_function.description)
    print("The name:", end=" ")
    print(the_function.__name__)
    print("The class:", end=" ")
    print(the_function.__class__)
    print("The class.name:", end=" ")
    print(the_function.__class__.__name__)
    print("Now I'll call the function passed in")
    the_function()

def main():
    another_function(my_function)
    another_function(second_function)

if __name__ == '__main__':
    main()    