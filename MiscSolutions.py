# Assumes input is a number
a, b, c = 0, 1, 0
def fib(n):
    print c
    if n > 0:
        a, b = b, c
        c = a + b
        return fib(n - 1)

# Assumes input is a list (although it may function for a string)
def print_even(xs):
    if len(xs) > 0: # increases runtime
        if xs[0] % 2 == 0:
            print xs[0]
        return print_even(xs[1:])
