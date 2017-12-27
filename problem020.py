def factorial(n):
    return 1 if n==1 else n*factorial(n-1)

if __name__ == '__main__':
    facto = factorial(100)
    total = 0
    for c in str(facto):
        total += int(c)
    print(total)

