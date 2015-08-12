def alpha_combs(alphabet, n, acc='', res=[]):
    if n == 0:
        res.append(acc)
    else:
        for c in alphabet:
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


if __name__ == "__main__":

    small_dataset = "T A G C\n2"
    large_dataset = open('rosalind_lexf.txt').read()

    bits = small_dataset.split()

    alphabet = bits[:-1]
    comb_len = int(bits[-1])

    #print alphabet, comb_len

    for p in alpha_combs(alphabet, comb_len):
        print p

