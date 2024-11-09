from src.product import Product


class Category:
    name: str
    description: str
    products: list
    count_of_categories = 0
    count_of_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.count_of_products += len(products) if products else 0
        Category.count_of_categories += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.count_of_products += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_str

    @property
    def products_list(self):
        return self.__products

# if __name__ == "__main__":
#     product1 = Product('Samsung', "256GB", 10000.0, 5)
#     product2 = Product('IPhone', "256GB", 10000.0, 5)
#     product3 = Product('Lenovo', "256GB", 10000.0, 5)
#     product4 = Product('Asus', "256GB", 10000.0, 5)
#
#     category = Category('Смартфоны', "Смартфоны", [product1, product2, product3, product4])
#
#     print(category.products)
#     print(category.count_of_products)


