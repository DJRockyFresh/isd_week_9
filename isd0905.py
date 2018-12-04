def main():
    userInput = input("Enter something: ")
    print(count_spaces((userInput)))

def count_spaces(userInput):
    spaces = 0
    for char in userInput:
        if char == " ":
            spaces = spaces + 1
    print("Number of spaces is ", spaces)
            
main()
