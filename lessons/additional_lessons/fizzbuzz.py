# fizzbuzz.py
# ------------------------------------------------------------
# PERSONALIZED ENHANCED FIZZBUZZ PROGRAM
# ------------------------------------------------------------
# This program does several things:
# 1. Asks the user for their name
# 2. Asks how far they want to count
# 3. Runs the classic FizzBuzz challenge
# 4. Explains the FIRST Fizz, Buzz, and FizzBuzz result
# 5. Prints a friendly closing message with today's date
# 6. Includes a weather message for Salado, TX 76571
#
# This version is written in a beginner-friendly style with
# lots of comments so you can learn what each part is doing.
#
# It is also
# later.
# ------------------------------------------------------------


# We import datetime so we can get the current date and time.
# This is useful for printing a personalized header and ending.
from datetime import datetime


# ------------------------------------------------------------
# FUNCTION: fizzbuzz_result
# ------------------------------------------------------------
# PURPOSE:
# This function handles the core FizzBuzz logic for ONE number.
#
# WHY THIS FUNCTION MATTERS:
# Instead of printing directly, this function RETURNS a value.
# Returning values makes the function much easier to test.
#
# EXAMPLES:
# fizzbuzz_result(3)  -> "Fizz"
# fizzbuzz_result(5)  -> "Buzz"
# fizzbuzz_result(15) -> "FizzBuzz"
# fizzbuzz_result(7)  -> "7"
#
# IMPORTANT CONCEPT:
# The modulo operator (%) gives the remainder after division.
# If the remainder is 0, that means the number is divisible.
#
# Example:
# 15 % 3 == 0  -> True
# 15 % 5 == 0  -> True
# So 15 should become "FizzBuzz"
# ------------------------------------------------------------
def fizzbuzz_result(n: int) -> str:
    """
    Return the FizzBuzz result for one number as a string.
    """

    # First, protect the function from bad input.
    # We only want positive integers greater than 0.
    if n < 1:
        raise ValueError("n must be a positive integer greater than 0")

    # IMPORTANT:
    # We must check "divisible by both 3 and 5" FIRST.
    #
    # Why?
    # Because if we checked "divisible by 3" first,
    # then 15 would incorrectly return "Fizz" and never
    # reach the "FizzBuzz" condition.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"

    # If the number is divisible by 3 only,
    # return "Fizz"
    if n % 3 == 0:
        return "Fizz"

    # If the number is divisible by 5 only,
    # return "Buzz"
    if n % 5 == 0:
        return "Buzz"

    # If none of the special rules matched,
    # return the number itself as a string.
    #
    # We convert it to a string so this function
    # always returns the same type of data.
    return str(n)


# ------------------------------------------------------------
# FUNCTION: build_fizzbuzz_lines
# ------------------------------------------------------------
# PURPOSE:
# Build all the lines we want to display from 1 to the limit.
#
# WHY THIS IS USEFUL:
# Instead of printing line by line immediately,
# we build a list of output lines first.
#
# BENEFITS:
# - cleaner program structure
# - easier to debug
# - easier to test
# - separates "building data" from "displaying data"
#
# EXTRA FEATURE:
# The first time we see:
# - Fizz
# - Buzz
# - FizzBuzz
# we include an explanation
# ------------------------------------------------------------
def build_fizzbuzz_lines(limit: int) -> list[str]:
    """
    Build the FizzBuzz output lines from 1 to limit.
    """

    # Validate the input so we do not process invalid numbers.
    if limit < 1:
        raise ValueError("limit must be a positive integer greater than 0")

    # This list will store every line we want to print.
    lines = []

    # These Boolean flags help us remember whether we already
    # explained each type of special result.
    #
    # False = explanation has NOT been shown yet
    # True  = explanation HAS already been shown
    explained_fizz = False
    explained_buzz = False
    explained_fizzbuzz = False

    # Loop through every number from 1 up to and including limit.
    #
    # range(1, limit + 1) includes the ending number.
    for i in range(1, limit + 1):

        # Ask our helper function what the FizzBuzz result should be.
        result = fizzbuzz_result(i)

        # CASE 1: FizzBuzz
        if result == "FizzBuzz":
            if not explained_fizzbuzz:
                # Add a longer explanation the FIRST time only.
                lines.append(
                    f"{i} → FizzBuzz ← because {i} is divisible by both 3 and 5"
                )
                explained_fizzbuzz = True
            else:
                # After that, use the shorter version.
                lines.append(f"{i} → FizzBuzz")

        # CASE 2: Fizz
        elif result == "Fizz":
            if not explained_fizz:
                lines.append(
                    f"{i} → Fizz ← because {i} is divisible by 3"
                )
                explained_fizz = True
            else:
                lines.append(f"{i} → Fizz")

        # CASE 3: Buzz
        elif result == "Buzz":
            if not explained_buzz:
                lines.append(
                    f"{i} → Buzz ← because {i} is divisible by 5"
                )
                explained_buzz = True
            else:
                lines.append(f"{i} → Buzz")

        # CASE 4: Normal number
        else:
            # If it is not Fizz, Buzz, or FizzBuzz,
            # just add the normal number string.
            lines.append(result)

    # Return the completed list of lines.
    return lines


