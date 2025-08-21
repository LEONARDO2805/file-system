def main():



    #printMenu(current_directory)

    inpt = -1

    root = Node("Root", False)
    current_directory = root
    root.add_child("Desktop", False)
    root.add_child("Downloads", False)
    root.add_child("Documents", False)



    while(inpt != "0"):

        printMenu(current_directory)
        inpt = input()


        if(inpt == "2"):
            name = input("Input the name of the folder you would like to add")
            current_directory.add_child(name, False)
            print(name + " folder was added successfully")

        elif (inpt == "4"):
            current_directory.list_children()

        elif (inpt == "1"):
            current_directory = current_directory.change_directory()




def printMenu(current):
    print("Current directory: " + current.data)
    #current.list_children()
    print("[1] Change Directory")
    print("[2] Add Folder")
    print("[3] Add files")
    print("[4] List Items in Directory")
    print()
    print("[0] Exit")



class Node:
    def __init__(self, data, file=False, parent=None):
        self.data = data #name of folder/file
        self.children = []
        self.file = file
        self.parent = parent

    def add_child(self, data, file=False):
        child = Node(data, file, parent=self)
        self.children.append(child)
        return child

    def list_children(self):
        if not self.children:
            print(f"{self.data} is empty.")
        else:
            count = 1
            print(f"Contents of {self.data}:")
            for child in self.children:
                if child.file:
                    print(f"{count} -  [File] {child.data}")
                else:
                    print(f"{count}  [Dir ] {child.data}")
                count = count+1

    def change_directory(self):
        if self.file:
            print("Cannot change directory from a file.")
            return self

        # show menu
        self.list_children()
        print()
        if self.parent is None:
            print("[0] - No parent (at root)")
        else:
            print(f"[0] - .. (go to {self.parent.data})")

        # prompt & validate
        while True:
            sel = input("Select the directory number: ").strip()

            if not sel.isdigit():
                print("Please enter a number.")
                continue

            sel = int(sel)

            # go up
            if sel == 0:
                if self.parent is None:
                    print("Already at root.")
                    return self
                return self.parent

            # go into child (1-based to 0-based)
            if 1 <= sel <= len(self.children):
                child = self.children[sel - 1]
                if child.file:
                    print("That item is a file; cannot cd into a file.")
                    continue
                return child

            print("No such index. Try again.")








if __name__ == "__main__":
    main()
