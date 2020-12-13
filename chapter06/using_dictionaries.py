# using_dictionaries.py 

stocks = {
"GOOG": (1235.20, 1242.54, 1231.06),
"MSFT": (110.41, 110.45, 109.84),
} 

def main():
    # print(stocks["GOOG"])
    # # print(stocks["RIM"])
    # print(stocks.get("RIM"))
    # print(stocks.get("RIM", "NOT FOUND"))

    print(stocks.setdefault("GOOG", "INVALID"))
    print(stocks["GOOG"])

    print(stocks.setdefault("BBRY", (10.87, 10.76, 10.90)))
    print(stocks["BBRY"])

    for stock, values in stocks.items():
        print(f"{stock} last value is {values[0]}")

    stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
    print(stocks["GOOG"])

    stocks["TWIT"] = (245.21, 252.64, 245.18)
    print(stocks["TWIT"])        

if __name__ == '__main__':
    main() 

