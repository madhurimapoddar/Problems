# -*- coding: utf-8 -*-


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
    
9836609393