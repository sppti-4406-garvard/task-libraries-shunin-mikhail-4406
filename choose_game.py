import random


def generate_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Введите число от 1 до 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Число должно быть в диапазоне от 1 до 100. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

def check_guess(guess, target):
    if guess < target:
        print("Слишком мало!")
        return False
    elif guess > target:
        print("Слишком много!")
        return False
    else:
        print("Поздравляю! Вы угадали число!")
        return True

def play_game():
    target_number = generate_number()
    attempts = 7
    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У вас есть {attempts} попыток, чтобы угадать его.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}.")
        guess = get_user_guess()
        if check_guess(guess, target_number):
            break
        elif attempt == attempts:
            print(f"\nВы исчерпали все попытки. Загаданное число было: {target_number}")
            break