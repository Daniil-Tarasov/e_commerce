# from src.category import Category
# from src.product import Product


class CategoryIterator:

    def __init__(self, obj_category):
        self.category = obj_category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# if __name__ == '__main__':
#     product1 = Product('Samsung', "256GB", 10000.0, 5)
#     product2 = Product('IPhone', "256GB", 100000.0, 2)
#     product3 = Product('Lenovo', "256GB", 10000.0, 5)
#     product4 = Product('Asus', "256GB", 10000.0, 5)
#
#     category = Category('Смартфоны', "Смартфоны", [product1, product2, product3, product4])
#
#     iterator = CategoryIterator(category)
#
#     for product in iterator:
#         print(product)
