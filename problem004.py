def first(n):
    return str(n)[0]

def last(n):
    return str(n)[-1]

def middle(n):
    return str(n)[1:-1]

def is_palindrome(n):
    if len(str(n)) <= 1:
        return True

    if first(n) != last(n):
        return False
    else:
        return is_palindrome(middle(n))



if __name__ == '__main__':
    palindrome = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j):
                palindrome.append(i*j)
    print(max(palindrome))




    
