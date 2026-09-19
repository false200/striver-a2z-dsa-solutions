class Solution:
    def divide(self, dvd: int, dvr: int) -> int:
        if dvd == dvr: return 1
        sgn = False
        sgn = (dvd < 0) != (dvr < 0)
        dvd , dvr = abs(dvd), abs(dvr)
        c = 0
        while (dvd >= dvr):
            n = 0
            while ((dvr << n) <= dvd):
                n += 1
            c += (1 << (n - 1))
            dvd -= (dvr << (n - 1))
        if sgn: c = -c
        if (c >= ((1 << 31) - 1)): return ((1 << 31) - 1)
        elif (c <= -(1 << 31)): return -(1 << 31)
        return c