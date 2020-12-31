# Write a function named "sum_all" that sums all the numbers in a nested list.

def sum_all(lst):
    if type(lst) != list:
        return lst
    if not lst:
        return 0
    return sum_all(lst[0]) + sum_all(lst[1:])
