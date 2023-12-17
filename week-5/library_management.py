from datetime import datetime
class Book:
    def __init__(self,title,author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
    def display_bookinfo(self):
        print("""
              Book Title: {self.title}
              Book author: {self.author}
              Book id : {self.isbn}
              Book availability: {self.availability}
              """)
    def update(self, availability):
        self.availability = availability
class User:
    def __init__(self,user_id,name,books_borrowed):
        self.user_id  = user_id
        self.name = name
        self.books_borrowed = []
        self.books_returned = []
    def display_userinfo(self):
        print( f"User id no: {self.user_id}")
        print(f"User name: {self.name}")
        print(f"borrowed book : {self.books_borrowed}")
        
        
    def borrow_book(self,book):
        self.books_borrowed.append(book)
        book.update("Not Available")
    def return_book(self, book):
        self.books_borrowed.remove(book)
        self.books_returned.append(book)
        book.update("Available")
class Library:
    def __init__(self):
        self.users = []
        self.books=[]
        self.transactions = []
    def add_book(self,book):
        self.books.append(book)
    def register_user(self,user):
        self.users.append(user)
    def view_books(self):
        for book in self.books:
            book.display()
    def view_users(self):
        for user in self.users:
            user.display()
    def return_transaction(self,user,book):
        if book in user.books_borrowed:
            user.return_book(book)
        else:
            print(f"You don't have {book} borrowed")
class Transaction:
    def __init__(self, user, book, date, type):
        self.user = user
        self.book = book
        self.date = date
        self.type = type
    @classmethod
    def record_transaction(cls, user, book, library):
        if book.availability == "Available":
            transaction = cls(user, book, datetime.now(), "Borrow")
            library.transactions.append(transaction)
            user.borrow_book(book)
        else:
            transaction = cls(user, book, datetime.now(), "Return")
            library.transactions.append(transaction)
            user.return_book(book)
    @classmethod
    def transaction_report(cls, library):
        for transaction in library.transactions:
            print(f"Date: {transaction.date}")
            print(f"User: {transaction.user.name}")
            print(f"Book: {transaction.book.title}")
            print(f"Type: {transaction.type}")
def main():
    book1 = Book("Book 1","Author 1","123")
    book2 = Book("Book 2","Author 2","345")
    
    user1 = User("1","User1") 
    user2 = User("2","User 2")
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.register_user(user1)
    library.register_user(user2)
    
    Transaction.record_transaction(user1, book1, library)
    Transaction.record_transaction(user2, book2, library)
    library.borrow_transaction(user1,book1)
    library.borrow_transaction(user2,book2)
    library.return_transaction(user1,book1)
    
    Transaction.transaction_report(library)
   
   
    
    while True:
        print("Library management System")
        print("1. View Books")
        print("2. view Users")
        print("3. exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            library.view_books()
        elif choice == 2:
            library.view_users()
        else:
            break
        if __name__ == '__main__':
            main()
    
           
        
        
