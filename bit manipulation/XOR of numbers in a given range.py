def xor1ton(n):
    if n % 4 == 0: return n
    elif n % 4 == 1: return 1
    elif n % 4 == 2: return n + 1
    else: return 0


def xor_range(l, r):
    return xor1ton(l) ^ xor1ton(r - 1)