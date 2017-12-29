def prime_number(n):
    divisor_count = 0
    for i in range(1, n+1):
        if n%2 == 0 and n!=2:
            return None

        if n%i == 0:
            divisor_count += 1


    if divisor_count == 2:
        return n
    else:
        return None

if __name__ == '__main__':
    index = 1
    num = 1
    while index <= 10001:
        if prime_number(num):
            print('index = {0}, num = {1}'.format(index, prime_number(num)))
            index += 1
        num += 1




