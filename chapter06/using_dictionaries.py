# using_dictionaries.py 

stocks = {
"GOOG": (1235.20, 1242.54, 1231.06),
"MSFT": (110.41, 110.45, 109.84),
} 

class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue 

def main():
    # print(stocks["GOOG"])
    # # print(stocks["RIM"])
    # print(stocks.get("RIM"))
    # print(stocks.get("RIM", "NOT FOUND"))

    # print(stocks.setdefault("GOOG", "INVALID"))
    # print(stocks["GOOG"])

    # print(stocks.setdefault("BBRY", (10.87, 10.76, 10.90)))
    # print(stocks["BBRY"])

    # for stock, values in stocks.items():
    #     print(f"{stock} last value is {values[0]}")

    # stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
    # print(stocks["GOOG"])

    # stocks["TWIT"] = (245.21, 252.64, 245.18)
    # print(stocks["TWIT"])        

    random_keys = {}
    random_keys["astring"] = "somestring"
    random_keys[5] = "aninteger"
    random_keys[25.2] = "floats work too"
    random_keys[("abc", 123)] = "so do tuples"

    my_object = AnObject(14)
    random_keys[my_object] = "We can even store objects"
    my_object.avalue = 12
    try:
        random_keys[[1,2,3]] = "we can't store lists though"
    except:
        print("unable to store list\n")
    for key, value in random_keys.items():
        print("{} has value {}".format(key, value))

    print(my_object.__dict__)

if __name__ == '__main__':
    main() 

