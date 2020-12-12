# tuple_stocks.py 
import datetime

def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

def main():
    stock = "FB", 177.46, 178.67, 175.79
    stock2 = ("FB", 177.46, 178.67, 175.79)
    print(stock)
    print(stock2)

    (mid_value, date) = middle(("FB", 177.46, 178.67, 175.79),
                                 datetime.date(2018, 8, 27))
    print('mid_value:', mid_value)
    print('date:', date)

    a_tuple = (stock, stock2)
    print('a_tuple:', a_tuple)
    stock = "FB", 177.46, 0.67, 175.79
    print('a_tuple:', a_tuple)

    stock = "FB", 75.00, 75.03, 74.90
    high = stock[2]
    print(high)


if __name__ == '__main__':
    main()