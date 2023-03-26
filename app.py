class Book:
    def __init__(self, name: str, pages: int, description: str, price: float):
        self.name: str = name
        self.pages: int = pages
        self.description: str = description
        self.price: float = price

    def __repr__(self) -> str:
        book_dict = {
            "name": f"{self.name}",
            "pages": f"{self.pages}",
            "description": f"{self.description}",
            "price": f"{self.price}",
        }
        return str(book_dict)


book1 = Book("crap", 45, "nice book right", 15.2)

print(book1)
