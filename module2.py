def main():
    n = 4
    print(mystery(n))

def mystery(n):
    if n <= 0:
        return 0
    else:
        return n + mystery(n - 1)

main()
