# odd_container.py
from collections.abc import Container 

class OddContainer:

    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True 

def main():        
    print('Abstract methods in Container class :', Container.__abstractmethods__) 
    # print('Help on Container.__contains__ method:', help(Container.__contains__))

    odd_container = OddContainer()
    print('Is odd_container an instance of Conatiner class? ', isinstance(odd_container, Container))
    print('Is OddContainer a subclass of Conatiner class? ', issubclass(OddContainer, Container))

    print('Is 1 in odd_container? ', 1 in odd_container)
    print('Is 2 in odd_container? ', 2 in odd_container)
    print('Is 3 in odd_container? ', 3 in odd_container)
    print('Is "a string" in odd_container? ', "a string" in odd_container)


if __name__ == '__main__':
    main()    