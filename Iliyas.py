import os
import hashlib
from typing import Any

books_db = [
    {"title": "Кыргыз тили", "copies": 3},
    {"title": "Математика", "copies": 2},
    {"title": "Физика", "copies": 1}
]

users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            for line in file:
                username, name, user_type, password = line.strip().split(",")
                users_db[username] = {"name": name, "type": user_type, "password": password}

def register_user():
    name = input("Атыңызды жана фамилияңызды киргизиңиз: ")
    username = input("Колдонуучу атын киргизиңиз: ").strip()
    password = input("Паролду киргизиңиз: ").strip()
    user_type = input("Сиз мугалимсизби же студент? (мугалим/студент): ").strip().lower()

    if user_type not in ["мугалим", "студент"]:
        print("Туура эмес киргизүү. Мугалим же студент катары катталыңыз.")
        return register_user()

    if username in users_db:
        print("Бул колдонуучу аты мурда эле колдонулган.")
    else:
        hashed_password = hash_password(password)
        users_db[username] = {"name": name, "type": user_type, "password": hashed_password}
        with open("users.txt", "a") as file:
            file.write(f"{username},{name},{user_type},{hashed_password}\n")
        print(f"{name} ийгиликтүү катталды!")

def login_user():
    username = input("Колдонуучу атын киргизиңиз: ").strip()
    password = input("Паролду киргизиңиз: ").strip()

    if username in users_db and users_db[username]["password"] == hash_password(password):
        print(f"Кош келдиңиз, {users_db[username]['name']}!")
        return users_db[username]
    else:
        print("Колдонуучу аты же паролу туура эмес.")
        return None

def search_book(book_title):
    for book in books_db:
        if book["title"].lower() == book_title.lower():
            return book
    return None

def borrow_book(user, book):
    if book["copies"] > 0:
        confirm = input(f"'{book['title']}' китебин алууга уруксат бересизби? (ооба/жок): ").strip().lower()
        if confirm == "ооба":
            book["copies"] -= 1
            save_borrow_info(user, book)
            print(f"{user['name']} '{book['title']}' китебин алды.")
        else:
            print("Китеп алуудан баш тарттыңыз.")
    else:
        print(f"'{book['title']}' китеби жеткиликтүү эмес.")

def save_borrow_info(user, book):
    with open("borrowed_books.txt", "a") as f:
        f.write(f"Колдонуучу: {user['name']}, Статус: {user['type']}, Китеп: {book['title']}\n")

def return_book(user):
    try:
        with open("borrowed_books.txt", "r") as f:
            borrowed_books = f.readlines()
    except FileNotFoundError:
        print("Сизде алынган китептер жок.")
        return

    user_books = [line for line in borrowed_books if user['name'] in line]
    if not user_books:
        print("Сизде алынган китептер жок.")
        return

    print("\nСиз алган китептер:")
    for i, entry in enumerate(user_books, start=1):
        print(f"{i}. {entry.strip()}")

    try:
        choice = int(input("Кайтарыла турган китептин номерин киргизиңиз: ")) - 1
        if 0 <= choice < len(user_books):
            book_title = user_books[choice].split("Китеп: ")[1].strip()
            book = search_book(book_title)
            if book:
                book["copies"] += 1
                borrowed_books.remove(user_books[choice])
                with open("borrowed_books.txt", "w") as f:
                    f.writelines(borrowed_books)
                print(f"'{book_title}' китеби ийгиликтүү кайтарылды.")
            else:
                print("Китеп базадан табылган жок.")
        else:
            print("Туура эмес тандоо.")
    except ValueError:
        print("Туура эмес киргизүү.")

def check_library_database():
    print("\n--- Китепканадагы Китептердин Базасы ---")
    if books_db:
        for book in books_db:
            print(f"Китеп: {book['title']}, Көчүрмөлөр: {book['copies']}")
    else:
        print("Китепканада китептер жок.")

def main():
    print("Китепкана системасына кош келиңиз!")
    load_users()

    while True:
        print("\nБашкы болум:")
        print("1. Китепканага катталуу")
        print("2. Жеке коб. кируу")
        action = input("Тандооңузду киргизиңиз:").strip()

        if action == '1':
            register_user()
            break

        elif action == '2':
            user: Any | None = login_user()
            if user:
                break

        else:
            print("Туура эмес тандоо. Катталуу же кирүү номерин киргизиңиз.")

    while True:
        print("\nМеню:")
        print("1. Китеп издөө жана алуу")
        print("2. Китепкана базасын текшерүү")
        print("3. Китепти кайтаруу")
        print("4. Кайра башкы болум")

        тандоо = input("Тандооңузду киргизиңиз: ")

        if тандоо == '1':
            book_title = input("Кандай китеп керек? (чыгуу үчүн 'чыг' деп жазыңыз): ")
            if book_title.lower() == "чыг":
                continue

            book = search_book(book_title)
            if book:
                borrow_book(user, book)
            else:
                print(f"'{book_title}' китеби китепканабызда жок.")

        elif тандоо == '2':
            check_library_database()

        elif тандоо == '3':
            return_book(user)

        elif тандоо == '4':
            print("Кайра катталуу же кирүү функциясына кайтып жатасыз...")
            main()

        else:
            print("Туура эмес тандоо. Менюдан номер киргизиңиз.")


if __name__ == "__main__":
    main()
