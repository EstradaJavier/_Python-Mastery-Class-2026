# ===================================
# 01_basics.py
# Python Mastery 2026 - Lesson 1: Python Basics
# ===================================

from datetime import date


def show_intro():
    print("🎉 Welcome to Python Mastery 2026! 🎉")
    print("Lesson 1: Python Basics - Your First Step Toward Mastery\n")
    print("In this lesson, we'll explore the fundamental building blocks of Python.")
    print("Let's make it fun and clear!\n")
    print("=" * 60)


def demonstrate_variables():
    print("\n📌 SECTION 1: VARIABLES & DATA TYPES")
    print("Variables are like boxes where we store information.\n")

    name = "Javier"
    age = 63
    height_meters = 1.78
    is_married = True

    print(f"• Name: {name}  → This is a 'string' (text)")
    print(f"• Age: {age}     → This is an 'integer' (whole number)")
    print(f"• Height: {height_meters} meters → This is a 'float' (decimal number)")
    print(f"• Married: {is_married} → This is a 'boolean' (True/False value)")
    print("These are the most common data types you'll use!\n")


def demonstrate_strings(name, age):
    print("📝 SECTION 2: STRINGS & f-STRINGS")
    print("Strings are how we work with text in Python.\n")

    print(f"1. Using an f-string (modern & recommended):")
    print(f"   Hello! My name is {name} and I am {age} years old.\n")

    print("2. String methods (very useful!):")
    print(f"   Uppercase: {name.upper()}")
    print(f"   Lowercase: {name.lower()}")
    print(f"   Length of my name: {len(name)} characters\n")


def demonstrate_functions():
    print("🔧 SECTION 3: FUNCTIONS")
    print("Functions are reusable blocks of code. They help us organize our program.\n")

    def greet_person(name):
        print(f"👋 Hello {name}! Welcome to Python learning!")

    greet_person("Javier")
    print()


def demonstrate_conditionals(age):
    print("⚖️ SECTION 4: CONDITIONALS (Making Decisions)")
    print("if / elif / else statements let our program make choices.\n")

    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are a working-age adult.")
    else:
        print("You are a senior citizen.")

    print(f"Since you are {age} years old, Python made the correct decision above!\n")


def main():
    show_intro()

    demonstrate_variables()
    demonstrate_strings("Javier", 63)
    demonstrate_functions()
    demonstrate_conditionals(63)

    print("🎯 Lesson 1 Complete!")
    print("You now understand: Variables, Strings, Functions, and Conditionals.")
    print("These are the foundation of everything you'll build in Python!")
    print("\nGreat job today! Keep practicing and have fun learning! 🚀")


if __name__ == "__main__":
    main()