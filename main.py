class Library:
    listOfBooks=[]
    lendDict={}
    
    
    
    def __init__(self,listOfBooks,nameOfLibrary):
        self.listOfBooks = listOfBooks
        self.nameOfLibrary=nameOfLibrary
        print(f"Welcome To  {self.nameOfLibrary}'s Libary \n  ")
        
    def addbook(self):
        nameOfBook=input("Enter name of book you want to add:   ")
        self.listOfBooks.append(nameOfBook)
        print("The Book was added successfuly !! \n \t Thank you !")
    
    
    
    def lendbook(self):
        for books in self.listOfBooks:
            print(books)
        name =input("Enter your Name :  ")
        book= input ("Enter name of book you want to read : ")
        if book in self.listOfBooks:
            Library.lendDict[book]=name
            self.listOfBooks.remove(book)
            print(f"You own {book} now \n please return after reading  ")
        elif book in Library.lendDict:
            print(f" {Library.lendDict.get(book)} owned this book")
        else:
            print("please enter a valid book")
    
    def returnBook(self):
        rname=input("enter your name: ")
        if rname in Library.lendDict:
            returnBook=input("Enter name of book you want to return:   ")
            Library.lendDict.pop(returnBook)
            print("Book was returned succesfuly !!!\n Thank you!!")
        else:
            print("you dont own any book")
    
        
        
        
if __name__=='__main__':
    mystic=Library(['python','c++','abc'],'mystic')

    while True:
        print (f"--------------------------------\n \n \n \n \nWelcome to {mystic.nameOfLibrary}'s Library \nWhat do you wan to do ")
        userInput=int (input("1. Lend Book   \n2. Return Book \n3. Add Book \n4.Quit \n(only enter their Sr no.)\n"))
        if userInput==1:
            mystic.lendbook()
            
            
        elif userInput==2:
            mystic.returnBook()
        elif userInput==3:
            mystic.addbook()
        elif userInput==4:
            print("Thank you for visiting !!")
            break
        else:
            print("please enter a valid option")
