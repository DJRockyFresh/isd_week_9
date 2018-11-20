def main():
    n = 20
    print(mystery(n))

def mystery(n):
    if n <= 0:
        return 0
    else:
        return mystery(n // 2) + 1

main()
