# fizzbuzz.py - Enhanced Classic FizzBuzz with user input, date/time, personalized messages
# Now with explanations for the FIRST occurrence of Fizz, Buzz, and FizzBuzz

import datetime  # Built-in module to get current date and time


def fizzbuzz(n: int) -> None:
    """
    Prints the FizzBuzz sequence from 1 to n (inclusive) with explanations for
    the FIRST occurrence of each special case (Fizz, Buzz, FizzBuzz).

    Args:
        n (int): The upper limit of the sequence (must be positive)

    Returns:
        None: Only prints output
    """
    # Trackers to show explanation only once for each type
    explained_fizz = False
    explained_buzz = False
    explained_fizzbuzz = False

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            if not explained_fizzbuzz:
                print("FizzBuzz  ← because 15 is divisible by both 3 and 5")
                explained_fizzbuzz = True
            else:
                print("FizzBuzz")

        elif i % 3 == 0:
            if not explained_fizz:
                print("Fizz     ← because 3 is divisible by 3")
                explained_fizz = True
            else:
                print("Fizz")

        elif i % 5 == 0:
            if not explained_buzz:
                print("Buzz     ← because 5 is divisible by 5")
                explained_buzz = True
            else:
                print("Buzz")

        else:
            print(i)


# =======================
# Main Execution Block
# =======================
if __name__ == "__main__":
    # Get current date and time
    now = datetime.datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    day_of_week = now.strftime("%A")
    formatted_date = now.strftime("%B %d, %Y")

    # === User Input Section ===
    print("Welcome to the Personalized FizzBuzz Program!")
    print("-" * 50)

    user_name = input("What is your name? ").strip()

    while True:
        try:
            max_number_str = input("Up to what number do you want to FizzBuzz to? ").strip()
            max_number = int(max_number_str)

            if max_number < 1:
                print("Please enter a positive number greater than 0.")
                continue

            break

        except ValueError:
            print("That's not a valid number. Please enter an integer.")

    # === Personalized Output Header ===
    print("\n" + "=" * 60)
    print(f"Date & Time: {current_datetime}")
    print("-" * 60)
    print(f"Hello, {user_name}! 👋")
    print(f"This FizzBuzz Program will give you the numbers up to: {max_number}")
    print("=" * 60 + "\n")

    # Run the enhanced FizzBuzz!
    fizzbuzz(max_number)

    # === Friendly Closing ===
    print("\n" + "-" * 60)
    print(f"{user_name}, have a great {day_of_week}, {formatted_date}! 🚀")
    print("See you next time for more Python fun!")
    print("-" * 60)
