page = input("Enter something: ")
print(page)
pagenum = 0


if page % 2 == 0:
    print(page)
else:
    print("%60s%d" % (" ", page))
# input something = page, page number should be in the next row.
