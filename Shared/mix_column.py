def xtimeN(x, n):
    assert(x <= 0xFF)
    assert(n <= 0xFF)
    result = 0
    for i in range(8):
        if n & (1 << i):
            result ^= x
        x = x << 1
        if x & 0x100:
            x ^= 0x11b
    return result