def count_bits(n):
    n = bin(n)[2:]
    print(n)
    count = 0
    for i in n:
        if i == "1":
            count += 1

    return count


print(count_bits(4))
