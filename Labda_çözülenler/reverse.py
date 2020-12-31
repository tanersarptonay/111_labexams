# Write a recursive function reverse that returns the reverse of a list.

def reverse(lst):
    if not lst:
        return []
    return reverse(lst[1:]) + [lst[0]]

