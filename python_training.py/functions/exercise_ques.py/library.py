class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Title : {self.title}, Author : {self.author}, ISBN : {self.isbn}")

    def written(self, author_name):
        return self.author.lower() == author_name.lower()
    
Books = book("Mistaken Man", "George C.", "12345567890")
Books.display()
print(Books.written("George"))
print(Books.written("Rowling"))
print(Books.written("George C."))