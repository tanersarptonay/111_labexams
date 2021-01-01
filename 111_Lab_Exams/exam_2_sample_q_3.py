def bucket_sum(pool, b1, b2, b3):
    """
    Given the capacity of a pool and three buckets, return how many
    ways there are to fill up the pool EXACTLY. Remember that that orders of
    the buckets matter even if they have the same capacity, i.e.
    (b1, b2) and (b2, b1) count as different ways
    :param pool: A positive integer. Capacity of pool
    :param b1, b2, b3: All positive integers. Capacity of each bucket.
    :return: integer
    """

    if pool < 0:
        return 0
    elif pool == 0:
        return 1
    return bucket_sum(pool-b1, b1, b2, b3) + bucket_sum(pool-b2, b1, b2, b3) + bucket_sum(pool-b3, b1, b2, b3)