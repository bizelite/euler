count = 0
max_count = 0

def collatz(n):
    count = 0
    while n != 1:
        if n%2 == 0:
            n = n / 2
            count += 1
        else:
            n = 3*n + 1
            count += 1

    return count



if __name__ == '__main__':
    max_index = 1
    for i in range(1, 1000000):
        if collatz(i) > max_count:
            max_count = collatz(i)
            max_index = i
    print(max_index)


