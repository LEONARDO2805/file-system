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
    print("[2] Add Folder")
    print("[3] Add files")
    print("[4] List Items in Directory")
    print()
    print("[0] Exit")


if __name__ == "__main__":
    main()