# ------------------------------------------------------------
# FUNCTION: fizzbuzz
# ------------------------------------------------------------
# PURPOSE:
# Print the FizzBuzz lines to the screen.
#
# WHY THIS EXISTS:
# build_fizzbuzz_lines() creates the data
# fizzbuzz() displays the data
#
# This separation is a good programming habit.
# ------------------------------------------------------------
def fizzbuzz(limit: int) -> None:
    """
    Print the FizzBuzz output from 1 to limit.
    """

    # Loop through each prepared line and print it.
    for line in build_fizzbuzz_lines(limit):
        print(line)


# ------------------------------------------------------------
# FUNCTION: get_user_name
# ------------------------------------------------------------
# PURPOSE:
# Ask the user for their name.
#
# .strip() removes extra spaces before and after the text.
# ------------------------------------------------------------
def get_user_name() -> str:
    """
    Ask the user for their name and return it.
    """
    return input("What is your name? ").strip()


# ------------------------------------------------------------
# FUNCTION: get_max_number
# ------------------------------------------------------------
# PURPOSE:
# Ask the user how high they want to count in FizzBuzz.
#
# This function keeps asking until the user enters
# a valid positive integer.
#
# WHY THIS IS IMPORTANT:
# Users may type:
# - text like "hello"
# - decimal values like "3.5"
# - negative numbers
# - zero
#
# We want to handle mistakes gracefully instead of crashing.
# ------------------------------------------------------------
def get_max_number() -> int:
    """
    Ask the user for the maximum FizzBuzz number.
    Keep asking until a valid positive integer is entered.
    """

    while True:
        try:
            # input() gives us text, so we convert it to int.
            max_number = int(
                input("Up to what number do you want to FizzBuzz to? ").strip()
            )

            # Reject numbers less than 1.
            if max_number < 1:
                print("Please enter a positive number greater than 0.")
                continue

            # If the input is valid, return it.
            return max_number

        except ValueError:
            # This runs if int(...) fails.
            print("That's not a valid number. Please enter an integer.")


# ------------------------------------------------------------
# FUNCTION: print_header
# ------------------------------------------------------------
# PURPOSE:
# Print a nice welcome section before the FizzBuzz output starts.
#
# We use datetime.now() to get the current date/time,
# and strftime() to format it as readable text.
# ------------------------------------------------------------
def print_header(user_name: str, max_number: int) -> None:
    """
    Print the personalized program header.
    """

    # Get the current local date and time.
    now = datetime.now()

    # Format the date/time as Year-Month-Day Hour:Minute:Second
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    # Print the welcome message and summary.
    print("Welcome to the Personalized FizzBuzz Program!")
    print("-" * 50)
    print("\n" + "=" * 60)
    print(f"Date & Time: {current_datetime}")
    print("-" * 60)
    print(f"Hello, {user_name}! 👋")
    print(f"This FizzBuzz program will run up to: {max_number}")
    print("=" * 60 + "\n")


# ------------------------------------------------------------
# FUNCTION: print_closing_message
# ------------------------------------------------------------
# PURPOSE:
# Print a warm and friendly ending after the FizzBuzz output.
#
# This version includes:
# - the current weekday
# - the formatted date
# - a weather message for Salado, TX 76571
#
# IMPORTANT NOTE:
# The weather text below is currently hard-coded.
# That means it is written directly into the program.
# Later, you could upgrade this to pull live weather from an API.
# ------------------------------------------------------------
def print_closing_message(user_name: str) -> None:
    """
    Print the closing message with weather for Salado, TX 76571.
    """

    # Get the current date and time again.
    now = datetime.now()

    # Format the weekday name, like "Wednesday"
    day_of_week = now.strftime("%A")

    # Format the date, like "May 13, 2026"
    formatted_date = now.strftime("%B %d, %Y")

    # This is the weather summary we want to include.
    #
    # Right now it is manually written into the program.
    # That keeps things simple for a beginner version.
    weather_summary = "sunny and warm, with a high near 91°F"

    # Print a polished and friendly closing section.
    print("\n" + "-" * 60)
    print(f"{user_name}, have a wonderful {day_of_week}, {formatted_date}! 🚀")
    print(f"Today's weather in Salado, TX 76571 looks {weather_summary}.")
    print(
        f"Hope you have an awesome day, {user_name}, "
        f"and see you next time for more Python fun!"
    )
    print("-" * 60)


# ------------------------------------------------------------
# FUNCTION: main
# ------------------------------------------------------------
# PURPOSE:
# This is the main control center of the program.
#
# PROGRAM FLOW:
# 1. Ask for the user's name
# 2. Ask for the max number
# 3. Print the header
# 4. Run FizzBuzz
# 5. Print the closing message
#
# Keeping this logic inside main() makes the whole program
# easier to read and easier to maintain.
# ------------------------------------------------------------
def main() -> None:
    """
    Run the full interactive FizzBuzz program.
    """

    # Step 1: ask for the user's name
    user_name = get_user_name()

    # Step 2: ask how high the user wants to count
    max_number = get_max_number()

    # Step 3: print the welcome/header section
    print_header(user_name, max_number)

    # Step 4: run the FizzBuzz sequence
    fizzbuzz(max_number)

    # Step 5: print the warm closing message
    print_closing_message(user_name)


# ------------------------------------------------------------
# PYTHON ENTRY POINT
# ------------------------------------------------------------
# This special check makes sure main() only runs when this file
# is executed directly.
#
# If you run:
#   python fizzbuzz.py
# then main() runs.
#
# If you import this file into a test file, main() does NOT run.
# That is very helpful for unit testing.
# ------------------------------------------------------------
if __name__ == "__main__":
    main()