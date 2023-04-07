import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            bid_price = float(quote['top_bid']['price'])
            ask_price = float(quote['top_ask']['price'])
            expected_price = (ask_price + bid_price) / 2
            stock = quote['stock']
            expected_data_point = (stock, bid_price, ask_price, expected_price)
            self.assertEqual(getDataPoint(quote), expected_data_point)
  
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
            bid_price = float(quote['top_bid']['price'])
            ask_price = float(quote['top_ask']['price'])
            expected_price = (ask_price + bid_price) / 2
            stock = quote['stock']
            expected_data_point = (stock, bid_price, ask_price, expected_price)
            self.assertEqual(getDataPoint(quote), expected_data_point)
  

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_PriceBZero(self):

        prices = {
          'ABC': 123,
          'DEF': 0
                      }
        self.assertIsNone(getRatio(prices["ABC"], prices["DEF"]))
  def test_getRatio_PriceAZero(self):

        prices = {
          'ABC': 0,
          'DEF': 123
                      }
        price = 0
        self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), price)
  def test_getRatio(self):

        prices = {
          'ABC': 234,
          'DEF': 123
                      }
        price = prices['ABC']/prices['DEF']
        self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), price)

if __name__ == '__main__':
    unittest.main()
