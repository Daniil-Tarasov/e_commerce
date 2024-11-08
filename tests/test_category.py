def test_category_init(for_category):
    assert for_category.name == "Молочные продукты"
    assert for_category.description == "Сыр с плесенью"
    assert for_category.products == ["Сыр 1", "Сыр 2", "Сыр 3"]
    assert for_category.count_of_categories == 1
    assert for_category.count_of_products == 3


def test_category_empty_products(for_category_empty_product):
    assert for_category_empty_product.count_of_products == 3
    assert for_category_empty_product.count_of_categories == 2
