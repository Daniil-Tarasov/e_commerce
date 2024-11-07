class Category:
    name: str
    description: str
    products: list
    count_of_categories = 0
    count_of_products = 0
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.count_of_products = len(products) if products else 0
        Category.count_of_categories += 1

if __name__ == '__main__':
    category = Category('Молочные продукты', "Сыр с плесенью")

    print(category.name)
    print(category.description)
    print(category.products)
    print(category.count_of_categories)
    print(category.count_of_products)
