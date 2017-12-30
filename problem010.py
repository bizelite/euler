def prime_number(n):
    divisor_count = 0

    for i in range(1, n+1):
        if n%2 == 0 and n!=2:
            return None
            break

        if n%i == 0:
            divisor_count += 1

    if divisor_count == 2:
        return n
    else:
        return None

def is_prime(num):
    if num==1:
        return False
    loop=num**0.5
    i=2
    while i<=loop:
        if num%i==0:
            return False
        i+=1
    return True

if __name__ == '__main__':
    total = 0
    num = 0

    while num <= 2000000:
        if is_prime(num):
            print(num, total)
            total += num
        num += 1

    print(total)

    


