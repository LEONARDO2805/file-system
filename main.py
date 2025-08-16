def main():

    current_directory = "root"
    printMenu(current_directory)

    inpt = -1

    while(inpt != "0"):
        inpt = input()
        printMenu(current_directory)

def printMenu(current):
    print(current)
    print("[1] Change Directory")
    print("[2] Move Back")
    print("[3] List files")
    print()
    print("[0] Exit")

if __name__ == "__main__":
    main()
