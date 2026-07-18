def lfsr(seed, taps, length):
    sr = seed
    output = []

    for _ in range(length):
        bit = 0
        for t in taps:
            bit ^= (sr >> t) & 1

        sr = (sr >> 1) | (bit << 7)
        output.append(sr & 1)

    return output