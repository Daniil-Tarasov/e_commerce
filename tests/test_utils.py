from unittest.mock import patch, mock_open

from src.utils import read_json, create_objects_from_json


@patch("builtins.open", new_callable=mock_open, read_data='[{"name": "Смартфоны", "description": "Samsung"}]')
def test_read_json(mock_file):
    data = read_json('data/products.json')
    assert data == [{"name": "Смартфоны", "description": "Samsung"}]


def test_create_objects_from_json():
    result = create_objects_from_json([
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }]}])
    assert result[0].name == "Смартфоны"
