class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из ассортимента")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте")

# Пример использования:
store = Store("Магазин Продукты", "ул. Ленина, 15")

# Добавление товаров
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)

# Удаление товара
store.remove_item("bananas")

# Получение цены товара
price = store.get_price("apples")
print(f"Цена на apples: {price}")

# Обновление цены товара
store.update_price("apples", 0.6)

# Проверка обновлённой цены
price = store.get_price("apples")
print(f"Новая цена на apples: {price}")