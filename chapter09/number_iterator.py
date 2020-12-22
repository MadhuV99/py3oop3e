# number_iterator.py

class NumberIterable:
    def __init__(self, max_num):
        self.number_range = range(max_num)

    def __iter__(self):
        return NumberIterator(self.number_range)


class NumberIterator:
    def __init__(self, range_of_numbers):
        self.number_list = [n for n in range_of_numbers]
        self.index = 0

    def __next__(self):
        if self.index == len(self.number_list):
            raise StopIteration()
        num = self.number_list[self.index]
        self.index += 1
        return num

    def __iter__(self):
        return self

def main():
    iterable = NumberIterable(10)
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

if __name__ == '__main__':
    main()            