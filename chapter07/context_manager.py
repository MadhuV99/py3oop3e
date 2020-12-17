# context_manager.py 
import random, string

class StringJoiner(list):
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.result = "".join(self)

def main():
    print(string.ascii_letters)
    with StringJoiner() as joiner:
        for i in range(15):
            joiner.append(random.choice(string.ascii_letters))

    print(joiner.result)

if __name__ == '__main__':
    main()