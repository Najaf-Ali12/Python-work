class Book:
    title="You can win"
    author="Shive khara"
    publication_year=2024
    Genre="Motivational"
    status="available"
    def displayBookInfo(self):
        print("title",self.title)
        print("Author: ",self.author)
        print("Publication Year: ",self.publication_year)
        print("Genre: ",self.Genre)
        print("Status: ",self.status)
    def BorrowBook(self,booktitle):
        if self.title==booktitle:
            if self.status=="available":
                borrower=input("Enter the name of borrower: ")
                self.status="not available"
                print(self.title,"is borrowed by",borrower)
                return borrower
            else:
                print("The book is already borrowed")
        else:
            print("There is no book with such a title")
    def ReturnBook(self,booktitle):
        if self.title==booktitle:
            if self.status=="not available":
                print("Book is returned by successfully")
                self.status="available"
            else:
                print("The book is available and was not borrowed")
        else:
            print("The book never existed in the library")
object=Book()
print("\3 \3 \3 \3 Welcome to Book Management System \3 \3 \3 \3")
while (True):
    print("Menu")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Display Book Information")
    print("4. Exit")
    choice=input("Enter your choice(1,2,3 or 4): ")
    if choice=="1":
        title=input("Enter the title of book that you want to borrow: ")
        object.BorrowBook(title)
    elif choice=="2":
        title=input("Enter the title of book that you want to return: ")
        object.ReturnBook(title)
    elif choice=="3":
        object.displayBookInfo()
    elif choice=="4":
        print("Thanks a lot to use our service")
        break
    else:
        print("Invalid Choice. Please select a valid choice")