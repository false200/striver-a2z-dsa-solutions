def set_rightmost_unset_bit(n):
    return n | (n + 1)  


def unset_rightmost_set_bit(n):
    return n & (n - 1)