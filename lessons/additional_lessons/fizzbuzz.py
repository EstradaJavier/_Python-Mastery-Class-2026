# fizzbuzz.py - Enhanced Classic FizzBuzz with user input, date/time, and explanations
import datetime


def fizzbuzz(n: int) -> None:
    """Prints the FizzBuzz sequence from 1 to n with explanations for the FIRST occurrence."""

    explained_fizz = False
    explained_buzz = False
    explained_fizzbuzz = False

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            if not explained_fizzbuzz:
                print(f"{i} → FizzBuzz ← because {i} is divisible by both 3 and 5")
                explained_fizzbuzz = True
            else:
                print(f"{i} → FizzBuzz")

        elif i % 3 == 0:
            if not explained_fizz:
                print(f"{i} → Fizz ← because {i} is divisible by 3")
                explained_fizz = True
            else:
                print(f"{i} → Fizz")

        elif i % 5 == 0:
            if not explained_buzz:
                print(f"{i} → Buzz ← because {i} is divisible by 5")
                explained_buzz = True
            else:
                print(f"{i} → Buzz")
        else:
            print(i)


# =======================
# Main Execution Block
# =======================
if __name__ == "__main__":
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    day_of_week = now.strftime("%A")
    formatted_date = now.strftime("%B %d, %Y")

    print("Welcome to the Personalized FizzBuzz Program!")
    print("-" * 50)

    user_name = input("What is your name? ").strip()

    while True:
        try:
            max_number = int(input("Up to what number do you want to FizzBuzz to? ").strip())
            if max_number < 1:
                print("Please enter a positive number greater than 0.")
                continue
            break
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

    # Personalized Header
    print("\n" + "=" * 60)
    print(f"Date & Time: {current_datetime}")
    print("-" * 60)
    print(f"Hello, {user_name}! 👋")
    print(f"This FizzBuzz Program will run up to: {max_number}")
    print("=" * 60 + "\n")

    # Run FizzBuzz
    fizzbuzz(max_number)

    # Closing Message
    print("\n" + "-" * 60)
    print(f"{user_name}, have a great {day_of_week}, {formatted_date}! 🚀")
    print("See you next time for more Python fun!")
    print("-" * 60)