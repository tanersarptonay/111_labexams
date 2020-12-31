# Better implementation of fibonacci function which avoids redundant computations.
# This is an example of 'tail recursion'.

def fibonacci(n):
    return helper_func(n, 1, 0)

def helper_func(n, curr, prev):
    if n == 1:
        return curr
    return helper_func(n-1, curr+prev, curr)


print(fibonacci(4))

#1,1,2,3