#This project is a Flowershop account platform. By the end of the day, it will give the total number of sold flowers and the total price


flower_prices = {
    'роза': 150,
    'тюльпан': 90,
    'орхидея': 200,
    'гвоздика': 100
}

sales_log = []


def flower_shop(action, flower_name=None, price=None, quantity=None):
    if action == "каталог":
        print("Каталог цветов:")
        for flower, price in flower_prices.items():
            print(f"{flower.capitalize()}: {price} сом за штуку")
    elif action == "добавить_цветок":
        if flower_name in flower_prices:
            print(f"Цветок '{flower_name}' уже существует.")
        else:
            flower_prices[flower_name] = price
            print(f"Добавлен цветок '{flower_name}' с ценой {price} за штуку.")
    elif action == "продажа":
        if flower_name in flower_prices:
            sale_total = flower_prices[flower_name] * quantity
            sales_log.append({'flower': flower_name, 'quantity': quantity, 'total': sale_total})
            print(f"Продано {quantity} шт. '{flower_name}' на сумму {sale_total} сом.")
        else:
            print(f"Цветок '{flower_name}' не найден в каталоге.")
    elif action == "журнал_продаж":
        print("Журнал продаж:")
        for sale in sales_log:
            print(f"{sale['quantity']} шт. '{sale['flower']}' - {sale['total']} сом.")
    elif action == "общая_выручка":
        total_revenue = sum(sale['total'] for sale in sales_log)
        print(f"Общая выручка: {total_revenue} сом.")


while True:
    action = input(
        "\nВыберите действие (каталог, добавить_цветок, продажа, журнал_продаж, общая_выручка, выход): ").strip()

    if action == "выход":
        print("Работа завершена.")
        break

    if action == "каталог":
        flower_shop(action)

    elif action == "добавить_цветок":
        flower_name = input("Введите название цветка: ").strip()
        try:
            price = int(input("Введите цену цветка: ").strip())
            flower_shop(action, flower_name=flower_name, price=price)
        except ValueError:
            print("Ошибка: Цена должна быть числом.")

    elif action == "продажа":
        flower_name = input("Введите название цветка для продажи: ").strip()
        try:
            quantity = int(input("Введите количество для продажи: ").strip())
            flower_shop(action, flower_name=flower_name, quantity=quantity)
        except ValueError:
            print("Ошибка: Количество должно быть числом.")

    elif action == "журнал_продаж":
        flower_shop(action)

    elif action == "общая_выручка":
        flower_shop(action)

    else:
        print("Некорректное действие. Попробуйте снова.")
