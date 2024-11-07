def test_product_init(first_product):
    assert first_product.name == "Сыр"
    assert first_product.description == "Сыр с плесенью"
    assert first_product.price == 100.50
    assert first_product.quantity == 3
