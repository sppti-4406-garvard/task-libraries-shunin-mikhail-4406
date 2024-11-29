import random

def choose_word():
    words = ["python", "programming", "hangman", "developer", "function", "variable", "syntax", "algorithm"]
    return random.choice(words)

def display_game_state(word, guessed_letters, attempts_left):
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("\nСлово:", " ".join(display_word))
    print(f"Угаданные буквы: {', '.join(sorted(guessed_letters))}")
    print(f"Осталось попыток: {attempts_left}")

def get_user_guess(guessed_letters):
    while True:
        guess = input("Введите букву (или 'выход' для завершения игры): ").strip().lower()
        if guess == "выход":
            return None
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже вводили эту букву. Попробуйте снова.")
            else:
                return guess
        else:
            print("Некорректный ввод. Введите одну букву.")

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6
    print("Добро пожаловать в игру 'Виселица'!")
    print(f"Загадано слово из {len(word)} букв. У вас есть {attempts_left} попыток.")

    while attempts_left > 0:
        display_game_state(word, guessed_letters, attempts_left)
        guess = get_user_guess(guessed_letters)

        if guess is None:  # Пользователь выбрал выйти
            print("Вы завершили игру. Спасибо за игру!")
            return

        guessed_letters.add(guess)

        if guess in word:
            print(f"Верно! Буква '{guess}' есть в слове.")
            if all(letter in guessed_letters for letter in word):
                print(f"\nПоздравляем! Вы угадали слово: {word}")
                return
        else:
            attempts_left -= 1
            print(f"Неверно! Буквы '{guess}' нет в слове.")
            if attempts_left == 0:
                print(f"\nВы проиграли. Загаданное слово было: {word}")