#project about counting/selling reports. At the end of the day, the seller will upload products with "name", "price", "and amount". The program will calculate the final price and add the data to the Txt file


import datetime

products = {
    'доска': 100,
    'балка': 250,
    'бревно': 300,
    'плита': 150
}

sales = []

def log_to_file(message):
    with open('log.txt', 'a', encoding='utf-8') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

def add_or_update_product(name, price):
    if name in products:
        old_price = products[name]
        if old_price != price:
            products[name] = price
            message = f"Товар '{name}' уже существует. Цена обновлена с {old_price} сом. на {price} сом."
        else:
            message = f"Товар '{name}' уже существует. Цена осталась прежней: {old_price} сом."
    else:
        products[name] = price
        message = f"Товар '{name}' добавлен с ценой {price} сом."
    
    print(message)
    log_to_file(message)

def add_sale(product_name, quantity):
    if product_name not in products:
        message = f"Товар '{product_name}' не найден."
        print(message)
        log_to_file(message)
        return

    sale_amount = products[product_name] * quantity
    sales.append({'product': product_name, 'quantity': quantity, 'total': sale_amount})
    message = f"Продано {quantity} шт. '{product_name}' на сумму {sale_amount} сом."
    print(message)
    log_to_file(message)

def view_sales():
    message = "\nВсе продажи:"
    print(message)
    log_to_file(message)
    for sale in sales:
        message = f"{sale['quantity']} шт. '{sale['product']}' - {sale['total']} сом."
        print(message)
        log_to_file(message)

def total_revenue():
    total = sum(sale['total'] for sale in sales)
    message = f"\nОбщая выручка: {total} сом."
    print(message)
    log_to_file(message)
    
    separator = "-" * 40
    print(separator)
    log_to_file(separator)

add_or_update_product('фанера', 250)
add_or_update_product('гвоздь', 300)
add_or_update_product('доска', 120)  
add_or_update_product('балка', 250)
add_sale('фанера', 10)
add_sale('балка', 3)
add_sale('гвоздь', 3)
add_sale('доска', 2)

view_sales()
total_revenue()
