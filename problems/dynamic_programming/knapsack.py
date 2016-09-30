# -*- coding: utf-8 -*-

#http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
#https://www.youtube.com/watch?v=PLJHuErj-Tw
#Time Complexity: O(nW) where n is the number of items and W is the capacity of knapsack.


def get_max_value(max_weight, weights, values):
    number_of_items = len(weights)
    answer = [[0 for x in range(max_weight + 1)] for x in range(number_of_items + 1)]
    for item in range(number_of_items + 1):
        for wt in range(max_weight + 1):
            if item == 0 or wt == 0:
                answer[item][wt] = 0
            elif weights[item - 1] <= wt:
                answer[item][wt] = max(answer[item - 1][wt], (values[item - 1] + answer[item - 1][wt - weights[item - 1]]))
            else:
                answer[item][wt] = max(values[item - 1], answer[item - 1][wt])

    print answer[number_of_items][max_weight]


# val = [3, 7, 2, 9]
# wt = [2, 3, 4, 5]
# W = 5
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
get_max_value(W, wt, val)
