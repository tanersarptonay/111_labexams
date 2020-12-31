# Write a function named "every" that takes a function and a list as arguments
# and applies the function to each item in the list and returns a list containing the returning values.

def every(func, lst):
    if not lst: # actually this part isn't necessary
        return []
    if len(lst) == 1:
        return [func(lst[0])]
    return [func(lst[0])] + every(func, lst[1:])

func = lambda x : x**2

lst = [1,2,3,4,5]

print(every(func, lst))