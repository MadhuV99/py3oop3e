# a_singleton.py

class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls
            ).__new__(cls, *args, **kwargs)
        return cls._singleton

def main():
    o1 = OneOnly()
    o2 = OneOnly()
    print(o1 == o2)
    print(o1)
    print(o2)

if __name__ == '__main__':
    main() 