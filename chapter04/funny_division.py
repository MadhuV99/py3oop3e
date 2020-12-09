# funny_division.py 

def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!" 

def funny_division2(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero" 

def funny_division3(divider):
    try:
        if divider == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divider
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise        

def main():
    # print(funny_division(0))
    # print(funny_division(50.0))
    # print(funny_division("0"))  
    # print(funny_division("Hi"))  

    # for val in (0, "hello", 50.0, 13, 25):
    #     print("Testing {}:".format(val), end=" ")
    #     print(funny_division2(val))

    # for val in (0, "hello", 50.0, 13, 25):
    #     print("Testing {}:".format(val), end=" ")
    #     print(funny_division3(val)) 

    try:
        raise ValueError("This is an argument")
    except ValueError as e:
        print("The exception arguments were", e.args)        

if __name__ == '__main__':
    main() 
