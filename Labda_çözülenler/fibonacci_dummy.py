# Write a function to compute the Nth number of the fibonacci series.
def fib_dummy(n):
    if n <= 2:
        return 1
    return fib_dummy(n-2) + fib_dummy(n-1)

print(fib_dummy(4))

#1,1,2,3,5,8