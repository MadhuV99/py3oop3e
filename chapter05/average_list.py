# average_list.py

class AverageList(list):
    
    @property
    def average(self):
        return sum(self) / len(self)

def main():
    a = AverageList([1,2,3,4])
    print(a.average)

if __name__ == '__main__':
    main() 