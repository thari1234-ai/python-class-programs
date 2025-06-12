class Cosmetics:
    def __init__(self, name="", brand="", price=0, category=""):
        self.name = name
        self.brand = brand
        self.price = price
        self.category = category

    def display_info(self):
        print("Product Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Category:", self.category)
product1 = Cosmetics("Lipstick", "Maybelline", 250, "Makeup")
product1.display_info()