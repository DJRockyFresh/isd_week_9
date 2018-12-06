def main():
    page = input("Enter something: ")
    print(count_symbols(page))

def count_symbols(page):
    pagenum = 1
    if len(page) % 2 == 0:
        print(page)
        print("%-9s"%(pagenum))
    else:
        print(page)
        print("%60s%d" % (" ", pagenum))

main()
