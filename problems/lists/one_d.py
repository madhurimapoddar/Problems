# -*- coding: utf-8 -*-

from operator import mul


def get_max_diff(numbers):
    # going in forward direction only find two numbers where the difference between them
    # is the maximum. Print out the numbers as well
    # [2, 3, 10, 6, 4, 8, 1], ans is 8, and the numbers are 2 and 10
    size = len(numbers)
    max_diff = numbers[-1] - numbers[0]
    min_num = numbers[0]
    max_num = 0
    for i in range(1, size):
        if numbers[i] - min_num > max_diff:
            max_diff = numbers[i] - min_num
            max_num = numbers[i]

            if numbers[i] < min_num:
                min_num = numbers[i]

    return max_diff, min_num, max_num


print get_max_diff([2, 3, 10, 6, 4, 8, 1])
print get_max_diff([7, 9, 5, 6, 3, 2])


# Stock Buy Sell to Maximize Profit
#http://www.geeksforgeeks.org/stock-buy-sell/
def maximum_profit(stocks):
    pass


def max_profit_one_transaction(stock_prices_yesterday):
    # https://www.interviewcake.com/question/python/stock-price
    # Time : O(n)
    number_of_stocks = len(stock_prices_yesterday)
    start = 0
    max_profit = 0
    while start < number_of_stocks:
        buy_stock = stock_prices_yesterday[start]
        stocks = stock_prices_yesterday[start + 1:]
        for stock in stocks:
            if stock - buy_stock > max_profit:
                max_profit = stock - buy_stock
        start += 1

    return max_profit


print max_profit_one_transaction([10, 7, 5, 8, 11, 9])


def get_products_of_all_ints_except_at_index(numbers):
    # https://www.interviewcake.com/question/python/product-of-other-numbers
    # input: [1, 7, 3, 4]
    # output : [84, 12, 28, 21]
    products = []
    for index, num in enumerate(numbers):
        if index == 0:
            products.append(reduce(mul, numbers[1:], 1))
        else:
            temp = numbers[0:index] + numbers[index + 1:]
            products.append(reduce(mul, temp, 1))
    return products
print get_products_of_all_ints_except_at_index([1, 7, 3, 4])


def get_highest_product_from_three_integers(numbers):
    # https://www.interviewcake.com/question/python/highest-product-of-3
    
