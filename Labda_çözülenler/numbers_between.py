# Write a function called "numbers_between" which takes two integers
# and generates an ordered list of the numbers in between them.

def numbers_between(x, y):
    if x > y:
        return numbers_between(y, x)
    if y == x+1:
        return [x]
    return [x] + numbers_between(x+1, y)

print(numbers_between(5, 1))
