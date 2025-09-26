import random

def show_history(attemps_history):
    print("\nистория попыток")
    for i, (guess, result) in enumerate(attemps_history, 1):
        print(f"{i}. {guess} -> {result}")


def main():
    print("угадай число")
    print("я загадал число от 1 до 100")
    print("Команды: 'история' - показать попытки, 'выход'- закончить")

    secret_number = random.randint(1, 100)
    attemps = 0
    attemps_history = []

    while True:
        guess = input("твоя догадка").lower()
        attemps += 1

        if guess_input == 'выход':
            print("До свидания")
            break
        elif guess_input == 'история':
            show_history(attemps_history)
            continue

        if not guess_input.isdigit():
            print("введи число")
            continue

        guess = int(guess_input)
        attemps += 1

        if guess < secret_number:
            result = "загаданое число больше"
            print(result)
        elif guess > secret_number:
            result = "загаданое число меньше"
            print(result)
        else:
            result = "угадал"
            print(result)
            print(f"ты угадал за {attemps} попыток")

            show_history(attemps_history)
            break

        attemps_history.append((guess,result))

if __name__ == "__main__":
    main()
