# ===================================
# 01_basics.py
# Python Mastery 2026 - Lesson 1: Python Basics
# ===================================

"""
MODULE OVERVIEW
---------------
This lesson introduces the foundational ideas that every beginner needs in Python.

Learning goals:
1. Understand what Python is doing when we create variables.
2. Recognize common built-in data types: str, int, float, bool.
3. Learn how to work with strings and f-strings.
4. Understand what functions are and why they are useful.
5. Learn how conditionals allow programs to make decisions.

Teaching philosophy:
- Keep examples small and concrete.
- Use comments to explain both "what" and "why."
- Reinforce vocabulary slowly and clearly.
- Favor readable examples over clever shortcuts.

This file is intentionally more verbose than professional production code
because it is written for learning, not for deployment.
"""

from datetime import date


def show_intro():
    """
    Display a welcome message and outline the purpose of the lesson.

    This function is intentionally simple. It shows that a function can be used
    to group related actions together.
    """
    print("🎉 Welcome to Python Mastery 2026! 🎉")
    print("Lesson 1: Python Basics - Your First Step Toward Mastery\n")
    print("In this lesson, we will study the building blocks of Python.")
    print("Each section introduces one important idea at a time.")
    print("Read the comments carefully, then run the file and study the output.\n")
    print("=" * 70)


def demonstrate_variables():
    """
    Introduce variables and basic data types.

    Key teaching points:
    - A variable is a name that refers to a value.
    - Python does not require explicit type declarations like some other languages.
    - Python determines the type from the assigned value at runtime.
    """
    print("\n📌 SECTION 1: VARIABLES & DATA TYPES")
    print("A variable is a name that refers to a value stored in memory.\n")

    # In Java, a beginner might write:
    #   String name = "Javier";
    #   int age = 63;
    #
    # In Python, we do not explicitly declare the type in most beginner code.
    # Python examines the value on the right side of the assignment operator (=)
    # and determines the type automatically.
    #
    # This is one reason Python is often considered beginner-friendly.

    name = "Javier"        # str  -> string (text)
    age = 63               # int  -> integer (whole number)
    height_meters = 1.78   # float -> decimal number
    is_married = True      # bool -> True or False

    print("Python created these variables and inferred their types automatically:\n")
    print(f"• name = {name}              -> type: {type(name)}")
    print(f"• age = {age}                -> type: {type(age)}")
    print(f"• height_meters = {height_meters}   -> type: {type(height_meters)}")
    print(f"• is_married = {is_married}       -> type: {type(is_married)}\n")

    print("Important idea:")
    print("The variable name does not carry a permanently fixed type.")
    print("Instead, the variable refers to a value, and that value has a type.\n")

    # This example shows reassignment.
    # It is useful academically because it reveals Python's dynamic typing.
    example = 10
    print(f"example = {example} -> {type(example)}")

    example = 10.5
    print(f"example = {example} -> {type(example)}")

    example = "ten"
    print(f"example = {example} -> {type(example)}\n")

    print("This flexibility is powerful, but it also means the programmer must")
    print("stay organized and use clear names.\n")

    print("Naming advice:")
    print("- Use descriptive variable names.")
    print("- Prefer account_balance over x.")
    print("- Prefer student_name over data.\n")


def demonstrate_strings(name, age):
    """
    Demonstrate how strings work in Python.

    Parameters:
    - name: expected to be a string
    - age: expected to be an integer

    This section teaches:
    - What strings are
    - How f-strings work
    - A few common string operations
    """
    print("📝 SECTION 2: STRINGS & f-STRINGS")
    print("A string is a sequence of characters used to represent text.\n")

    print("1. Creating a sentence with an f-string")
    print("An f-string lets us insert variable values directly into text.\n")

    introduction = f"Hello! My name is {name} and I am {age} years old."
    print(introduction)
    print()

    print("2. Common string operations")
    print(f"Original text: {name}")
    print(f"Uppercase: {name.upper()}")
    print(f"Lowercase: {name.lower()}")
    print(f"Length: {len(name)} characters\n")

    # Beginner-friendly note:
    # Methods are actions that belong to an object.
    # We write them with dot notation.
    print("Important idea:")
    print("When we write name.upper(), we are calling a method on a string object.")
    print("Methods are behaviors attached to specific kinds of data.\n")

    print("3. String concatenation")
    first = "Python"
    second = "Basics"
    combined = first + " " + second
    print(f'first = "{first}"')
    print(f'second = "{second}"')
    print(f'combined = first + " " + second -> {combined}\n')

    print("4. Why strings matter")
    print("Strings are used in names, messages, file paths, user input,")
    print("web data, labels, and almost every real program you will write.\n")


