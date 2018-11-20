def main():
    a = 100
    print(f(a))

def f(a):
    if a < 0:
        return -1
    n = a
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            print(n) 
        elif n == 1:
            return 1
            print(n)
        else:
            n = 3 * n + 1
            print(n)  
    return 0

main()

#a = 100: 50 76 58 88 34 52 40 16 - all divided until 1 is left
#a = 10: 5 16 - same
#a = 2: 1
#a = 1: 1
#a = 0: 0
#a = -1: -1
