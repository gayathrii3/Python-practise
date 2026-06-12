class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):   #for printing the string obj
        return f"{self.title} is written by {self.author}"
    
    def __eq__(self, other):             #to compare attributes in objects
        return self.author == other.author
        
    def __lt__(self, other):           #less than ( __gt__ for greater than)
        return self.num_pages < other.num_pages
    
    def __contains__(self, keyword):     #checks if a word is present or not
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        if key == 'author':
            return self.author


book1 = Book("The Mistake", "Chloe Walsh", 315)
book2 = Book("Binding 13", "Chloe Walsh", 285)
book3 = Book("The Love Hypothesis", "Ali Hazelwood", 219)

# print(book1.num_pages)
print(book2)                            #----- not possible(use  dunder string)
# print(book1 == book2)
# print(book2 < book3)
# print("Love" in book3)
print(book1['title'])
