# importing a class from another file or directory

# way 1
# from file_name import class_name

from code5_book import Book

book1 = Book("Opekkha", "Humayun Ahmed")

book1.details()


# Alternative 2
# import file_name
import code5_book

book2 = code5_book.Book("Boss","Rajo")

#to access the Book class, I have to access it 
#by refrencing through the filename code5_book
# file_name.class_name

#but in way 1, I don't need to reference by the file_name since I imported the class directly from the file_name i.e from code5_book import Book

book2.details()



# example of aliasing 

import code5_book as b
# here as b is the part of aliasing , 
# now I can access code5_book just by typing b

book3 = b.Book("Amazing","syed faysel")
book3.details()







