def gcd(num1, num2):
    if num1 < num2:
        num2, num1 = num1, num2

    if num1 % num2 == 0:
        return num2
    else:
        r = num1 % num2
        return gcd(num2, r)

def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)

def get_nums_lcm(n):
    temp = 1
    for i in range(2, n+1):
        temp = lcm(temp, i)
    return temp

if __name__ == '__main__':
    print(get_nums_lcm(20))
    