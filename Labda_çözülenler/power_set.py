# Using the append_element function write a recursive function called "power_set"
# which takes a set as a Python list and returns its power set.
# (The order of the elements in the returned list is not important.)

def power_set(lst):
    if not lst:
        return [[]]
    return [[lst[0]] + sets for sets in power_set(lst[1:])] + power_set(lst[1:])

print(power_set([1,2,3]))