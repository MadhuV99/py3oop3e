# even_integers.py

class EvenOnly(list):

    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def main():
    e = EvenOnly()
    # e.append("a string")

    # e.append(3) 

    e.append(2)
    print(e)

if __name__ == '__main__':
    main()

