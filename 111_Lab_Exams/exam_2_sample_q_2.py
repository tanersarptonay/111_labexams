def nfilter_leq(threshold, nlist):
    """
    Filter out all the values > threshold in the given nested list,
    keeping only values <= threshold. The result should not contain
    any nested empty lists, but result itself can be an empty list, []
    :param threshold: An integer. The filtering threshold.
    :param nlist: A nested list of integers. Return a new, filtered
                  nested list without modifying the input one.
    """

    new_list = []

    if not nlist:
        return []

    if type(nlist[0]) == list:
        filtered_list = nfilter_leq(threshold, nlist[0])
        if filtered_list == []:
            return nfilter_leq(threshold, nlist[1:])
        else:
            return [filtered_list] + nfilter_leq(threshold, nlist[1:])

    if nlist[0] <= threshold:
        new_list.append(nlist[0])

    return new_list + nfilter_leq(threshold, nlist[1:])

