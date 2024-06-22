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

# Создание магазинов
store1 = Store("Магазин Продукты", "ул. Ленина, 15")
store2 = Store("Хоз. товары", "ул. Мира, 20")
store3 = Store("Книжный Дом", "ул. Пушкина, 10")

# Добавление товаров в магазин Продукты
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)
store1.add_item("Молоко", 1.2)

# Добавление товаров в магазин Хоз. товары
store2.add_item("Салфетки", 20)
store2.add_item("Смеситель", 2300)
store2.add_item("Швабра", 350)

# Добавление товаров в магазин Книжный Дом
store3.add_item("книга1", 10)
store3.add_item("книга2", 15)
store3.add_item("журнал", 5)

# Вывод информации о магазинах
print(store1)
print(store2)
print(store3)

# Обновление и удаление товаров
store1.update_price("Яблоки", 0.6)
store2.remove_item("Швабра")
store3.update_price("журнал", 4)

# Получение цен на товары
print(f"Цена на Яблоки в магазине Продукты: {store1.get_price('Яблоки')}")
print(f"Цена на Смеситель в магазине Хоз. товары: {store2.get_price('Смеситель')}")
print(f"Цена на журнал в магазине Книжный Дом: {store3.get_price('журнал')}")