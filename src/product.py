class Product:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product, products=None):
        if products:
            for product in products:
                if product.name == dict_product["name"]:
                    product.quantity += dict_product["quantity"]
                    product.price = max([product.price, dict_product["price"]])
                    return product
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if price < self.__price:
            check_input = input("Изменять цену? Введите y если да,и n если нет.\n")
            if check_input != "y":
                return
        self.__price = price


# if __name__ == "__main__":
#     product1 = Product('Samsung', "256GB", 10000.0, 5)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     product2 = Product.new_product('IPhone', "256GB", 10000.0, 5)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     product2.price = 0.0
