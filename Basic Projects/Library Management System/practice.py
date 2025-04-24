# library = {
#     "Book1": {
#         "author": "Author One",
#         "publication_year": 2001,
#         "status": "available"
#     },
#     "Book2": {
#         "author": "Author Two",
#         "publication_year": 2002,
#         "status": "available"
#     },
#     "Book3": {
#         "author": "Author Three",
#         "publication_year": 2003,
#         "status": "available"
#     }
# }

# book = input("Name of book: ")
# details = f"""
# Details of '{book}': 
#     Author: {library[book]["author"]}  
#     Publication Year: {library[book]["publication_year"]}
# """
# print(details)

# a = input("A: ")
# print(a.isspace())

publication_year = input("Enter the publication year: ")
while publication_year.isnumeric == False:
    publication_year = input("Invalid input. Enter the publication year: ")

print(publication_year)