def greet_person(name):
    """
    Print a greeting to a specific person.

    Parameters:
    - name: the person's name as text

    This function prints output directly.
    It does not return a value.
    """
    print(f"👋 Hello, {name}! Welcome to Python learning!")


def add_two_numbers(a, b):
    """
    Return the sum of two values.

    This function is useful because it introduces the idea that
    some functions return data instead of printing it.
    """
    return a + b


def demonstrate_functions():
    """
    Demonstrate what functions are and why they are useful.

    Key teaching points:
    - Functions help organize code.
    - Functions can take input through parameters.
    - Functions may print results or return results.
    """
    print("🔧 SECTION 3: FUNCTIONS")
    print("A function is a reusable block of code that performs a task.\n")

    print("Why functions matter:")
    print("- They reduce repetition.")
    print("- They organize code into meaningful parts.")
    print("- They make programs easier to read, test, and improve.\n")

    print("1. Calling a function that prints a greeting")
    greet_person("Javier")
    print()

    print("2. Calling a function that returns a value")
    result = add_two_numbers(3, 5)
    print(f"add_two_numbers(3, 5) returned: {result}\n")

    print("Important distinction:")
    print("- print() displays information to the screen.")
    print("- return sends a value back to the place where the function was called.\n")


def demonstrate_conditionals(age):
    """
    Demonstrate conditional logic using if, elif, and else.

    Conditionals allow a program to make decisions by evaluating
    whether a statement is True or False.
    """
    print("⚖️ SECTION 4: CONDITIONALS (Making Decisions)")
    print("Conditionals let a program choose among different paths.\n")

    print("Python checks conditions from top to bottom.")
    print("As soon as one condition is True, that block runs.\n")

    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are a working-age adult.")
    else:
        print("You are a senior citizen.")

    print(f"\nGiven age = {age}, Python selected the correct branch.\n")

    print("Examples of conditions:")
    print("age < 18   -> Is age less than 18?")
    print("age == 63  -> Is age exactly 63?")
    print("age >= 21  -> Is age at least 21?\n")


def demonstrate_real_world_example():
    """
    Provide a small real-world example that combines variables,
    strings, arithmetic, and conditionals.
    """
    print("🌍 SECTION 5: A SMALL REAL-WORLD EXAMPLE")
    print("This example combines several ideas from the lesson.\n")

    today = date.today()
    current_year = today.year
    birth_year = 1962
    approximate_age = current_year - birth_year

    print(f"Today's date is: {today}")
    print(f"Birth year: {birth_year}")
    print(f"Approximate age: {approximate_age}\n")

    if approximate_age >= 18:
        print("This person is an adult.")
    else:
        print("This person is a minor.")

    print("\nNotice what happened here:")
    print("- We stored values in variables.")
    print("- We performed arithmetic.")
    print("- We displayed values with f-strings.")
    print("- We used a conditional to make a decision.\n")


def main():
    """
    Run the full lesson in a clear instructional order.

    The main function acts like a lesson plan:
    it decides which section appears and in what order.
    """
    show_intro()
    demonstrate_variables()
    demonstrate_strings("Javier", 63)
    demonstrate_functions()
    demonstrate_conditionals(63)
    demonstrate_real_world_example()

    print("🎯 Lesson 1 Complete!")
    print("You now have a foundation in:")
    print("- Variables")
    print("- Data types")
    print("- Strings")
    print("- Functions")
    print("- Conditionals")
    print("\nKeep reviewing the comments and changing the examples.")
    print("That is one of the best ways to learn Python well. 🚀")


if __name__ == "__main__":
    main()