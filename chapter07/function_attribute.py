# function_attribute.py 

class A:
    def print(self):
        print("my class is A")

def fake_print():
    print("my class is not A")

def new_print(self):
    print("my class is not A")    

def main():
    a = A()
    a.print()
    
    # a.print = fake_print
    A.print = new_print
    a.print() 


if __name__ == '__main__':
    main()