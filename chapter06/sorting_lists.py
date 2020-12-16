# sorting_lists.py 
from functools import total_ordering
from operator import itemgetter

@total_ordering
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num
    
    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string
    
    def __repr__(self):
        return f"{self.string}:{self.number}" 

    def __eq__(self, object):
        return all(
                self.string == object.string,
                self.number == object.number,
                self.sort_num == object.number
                )

def main():
    # a = WeirdSortee('a', 4, True)
    # b = WeirdSortee('b', 3, True)
    # c = WeirdSortee('c', 2, True)
    # d = WeirdSortee('d', 1, True)
    # l = [a,b,c,d]
    # print(l)

    # l.sort()
    # print(l)

    # for i in l:
    #     i.sort_num = False

    # l.sort()
    # print(l)

    # print('l[1] < l[2]?',l[1] < l[2])
    # print('l[1] > l[2]?',l[1] > l[2])

    # l = ["hello", "HELP", "Helo"]
    # l.sort()
    # print(l)
    # l.sort(key=str.lower)
    # print(l) 

    l = [('n', 6), ('h', 4), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
    l.sort()
    print(l)
    l.sort(key=itemgetter(0))
    print(l)
    l.sort(key=itemgetter(1))
    print(l)    

if __name__ == '__main__': 
    main()
