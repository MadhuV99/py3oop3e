# custom_sequence.py 

class CustomSequence:
    
    def __len__(self):
        return 5
    
    def __getitem__(self, index):
        return f"x{index}"

class FunkyBackwards:
    
    def __reversed__(self):
        return "BACKWARDS!"

def main():

    normal_list = [1, 2, 3, 4, 5]
    for seq in normal_list, CustomSequence(), FunkyBackwards():
        print(f"\n{seq.__class__.__name__}: ", end="")

        for item in reversed(seq):
            print(item, end=", ") 

if __name__ == '__main__':
    main()
