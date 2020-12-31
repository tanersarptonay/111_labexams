# Write a recursive function named "append_element" which takes two arguments.
# The first argument is a Python value and the second element is a list of nested lists.
# The function should append the first argument to each nested list in the second argument.

def append_element(value, nested_l):

    if len(nested_l) == 1:
        nested_l[0].append(value)
        return [nested_l[0]]
    nested_l[0].append(value)
    return [nested_l[0]] + append_element(value, nested_l[1:])

def append_elementtt(e, lst):
    if not lst:             # notice that the empty list corresponds to False
        return []
    else:
        return [lst[0] + [e]] + append_element(e, lst[1:])



listo = [[1,2,3,4], ["m","e","r"], [31,31,31], []]
val = "hobo"

print(append_elementtt(val, listo))