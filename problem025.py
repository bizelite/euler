def fibo_count(length):
    n1 = 1
    n2 = 1
    count = 1

    while len(str(n1)) < length:
        n1, n2 = n2, n1+n2
        count += 1

    return count, str(n1)



if __name__ == '__main__':
    print(fibo_count(1000))


