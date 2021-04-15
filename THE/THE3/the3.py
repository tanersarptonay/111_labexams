def tuples_to_lists(part_list):  # Converts tuples into lists for easier modifications.
    new_part_list = []
    if (len(part_list) == 1) and type(part_list[0]) == tuple:  # in case of an edge case where root and leaf are same
        new_part_list = [list(part_list[0])]
        return new_part_list
    for item in part_list:
        if type(item[1]) == tuple: new_part_list.append([item[0]] + [[x[0], x[1]] for x in item if type(x) != str])
        else: new_part_list.append(item)
    return new_part_list


def item_finder(new_part_list, name):  # Finds the index number of an assembly or an basic part in the new_part_list.
    for index in range(len(new_part_list)):
        if name in new_part_list[index]: return index


def list_to_tree(part_list):  # Copies and pastes assemblies and basic parts to the list to create a tree.
    new_part_list = tuples_to_lists(part_list)
    tree = new_part_list[:]
    for i in tree:
        if type(i[1]) == list:
            for j in i[1:]:
                index = item_finder(new_part_list, j[1])
                copy = new_part_list[index]  # Copies elements from list.
                j[1] = copy  # Pastes into the (soon-to-be) tree.
    prev_length = 0  # This function created unnecessary tree-like data structures,
    index_saver = 0  # so we need to get rid of them by taking the longest one.
    for index_of_item in range(len(tree)):
        if len(str(tree[index_of_item])) > prev_length:  # If the new list is longer than previous one,
            index_saver = index_of_item  # then save it's index.
            prev_length = len(str(tree[index_of_item]))  # Update the maximum length.
    return tree[index_saver]  # Return the list with the maximum length, which is our tree


def calculate_price(part_list):  # To convert input part_list into a tree
    return calculate_price_helper(list_to_tree(part_list))


def calculate_price_helper(tree):
    if not tree: return 0  # Recursively skipping items creates an empty lists in the end
    if is_leaf(tree): return tree[1]  # If the element is a leaf, then return it's price
    elif type(tree[0]) == str:  # If the first element is str, recursively sum other element's prices
        if len(tree) > 2:
            return calculate_price_helper(tree[1]) + calculate_price_helper(tree[2:])
        else:
            return calculate_price_helper(tree[1])
    elif type(tree[0]) == int:  # If first element is an integer, then recursively multiply with the price
        return tree[0] * calculate_price_helper(tree[1])
    elif type(tree[0]) == list:  # Recursion created list of lists, so we slice and index them and use recursion
        return calculate_price_helper(tree[0]) + calculate_price_helper(tree[1:])


def required_parts_helper(part_list, multiplier=1):
    if not part_list: return []  # Recursively skipping items creates an empty lists in the end
    elif len(part_list) == 2 and type(part_list[0]) == str and type(part_list[1]) == float:  # in case of an edge case
        return [(1, part_list[0])]                                                      # where root and leaf are same
    elif is_leaf_for_req(part_list):  # If element is a leaf, then calculate and return it's price with it's name
        amount = multiplier * part_list[0]
        return [(amount, part_list[1][0])]
    elif type(part_list[0]) == str:  # if the first element is str, skip that element
        return required_parts_helper(part_list[1:], multiplier)
    elif type(part_list[0]) == int:
        # multiply its amount with the previous factor. for e.g if there are two wheels, then there are 2x1 breaks
        return required_parts_helper(part_list[1], multiplier * part_list[0])
    elif type(part_list[0]) == list:  # skipping an element creates lists, so we need to check for that too
        return required_parts_helper(part_list[0], multiplier) + required_parts_helper(part_list[1:], multiplier)


def required_parts(part_list):  # To convert input part_list into a tree
    return required_parts_helper(list_to_tree(part_list))


def stock_check(part_list, stock_list):
    tuplee_list = required_parts(part_list)[:]  # Couldn't integrate the func tuples_to_lists, bc of required_parts
    need_list = []
    for tuplee in tuplee_list:  # Convert tuples into lists for easiness
        need_list.append(list(tuplee))
    short_list = []
    for stock in stock_list:
        for need in need_list:
            if stock[1] == need[1]:  # If we have the needed item in stock,
                need[0] -= stock[0]  # then decrease needed parts by how many we have in stock
            else: continue
    for need in need_list:  # Append items we need in short_list
        if need[0] > 0:
            short_list.append((need[1], need[0]))
    return short_list


def is_leaf(element):  # Check if the element is a leaf without it's amount, for the function calculate_price
    if type(element[0]) == str and type(element[1]) == float: return True
    else: return False


def is_leaf_for_req(element):  # Check if the element is a leaf with it's amount, for the function required_parts
    # difference between is_leaf and this is that this checks the data inside of a leaf.
    if type(element[0]) == int and type(element[1][1]) == float: return True
    else: return False
