#This project is called "Game Platform", where people can choose one of the available games and play from the terminal. Currently, there are 3 games. And you can try it now!!!!!


import random
# Камень, ножницы, бумага
def rock_paper_scissors():
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        user_choice = input("Ваш выбор (камень, ножницы, бумага): ")
        if user_choice not in choices:
            print("Некорректный выбор. Пожалуйста, выберите: камень, ножницы или бумага.")
            continue
        computer_choice = random.choice(choices)
        print(f"Компьютер: {computer_choice}")

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "камень" and computer_choice == "ножницы") or \
                (user_choice == "ножницы" and computer_choice == "бумага") or \
                (user_choice == "бумага" and computer_choice == "камень"):
            print("Вы победили!")
        else:
            print("Вы проиграли.")

        play_again = input("Сыграть еще раз? (да/нет): ")
        if play_again == "нет":
            break
# Виселица
def hangman():
    from random import choice

    hangman = (
        """
          _____
         |     |
         |
         |
         |
         |_____
        """,
        """
          _____
         |     |
         |     O
         |
         |
         |_____
        """,
        """
          _____
         |     |
         |     O
         |     |
         |
         |_____
        """,
        """
          _____
         |     |
         |     O
         |    /|
         |
         |_____
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |
         |_____
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |    /
         |_____
        """,
        """
          _____
         |     |
         |     O
         |    /|\\
         |    / \\
         |_____
        """
    )

    maxWrong = len(hangman) - 1
    words = ("python", "elephant", "astronomy", "guitar", "chocolate")
    word = choice(words)
    line = '_' * len(word)
    wrong = 0
    used = []

    while wrong < maxWrong and line != word:
        print(hangman[wrong])
        print("\nВы использовали буквы:\n", used)
        print('\nНа данный момент слово выглядит так:\n', line)

        guess = input('\nВведите букву: ').lower()

        while guess in used:
            print('Вы уже использовали букву', guess)
            guess = input('Введите букву: ')

        used.append(guess)

        if guess in word:
            print("Да, буква", guess, 'есть в слове.')
            new = ''
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += line[i]
            line = new
        else:
            print("Извините, буквы '" + guess + "' нет в слове.")
            wrong += 1

    if wrong == maxWrong:
        print(hangman[wrong])
        print("\nВы проиграли! Загаданное слово было: \"" + word + "\"")
    else:
        print(hangman[-1])
        print('\nПоздравляем! Вы угадали слово: "' + word + '"')

# Словесный миксер
def word_scramble():
    words = ["python", "computer", "program", "developer", "challenge"]
    word = random.choice(words)
    scrambled_word = ''.join(random.sample(word, len(word)))

    print("Добро пожаловать в игру 'Словесный миксер'!")
    print("Угадайте слово:", scrambled_word)

    attempts = 3
    while attempts > 0:
        guess = input("Ваш ответ: ")
        if guess == word:
            print("Поздравляем! Вы угадали слово.")
            break
        else:
            attempts -= 1
            print(f"Неправильно. Осталось попыток: {attempts}")

    if attempts == 0:
        print(f"Вы проиграли. Загаданное слово было: {word}")


# Платформа
def main():
    print("Добро пожаловать на игровую платформу!")
    while True:
        print("\nВыберите игру:")
        print("1. Камень, ножницы, бумага")
        print("2. Виселица")
        print("3. Словесный миксер")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            hangman()
        elif choice == "3":
            word_scramble()
        elif choice == "0":
            print("Спасибо за игру! До встречи!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите номер игры.")
# def run_game():
#     main()

main()
