# syntactic_sugar.py

class SillyInt(int):
    def __add__(self, num):
        return 0 

def main(): 
    a = SillyInt(1)
    b = SillyInt(2)
    print(a + b) 

if __name__ == '__main__':
    main()    

