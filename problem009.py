# Pythagorean theorem 
 c = 997
 while c > 335:
    for a in range(1, 332):
        for b in range(2, 999):
            if a > b or a+b+c != 1000:
                continue
            elif a**2 + b**2 == c**2:
                print(a*b*c)
    c -= 2

