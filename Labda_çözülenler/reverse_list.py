# Write a function "reverse_lists" that takes a nested list as an argument
# and returns the reverse of the list and all the lists inside it.

def reverse_list(lst):
    if type(lst) != list:
        return lst
    elif len(lst) == 0:
        return []
    return [reverse_list(lst[-1])] + reverse_list(lst[:-1])
