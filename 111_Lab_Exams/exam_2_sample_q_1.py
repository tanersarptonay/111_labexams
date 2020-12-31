def maze(lst):
    """
    Given the maze, return how many different distinct ways to find the way to gome.
    lst: 2d list that stores maze information.
    Each list inside the lst corresponds to a row in the maze.
    """

    if len(lst) == 1 and "x" in lst[0]:
        # If the path on the bottom is blocked but character is on the final row
        return 0

    elif len(lst) == 1:
        # Character is on the final row
        return 1

    elif len(lst[0]) == 1 and lst[1][0] == "x":
        # If there's only one column and path on the bottom is blocked
        return 0

    elif len(lst[0]) == 1 and lst[1][0] == "o":
        # If there's only one column and path on the bottom is free
        return maze(lst[1:])

    elif lst[1][0] == "x" and lst[0][1] == "x":
        # If both sides are blocked
        return 0

    elif lst[1][0] == "o" and lst[0][1] == "x":
        # If only the path on the bottom is free
        return maze(lst[1:])

    elif lst[0][1] == "o" and lst[1][0] == "x":
        # If only the path on the right is free
        return maze([i[1:] for i in lst])

    elif (lst[1][0] == "o") and (lst[0][1] == "o"):
        # If both sides are free
        return maze(lst[1:]) + maze([i[1:] for i in lst])





