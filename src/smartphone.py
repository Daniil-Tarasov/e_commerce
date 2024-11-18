from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# if __name__ == "__main__":
#     product1 = Smartphone('Samsung', "256GB", 10000.0, 5, 'Exynos', 'S24', '8', 'Gray')
#     product2 = Product('IPhone', "256GB", 100000.0, 5)
#     product3 = Smartphone('IPhone', "256GB", 100000.0, 5, "Test", "15 Pro", '16', 'Red')
#
#     print(product3 + product1)

