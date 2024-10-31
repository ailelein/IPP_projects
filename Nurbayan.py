# This project is related to EMenu, where people can check the available dishes and their prices before going to the restaurant. the address and meal time can be chosen. After that, the total price including the drinks will be shown to customers

# Данные филиалов кафе "Нават" с меню
branches = {
    "ул. Токтогула, 123": {
        "breakfast": {"сырники": 180, "овсянка": 160},
        "lunch": {"шорпо": 320, "жаркое с мясом": 390},
        "dinner": {"овощной салат": 250, "шашлык": 400}
    },
    "ул. Исанова, 45": {
        "breakfast": {"гренки с джемом": 140, "йогурт с фруктами": 150},
        "lunch": {"солянка": 310, "манты": 280},
        "dinner": {"греческий салат": 280, "спагетти карбонара": 390}
    },
    "ул. Абдрахманова, 67": {
        "breakfast": {"блины с мёдом": 190, "фриттата": 170},
        "lunch": {"суп-харчо": 330, "долма": 260},
        "dinner": {"салат цезарь": 290, "рыба на гриле": 450}
    }
}

# Данные напитков
drinks = {"компот": 60, "чай": 40, "мохито": 80, "капучино": 120}

# 1. Выбор филиала
print("Филиалы кафе 'Нават':")
for num, branch in enumerate(branches, 1):
    print(f"{num}. {branch}")
branch_num = int(input("Выберите филиал (введите номер): "))
selected_branch = list(branches.keys())[branch_num - 1]

# 2. Выбор времени приема пищи
print("\nВремя приема пищи:")
meal_times = list(branches[selected_branch].keys())
for num, meal in enumerate(meal_times, 1):
    print(f"{num}. {meal.capitalize()}")
meal_choice = int(input("Выберите время приема пищи (введите номер): "))
selected_meal = meal_times[meal_choice - 1]

# 3. Выбор блюда
print(f"\nМеню на {selected_meal.capitalize()}:")
menu = branches[selected_branch][selected_meal]
for dish, price in menu.items():
    print(f"{dish} - {price} сом")
dish_choice = input("Введите название блюда: ")
dish_price = menu.get(dish_choice, 0)

# Спрашиваем количество порций
quantity = int(input("Введите количество порций: "))
total_dish_price = dish_price * quantity

# 4. Выбор напитка
print("\nНапитки:")
for drink, price in drinks.items():
    print(f"{drink} - {price} сом")
drink_choice = input("Введите название напитка: ")
drink_price = drinks.get(drink_choice, 0)

# Спрашиваем количество напитков
drink_quantity = int(input("Введите количество напитков: "))
total_drink_price = drink_price * drink_quantity

# 5. Расчет общей стоимости и вывод чека
total_price = total_dish_price + total_drink_price
print("\n--- Ваш чек ---")
print(f"Филиал: {selected_branch}")
print(f"{dish_choice} - {dish_price} сом x {quantity} = {total_dish_price} сом")
print(f"{drink_choice} - {drink_price} сом x {drink_quantity} = {total_drink_price} сом")
print(f"Общая сумма: {total_price} сом")
print("Спасибо за заказ!")

