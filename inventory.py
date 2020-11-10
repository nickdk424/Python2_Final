import csv

class Product :

        def __init__(self, name, price, id, quantity):
            self.__name = name
            self.__price = price
            self.__id = id
            self.__quantity = quantity

        def get_name(self):
            return self.__name
        
        def get_total(self):
            qty = float(self.__quantity)
            pr = float(self.__price)
            return pr * qty

        def get_info(self):
            print(f"{self.__id}\t\t{self.__name}\t\t\t{self.__price}\t\t{self.__quantity}\t\t${self.get_total():.2f}")

class Book(Product):

    def __init__(self, name, price, id, quantity, author):
        self.__author = author
        super().__init__(name, price, id, quantity)

    def get_description(self):
        return super().get_name() + ' by ' + self.__author

class Movie(Product):
    def __init__(self, name, price, id, quantity, genre, year):
        self.__genre = genre
        self.__year = year
        super().__init__(name, price, id, quantity)

    def get_description(self):
        return f"{super().get_name()}\nGenre: {self.__genre}\nYear: {self.__year}"

products = []

with open('inventory_table.csv', "r") as data_file:
    csv_data = csv.reader(data_file)

    for row in csv_data:
        if len(row) == 5:
            products.append(Book(row[0], row[1], row[2],row[3], row[4]))
        elif len(row) == 6:
            products.append(Movie(row[0], row[1], row[2],row[3], row[4], row[5]))
        # else:
        #     products.append(Product(row[0], row[1], row[2], row[3]))
    
 
def menu():
    print("Product Inventory Program")
    print("1. Show all products")
    print("2. Add a product")
    print("3. Update a product")
    print("4. Delete a product")
    print("5. Exit")
    print("Please enter your choice")
    choice = input(">>> ")

def show_all_products():
    print("PRODUCT ID\tNAME\t\t\t\t\tPRICE\t\tQTY\t\tTOTAL")
    print("="*100)
    for item in products:
        print(item.get_info())

def add_product():
    print("Please choose to add 1 or 2:\n1. Book\n2.Movie")
    choose = int(input(">>> "))
    if choose == 1:
        print("Please input item #")
        book_num = input(">>> ")
        print("Input item name")
        book_name = input(">>> ")
        print("Input price")
        book_price = input(">>> ")
        print("Input quantity")
        book_qty = input(">>> ")
        print("Enter Author")
        book_author = input(">>> ")
        book = Book(book_name, book_price, book_num, book_qty, book_author)
        products.append(book)
        out_csv_file = open("inventory_table.csv", "w", newline = '')
        csv_out = csv.writer(out_csv_file)
        csv_out.writerows(item)
        out_csv_file.close()
    elif choose == 2:
        print("Please input item #")
        movie_num = input(">>> ")
        print("Input item name")
        movie_name = input(">>> ")
        print("Input price")
        movie_price = input(">>> ")
        print("Input quantity")
        movie_qty = input(">>> ")
        print("Enter Genre")
        movie_genre = input(">>> ")
        print("Enter Year")
        movie_year = input(">>> ")
        products.append(Movie(movie_name, movie_price, movie_num, movie_qty, movie_genre, movie_year))


add_product()
show_all_products()

