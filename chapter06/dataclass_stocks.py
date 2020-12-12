# dataclass_stocks.py
from dataclasses import make_dataclass, dataclass 
from pprint import pprint

class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float

@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

def main():
    # Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
    # stock = Stock("FB", 177.46, high=178.67, low=175.79) 
    # print(stock)
    # print(stock.current)
    # stock.current = 178.25
    # print(stock)
    # stock.unexpected_attribute = 'allowed'
    # print(stock.unexpected_attribute)
    # print(stock) 

    # stock_reg_class = StockRegClass("FB", 177.46, high=178.67, low=175.79)
    # print('stock_reg_class:',stock_reg_class)
    # stock_reg_class2 = StockRegClass("FB", 177.46, 178.67, 175.79)
    # print('stock_reg_class2:',stock_reg_class2)
    # print('stock_reg_class2 == stock_reg_class?', stock_reg_class2 == stock_reg_class)

    # stock1 = Stock("FB", 177.46, high=178.67, low=175.79)
    # print('stock1:',stock1)
    # stock2 = Stock("FB", 177.46, 178.67, 175.79) 
    # print('stock2:',stock2)
    # print('stock1 == stock2?', stock1 == stock2)

    # print(StockDefaults('FB'))
    # print(StockDefaults('FB', 177.46, 178.67, 175.79))

    stock_ordered1 = StockOrdered("FB", 177.46, high=178.67, low=175.79)
    stock_ordered2 = StockOrdered("FB")
    stock_ordered3 = StockOrdered("FB", 178.42, high=179.28, low=176.39)

    print('stock_ordered1 < stock_ordered2?', stock_ordered1 < stock_ordered2)
    print('stock_ordered1 > stock_ordered2?', stock_ordered1 > stock_ordered2)

    pprint(sorted([stock_ordered1, stock_ordered2, stock_ordered3]))


if __name__ == '__main__':
    main()
