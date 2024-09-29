
# играющий сдаётся, если он вводит одно из этих слов
EXIT_WORDS = {"quit", "exit", "сдаюсь", "выход"}
# загаданное секретное число
SECRET_NUMBER = 42
# максимально допустимое количество попыток
MAX_ATTEMPTS = 10

    
def print_introduction():
    "Распечатать вводное сообщение."
    print("0 < SECRET_NUMBER < 100. Make your guess.")

def print_less(user_input):
    "Распечатать ответ на слишком большое число."
    print(f"SECRET_NUMBER < {int(user_input)}. Try again.")

def print_greater(user_input):
    "Распечатать ответ на слишком маленькое число."
    print(f"SECRET_NUMBER > {user_input}. Try again.")

def print_equal(user_input):
    "Распечатать ответ на угаданное число."
    print(f"SECRET_NUMBER = {user_input}. You win!")

def print_early_exit():
    "Распечатать ответ на одно из EXIT_WORDS."
    print("You have given up.")

def print_end():
    "Распечатать сообщение об исчерпании количества попыток."
    print("Game is over.")

def print_error(user_input):
    "Человек, я тебя не понимаю!"
    quoted_exit_words = (f"'{w}'" for w in EXIT_WORDS)
    joined_exit_words = ", ".join(quoted_exit_words)
    print(f"What is '{user_input}'? Enter a number or one of {joined_exit_words}.")


# ------------------------------------------------------------------------------


def main():
    # начальное количество попыток
    ATTEMPT = 0
    print_introduction()
    while ATTEMPT < MAX_ATTEMPTS:
        user_input = input(f"Attempt № {ATTEMPT + 1}: Enter your guess: ").strip()
        if user_input in EXIT_WORDS:
            print_early_exit()
            break
        if user_input.isnumeric():
            user_input = int(user_input)
            ATTEMPT+=1
            if user_input == SECRET_NUMBER:
                print_equal(user_input)
                break
            elif user_input>SECRET_NUMBER:
                print_less(user_input)
            else:
                print_greater(user_input)
        else:
            print_error(user_input)
        if ATTEMPT == MAX_ATTEMPTS:
            print_end()

main ()