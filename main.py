def main():


    current_directory = "root"
    #printMenu(current_directory)

    inpt = -1

    root = Node("Root", False)

    root.add_child("Desktop", False)
    root.add_child("Downloads", False)
    root.add_child("Documents", False)



    while(inpt != "0"):

        printMenu(current_directory)
        inpt = input()


        if(inpt == "2"):
            name = input("Input the name of the folder you would like to add")
            root.add_child(name, False)
            print(name + " folder was added successfully")

        elif (inpt == "4"):
            root.list_children()


def printMenu(current):
    print(current)
    print("[1] Change Directory")
    print("[2] Add Folder")
    print("[3] Add files")
    print("[4] List Items in Directory")
    print()
    print("[0] Exit")



class Node:
    def __init__(self,data, file):
        self.data = data #name of folder/file
        self.children = []
        self.file = False

    def add_child(self, data, file):
        child = Node(data, file)
        self.children.append(child)
        return child

    def list_children(self):
        if not self.children:
            print(f"{self.data} is empty.")
        else:
            print(f"Contents of {self.data}:")
            for child in self.children:
                if child.file:
                    print(f"  [File] {child.data}")
                else:
                    print(f"  [Dir ] {child.data}")





if __name__ == "__main__":
    main()
