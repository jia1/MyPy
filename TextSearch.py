from time import *

# Knuth-Morris-Pratt
# return True if substring in text else False
def kmp(substring, text): # , len_substring, len_text):
    len_substring = len(substring)
    len_text = len(text)
    # substring and text indices respectively
    s, t = 0, 0
    # list of next indices to jump to when current matching fails
    jump = []
    # f = False if at index 0 of current matching
    # prevents infinite loop
    f = False
    while t < len_text:
        # print "%4d %4d %c" %(s, t, text[t]),
        if substring[s] != text[t]:
            if f and text[t] == substring[0] and t not in jump:
                jump.append(t)
                # print jump,
            s = 0
            t = t+1 if not jump else jump.pop(0)
            # print jump,
            f = False
        else:
            s += 1
            if s == len_substring:
                return True
            if f and text[t] == substring[0] and t not in jump:
                jump.append(t)
            t += 1
            f = True
        # print
    return False

# Boyer-Moore-Horspool
def bmh(substring, text):
    pass

# Simple Text Search
def sts(substring, text):
    len_substring = len(substring)
    len_text = len(text)
    # substring and text indices respectively
    s, t = 0, 0
    while t < len_text:
        if substring[s] != text[t]:
            s = 0
        else:
            s += 1
            if s == len_substring:
                return True
        t += 1
    return False

# Python Built-In Text Search
def pys(substring, text):
    return substring in text
