def balanced_brackets(brackets):
    #https://www.hackerrank.com/challenges/balanced-brackets
    #https://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html
    brackets = list(brackets)
    prev = ''
    temp = []
    balanced = False
    while brackets:
        current = brackets.pop()
        if current == '{' and prev == '}':
            balanced = True
            if temp:
                temp.pop()
        elif current == '[' and prev == ']':
            balanced = True
            if temp:
                temp.pop()
        elif current == '(' and prev == ')':
            balanced = True
            if temp:
                temp.pop()
        if balanced == False:
            prev = current
            temp.append(current)
        else:
            if temp:
                prev = temp[-1]
    if not temp:
        print True
    else:
        print False


def check_symbol_balance(input):
    symbol_stack = []
    balanced = False
    for symbol in input:
        if symbol in ["{", "(", "["]:
            symbol_stack.append(symbol)
        else:
            if not symbol_stack:
                balanced = False
                return balanced
            else:
                top_symbol = symbol_stack.pop()
                balanced = matches(top_symbol, symbol)
                if balanced == False:
                    return balanced
    return balanced


def matches(top_symbol, symbol):
    matches = {'(': ')', '{': '}', '[': ']'}
    match = matches.get(top_symbol)
    return match == symbol


def largest_rectange(height):
    #https://github.com/kamyu104/LeetCode/blob/master/Python/largest-rectangle-in-histogram.py
    increasing, area, i = [], 0, 0
    while i <= len(height):
        if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
            increasing.append(i)
            i += 1
        else:
            last = increasing.pop()
            if not increasing:
                area = max(area, height[last] * i)
            else:
                area = max(area, height[last] * (i - increasing[-1] - 1))
    print area


def equal_stacks(h1, h2, h3):
    ans = 0
    while h1 and h2 and h3:
        sum_h1 = sum(h1)
        sum_h2 = sum(h2)
        sum_h3 = sum(h3)
        if sum_h1 > sum_h2:
            h1.pop()
        elif sum_h2 > sum_h3:
            h2.pop()
        else:
            h3.pop()
        if sum_h1 == sum_h2 and sum_h1 == sum_h3:
            ans = sum_h1
            break
    print ans


def poisonous_plants(number_of_plants, pesticides):
    # https://www.hackerrank.com/challenges/poisonous-plants
    count = 0
    while True:
        final = [pesticides[0]]
        something_changed = []
        for i in range(1, number_of_plants):
            if pesticides[i] < pesticides[i - 1]:
                final.append(pesticides[i])
                something_changed.append(False)
            else:
                something_changed.append(True)
        if True in something_changed:
            count = count + 1
        pesticides = final
        number_of_plants = len(pesticides)
        if not any(something_changed):
            break
    print count


def calculate_span(price, S):
    n = len(price)
    # Create a stack and push index of fist element to it
    st = []
    st.append(0)
    # Span value of first element is always 1
    S[0] = 1
    # Calculate span values for rest of the elements
    for i in range(1, n):
        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while(len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        S[i] = i + 1 if len(st) <= 0 else (i - st[-1])
        # Push this element to stack
        st.append(i)

price = [100, 80, 60, 70, 60, 75, 85]
S = [0 for i in range(len(price) + 1)]
# Fill the span values in array S[]
calculate_span(price, S)
print S



#poisonous_plants(17, [20, 5, 6, 15, 2, 2, 17, 2, 11, 5, 14, 5, 10, 9, 19, 12, 5])

#equal_stacks([1, 1, 1, 2, 3], [2, 3, 4], [1, 4, 1, 1])

#largest_rectange([2, 1, 2, 3, 1])

#balanced_brackets("{[(])}")
check_symbol_balance("{[(])}")


