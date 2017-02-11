def prefix_table(pattern):
    # fail function
    m = len(pattern)
    F = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = F[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        F[q] = k
    return F


def KMP_search(text, pattern):
    # O(m + n)
    n = len(text)
    m = len(pattern)
    F = prefix_table(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = F[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1

print KMP_search("bacbabababacaca", "ababaca")


class Node(object):
    def __init__(self):
        self.data = ''
        self.children = {}  # contains a map with child chars as keys and their nodes as values


class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.data = "/"

    def add_word(self, word):
        # Inserting a string
        current_node = self.root
        i = 0
        print "Adding word ", word, " to the trie"
        for char in word:
            print "Adding character ", char
            try:
                current_node = current_node.children[char]
            except:
                self.createSubTree(word[i:len(word)], current_node)
                break
            i = i + 1


def longest_palindrome(string):
    # use suffix tree
    # http://www.geeksforgeeks.org/suffix-tree-application-6-longest-palindromic-substring/
    pass


def fastLongestPalindromes(seq):
    """
    runs in linear time.
    """
    seqLen = len(seq)
    l = []
    i = 0
    palLen = 0
    # Loop invariant: seq[(i - palLen):i] is a palindrome.
    # Loop invariant: len(l) >= 2 * i - palLen. The code path that
    # increments palLen skips the l-filling inner-loop.
    # Loop invariant: len(l) < 2 * i + 1. Any code path that
    # increments i past seqLen - 1 exits the loop early and so skips
    # the l-filling inner loop.
    while i < seqLen:
        # First, see if we can extend the current palindrome.  Note
        # that the center of the palindrome remains fixed.
        if i > palLen and seq[i - palLen - 1] == seq[i]:
            palLen += 2
            i += 1
            continue

        # The current palindrome is as large as it gets, so we append
        # it.
        l.append(palLen)

        # Now to make further progress, we look for a smaller
        # palindrome sharing the right edge with the current
        # palindrome.  If we find one, we can try to expand it and see
        # where that takes us.  At the same time, we can fill the
        # values for l that we neglected during the loop above. We
        # make use of our knowledge of the length of the previous
        # palindrome (palLen) and the fact that the values of l for
        # positions on the right half of the palindrome are closely
        # related to the values of the corresponding positions on the
        # left half of the palindrome.

        # Traverse backwards starting from the second-to-last index up
        # to the edge of the last palindrome.
        s = len(l) - 2
        e = s - palLen
        for j in xrange(s, e, -1):
            # d is the value l[j] must have in order for the
            # palindrome centered there to share the left edge with
            # the last palindrome.  (Drawing it out is helpful to
            # understanding why the - 1 is there.)
            d = j - e - 1

            # We check to see if the palindrome at l[j] shares a left
            # edge with the last palindrome.  If so, the corresponding
            # palindrome on the right half must share the right edge
            # with the last palindrome, and so we have a new value for
            # palLen.
            #
            # An exercise for the reader: in this place in the code you
            # might think that you can replace the == with >= to improve
            # performance.  This does not change the correctness of the
            # algorithm but it does hurt performance, contrary to
            # expectations.  Why?
            if l[j] == d:
                palLen = d
                # We actually want to go to the beginning of the outer
                # loop, but Python doesn't have loop labels.  Instead,
                # we use an else block corresponding to the inner
                # loop, which gets executed only when the for loop
                # exits normally (i.e., not via break).
                break

            # Otherwise, we just copy the value over to the right
            # side.  We have to bound l[i] because palindromes on the
            # left side could extend past the left edge of the last
            # palindrome, whereas their counterparts won't extend past
            # the right edge.
            l.append(min(d, l[j]))
        else:
            # This code is executed in two cases: when the for loop
            # isn't taken at all (palLen == 0) or the inner loop was
            # unable to find a palindrome sharing the left edge with
            # the last palindrome.  In either case, we're free to
            # consider the palindrome centered at seq[i].
            palLen = 1
            i += 1

    # We know from the loop invariant that len(l) < 2 * seqLen + 1, so
    # we must fill in the remaining values of l.

    # Obviously, the last palindrome we're looking at can't grow any
    # more.
    l.append(palLen)

    # Traverse backwards starting from the second-to-last index up
    # until we get l to size 2 * seqLen + 1. We can deduce from the
    # loop invariants we have enough elements.
    lLen = len(l)
    s = lLen - 2
    e = s - (2 * seqLen + 1 - lLen)
    for i in xrange(s, e, -1):
        # The d here uses the same formula as the d in the inner loop
        # above.  (Computes distance to left edge of the last
        # palindrome.)
        d = i - e - 1
        # We bound l[i] with min for the same reason as in the inner
        # loop above.
        l.append(min(d, l[i]))

    return l
print fastLongestPalindromes("abababa")


def findLongestPalindromicString(text):
    # Manacher's algorithm
    N = len(text)
    if N == 0:
        return
    N = (2 * N) + 1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1

    for i in xrange(2, N):
        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = (2 * C) - i
        L[i] = 0
        diff = R - i
        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)

        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or \
                    (text[(i + L[i] + 1) / 2] == text[(i - L[i] - 1) / 2])):
                L[i] += 1
        except Exception:
            pass

        if L[i] > maxLPSLength:        # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            C = i
            R = i + L[i]

    print L
    print maxLPSCenterPosition
    print maxLPSLength
    start = (maxLPSCenterPosition - maxLPSLength) / 2
    print start
    end = start + maxLPSLength - 1
    print text[start:end + 1]

findLongestPalindromicString("abababa")


def find_longest_common_substring(string1, string2):
    # suffix tree
    # linear time
    pass


def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)):
                    answer = match
                match = ""
    return answer


def reverse_string(string):
    # while reversing a long string in python, dont do it all at once.
    # use reversed() returns and iterator and is most pythonic
    # time : O(n), space: O(1)
    s = list(string)
    end = len(string) - 1
    start = 0
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s)
print reverse_string("dog")


def find_pattern_in_text(text, pattern):
    # look up, KMP search
    pass


def reverse_words_in_a_string(string):
    # time : O(N), Space O(N)
    words_stack = []
    string_array = string.split(" ")
    for word in string_array:
        words_stack.append(word)
    while words_stack:
        print words_stack.pop(),

reverse_words_in_a_string("This is a Career Monk String")


def anagrams(element):
    level = [element[0]]
    for i in range(1, len(element)):
        n_list = []
        for item in level:
            n_list.append(item + element[i])
            for j in range(len(item)):
                n_list.append(item[0:j] + element[i] + item[j:i])
            level = n_list
    return n_list

print anagrams("abc")


def permutations(string, step=0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)


permutations("aaa")


def longest_substring_without_repeating_characters(string):
    last_repeating = -1
    longest = 0
    positions = {}
    for i in range(len(string)):
        if string[i] in positions and last_repeating < positions[string[i]]:
            last_repeating = positions[string[i]]
        if i - last_repeating > longest:
            longest = i - last_repeating

        positions[string[i]] = i
    return longest
print longest_substring_without_repeating_characters("ABDEFGABEF")


