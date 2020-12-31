def isCovered(cp_bl, cp_tr, t1_bl, t1_tr, t2_bl, t2_tr):

    set_cp_x = set(range(cp_bl[0], cp_tr[0]))
    set_t1_x = set(range(t1_bl[0], t1_tr[0]))
    set_t2_x = set(range(t2_bl[0], t2_tr[0]))
    set_t_x = set_t1_x.union(set_t2_x)
    x = set_cp_x.issubset(set_t_x)

    set_cp_y = set(range(cp_bl[1], cp_tr[1]))
    set_t1_y = set(range(t1_bl[1], t1_tr[1]))
    set_t2_y = set(range(t2_bl[1], t2_tr[1]))
    set_t_y = set_t1_y.union(set_t2_y)
    y = set_cp_y.issubset(set_t_y)

    for_t1_bl = (cp_bl[0] >= t1_bl[0]) and (cp_bl[1] >= t1_bl[1])
    for_t1_tr = (cp_tr[0] <= t1_tr[0]) and (cp_tr[1] <= t1_tr[1])

    for_t2_bl = (cp_bl[0] >= t2_bl[0]) and (cp_bl[1] >= t2_bl[1])
    for_t2_tr = (cp_tr[0] <= t2_tr[0]) and (cp_tr[1] <= t2_tr[1])

    for_t1 = for_t1_bl and for_t1_tr
    for_t2 = for_t2_bl and for_t2_tr

    a = (cp_bl[0] >= t2_bl[0]) and (cp_bl[0] <= t2_tr[0])
    b = (cp_tr[0] >= t1_bl[0]) and (cp_tr[0] <= t1_tr[0])
    f = (cp_bl[1] >= t1_bl[1]) and (cp_tr[1] <= t1_tr[1]) and (cp_bl[1] >= t2_bl[1]) and (cp_tr[1] <= t2_tr[1])
    c = a and b and f and x and y


    if x and y and (for_t1 or for_t2) or c:
        return "COMPLETELY COVERED"

    else:
        return "NOT COMPLETELY COVERED"
