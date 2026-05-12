# ===================================
# 01_basics.py
# Python Mastery 2026 - Lesson 1: Python Basics and Foundations
# ===================================
#
# PURPOSE OF THIS FILE
# --------------------
# This lesson introduces beginner-level Python basics:
# - Printing output
# - Comments
# - Variables
# - Data types
# - Basic math
# - Strings and f-strings
# - Boolean values
# - Simple functions
# - User profile data
# - Age calculation from date of birth
# - Basic testing with assert
# - Using if statements
# - Type conversion
#
# EXPECTED RESULT WHEN YOU RUN THIS FILE
# --------------------------------------
# The program will:
# 1. Print an introduction.
# 2. Build a small personal profile.
# 3. Calculate age from date of birth.
# 4. Display data types for several values.
# 5. Run simple math and string examples.
# 6. Show beginner-friendly examples of lists and conditionals.
# 7. Run a few self-tests.
# 8. Print a completion message.
#
# BEST PRACTICE NOTES
# -------------------
# - Keep code readable.
# - Use 4 spaces for indentation.
# - Use clear variable names.
# - Add comments to explain WHY something matters, not just WHAT it says.
# - Use functions to break a large problem into smaller pieces.
# - Test simple ideas often.
#
# VISUAL LEARNER TIP
# ------------------
# Think of this file like a lesson broken into blocks:
# Intro -> Profile -> Data Types -> Operations -> Decisions -> Tests
# You can collapse and expand functions in IntelliJ to study one block at a time.

# ============================================================
# IMPORTS
# ============================================================
#
# Imports bring in code written by Python or other programmers.
# Here we import date and datetime so we can work with dates.
#
# date     -> used to store a date like 1963-02-09
# datetime -> used here to convert text input into a date object

from datetime import date, datetime

# ============================================================
# INTELLIJ HELP FOR BEGINNERS
# ============================================================
#
# BEFORE YOU RUN:
# 1. Open your project in IntelliJ IDEA.
# 2. Make sure Python is installed on your computer.
# 3. Make sure your project has a Python interpreter selected.
#
# HOW TO CHECK YOUR PYTHON INTERPRETER IN INTELLIJ:
# - Go to File -> Project Structure, or Settings/Preferences
# - Look for Python Interpreter / SDK
# - Select a valid Python version
#
# HOW TO RUN THIS FILE:
# - Right-click anywhere in this file
# - Click: Run '01_basics'
# - Or click the green triangle near the top
# - Or use Shift + F10 in many IntelliJ setups
#
# HOW TO RUN ONLY A FEW LINES:
# - Highlight the lines you want
# - Right-click
# - Choose: Execute Selection in Python Console
#
# HOW TO COMMENT / UNCOMMENT CODE:
# - Mac: Cmd + /
# - Windows: Ctrl + /
#
# HOW TO DEBUG:
# - Click in the gutter next to a line number to add a breakpoint
# - Right-click the file
# - Choose Debug
# - Then step through line by line
#
# WHAT __name__ == "__main__" MEANS:
# - Python runs the code inside that block only when this file is run directly.
# - If another file imports this file, the main() function will not run automatically.

# ============================================================
# INTRODUCTION OUTPUT
# ============================================================

def show_intro():
    """
    Print the lesson title and learning goals.

    This function does not return anything.
    It simply displays text to the screen.
    """
    print("Welcome to Python Mastery 2026 - Lesson 1: Basics")
    print("In this lesson, you will practice core Python foundations.")
    print("We will explore variables, data types, strings, math,")
    print("functions, conditionals, and beginner-friendly self-tests.\n")


# ============================================================
# AGE CALCULATION
# ============================================================

def calculate_age_from_dob(dob: date) -> int:
    """
    Calculate age from date of birth.

    Parameter:
        dob (date): A date object representing the person's birth date.

    Returns:
        int: The person's age in whole years.

    HOW IT WORKS:
    - Start with the difference in years.
    - If the birthday has not happened yet this year,
      subtract 1 from the result.
    """
    today = date.today()
    return today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
    )


# ============================================================
# OPTIONAL USER INPUT
# ============================================================

def get_dob_from_user() -> date:
    """
    Ask the user to enter a DOB in YYYY-MM-DD format.

    Example valid input:
        1963-02-09

    Returns:
        date: A Python date object

    IMPORTANT:
    If the format is wrong, Python will raise an error.
    That is normal for this beginner lesson.
    Later lessons can teach try/except for safer input handling.
    """
    dob_input = input("Enter your DOB (YYYY-MM-DD): ")
    return datetime.strptime(dob_input, "%Y-%m-%d").date()


# ============================================================
# PROFILE CREATION
# ============================================================

def create_profile(use_input=False):
    """
    Create a beginner-friendly personal profile.

    Parameter:
        use_input (bool): If True, ask the user for DOB.
                          If False, use the lesson's saved DOB.

    Returns:
        tuple: name, age, height_feet, height_inches, height_meters,
               eye_color, blood_type, is_married, spouse_name, dob

    BEGINNER NOTE:
    A tuple is a collection of values returned together.
    """
    name = "Javier"
    eye_color = "Hazel"
    blood_type = "O-"
    is_married = True
    spouse_name = "Alesha Estrada"

    # Height stored in feet and inches because that is familiar to many beginners.
    height_feet = 5
    height_inches = 10

    # Convert height to total inches, then to meters.
    total_inches = (height_feet * 12) + height_inches
    height_meters = round(total_inches * 0.0254, 2)

    # Choose DOB source.
    if use_input:
        dob = get_dob_from_user()
    else:
        dob = date(1963, 2, 9)

    age = calculate_age_from_dob(dob)

    return (
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    )


# ============================================================
# DISPLAY PROFILE INFO
# ============================================================

def display_profile(
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
):
    """
    Print the user's profile and show the type of each value.

    WHY THIS MATTERS:
    Beginners often see values but do not yet notice their data types.
    This section helps connect the value with its Python type.
    """
    print("===== PROFILE INFORMATION =====")
    print(f"Name: {name} (type: {type(name)})")
    print(f"Date of birth: {dob} (type: {type(dob)})")
    print(f"Age: {age} (type: {type(age)})")
    print(f"Height: {height_feet}'{height_inches}\" / {height_meters} m")
    print(f"Eye color: {eye_color} (type: {type(eye_color)})")
    print(f"Blood type: {blood_type} (type: {type(blood_type)})")
    print(f"Married: {is_married} (type: {type(is_married)})")
    print(f"Spouse: {spouse_name} (type: {type(spouse_name)})\n")


# Explanation of the
# lines 247 & 248:
# EXPLANATION OF THESE TWO LINES (BEGINNER-FRIENDLY)
# ---------------------------------------------------
# Line 1:
# print(f"Age: {age} (type: {type(age)})")
#
# 1. print(...)
#    - print(...) is a built‑in Python function.
#    - It sends information to the screen (the console).
#    - Whatever you put inside the parentheses will be shown to the user.
#
# 2. f"..."
#    - The f in front of the string makes this a "formatted string literal",
#      commonly called an f‑string.
#    - It tells Python: "Inside this string, I will embed live values from
#      variables or expressions."
#    - Without the f, anything in {curly_braces} would just be plain text.
#
# 3. The string "Age: {age} (type: {type(age)})"
#    - This whole thing is one string template.
#    - Parts WITHOUT braces are fixed text.
#    - Parts WITH braces { ... } are placeholders that Python will replace
#      with actual values when the line runs.
#
# 4. {age}
#    - age is a variable you defined earlier, most likely an int (integer).
#    - {age} tells Python: "Take the current value stored in age and insert
#      it here as text."
#    - Example: if age = 63, this part becomes "63" in the final output.
#
# 5. {type(age)}
#    - type(age) is a function call used as an expression.
#    - type(...) returns the data type of the value you pass in.
#      For example, type(63) returns <class 'int'>.
#    - {type(age)} tells Python: "Evaluate type(age), then insert that
#      result as text."
#    - This is useful for learning, because it shows you not only the value
#      of age, but also what kind of value it is.
#
# 6. How Python builds the final string
#    - Start with the template: "Age: {age} (type: {type(age)})"
#    - Replace {age} with the current value of age.
#    - Replace {type(age)} with the string version of age's type.
#    - Example:
#        age = 63
#      Then the printed line looks like:
#        Age: 63 (type: <class 'int'>)
#
# 7. Why this is helpful for beginners
#    - You see the value and its type in one place.
#    - It reinforces that age is not just "63", but specifically an integer,
#      which matters for math and other operations.

# ---------------------------------------------------
# Line 2:
# print(f"Height: {height_feet}'{height_inches}\" / {height_meters} m")
#
# 1. Same print(...) and f-string idea
#    - print(...) shows a line on the screen.
#    - The f before the quotes means "this string can include placeholders
#      for variables and expressions".
#
# 2. The variables used here
#    - height_feet      -> expected to be an integer for the feet part (for example, 5)
#    - height_inches    -> expected to be an integer for the inches part (for example, 10)
#    - height_meters    -> usually a float representing height in meters (for example, 1.78)
#
# 3. The overall string template
#    - "Height: {height_feet}'{height_inches}\" / {height_meters} m"
#    - Break it into pieces:
#        "Height: "          -> fixed text
#        {height_feet}       -> placeholder for the feet value
#        "'"                 -> a single quote character (for feet)
#        {height_inches}     -> placeholder for the inches value
#        \"                  -> an escaped double quote character (for inches)
#        " / "               -> fixed text separator
#        {height_meters}     -> placeholder for the metric height
#        " m"                -> fixed text, letter m for meters
#
# 4. Why there is a backslash before the double quote (\")
#    - The whole string is wrapped in double quotes: f"..."
#    - If you wrote " directly inside, Python would think that ends the string.
#    - Using \" tells Python: "This is a literal double quote character inside
#      the string, not the end of the string."
#    - On screen, you will see a normal " character.
#
# 5. How Python builds the final output
#    - Suppose:
#        height_feet = 5
#        height_inches = 10
#        height_meters = 1.78
#    - Python replaces each placeholder:
#        {height_feet}   -> 5
#        {height_inches} -> 10
#        {height_meters} -> 1.78
#    - The printed line becomes:
#        Height: 5'10" / 1.78 m
#
# 6. Visual way to read this line
#    - Think of it as a sentence with three blanks:
#        "Height: [feet]'[inches]\" / [meters] m"
#    - {height_feet}, {height_inches}, and {height_meters} are the blanks.
#    - Each time the program runs, Python fills in the blanks with the
#      current values of those variables.
#
# 7. Why this formatting is useful
#    - It shows both imperial (feet/inches) and metric (meters) in a single,
#      easy‑to‑read line.
#    - It keeps all the formatting logic in one place instead of using
#      multiple prints or manual string concatenation.

# ============================================================
# DATA TYPES LESSON
# ============================================================

def explain_basic_data_types(age, height_meters, eye_color, is_married):
    """
    Show common beginner data types.

    This lesson focuses on:
    - int
    - float
    - str
    - bool
    """
    print("===== BASIC DATA TYPES =====")
    print(f"Integer example: age = {age}")
    print("Integers are whole numbers like 1, 25, and 100.\n")

    print(f"Float example: height_meters = {height_meters}")
    print("Floats are numbers with decimals like 1.5 or 3.14.\n")

    print(f"String example: eye_color = '{eye_color}'")
    print("Strings are text values inside quotes.\n")

    print(f"Boolean example: is_married = {is_married}")
    print("Booleans are only True or False.\n")


# ============================================================
# STRING BASICS
# ============================================================

def string_examples(name, eye_color, spouse_name):
    """
    Demonstrate beginner string operations.
    """
    print("===== STRING EXAMPLES =====")

    # Concatenation joins strings together.
    print("Concatenation:")
    print(name + " has " + eye_color + " eyes.\n")

    # f-strings are the modern preferred way to build strings.
    print("f-string:")
    print(f"{name} is married to {spouse_name}.\n")

    # Common string methods.
    print("String methods:")
    print(f"Uppercase name: {name.upper()}")
    print(f"Lowercase eye color: {eye_color.lower()}")
    print(f"Spouse name length: {len(spouse_name)} characters\n")


# ============================================================
# NUMBER OPERATIONS
# ============================================================

def run_operations(age, height_meters):
    """
    Demonstrate basic arithmetic.

    Returns:
        tuple: years_to_retirement, height_feet_decimal
    """
    print("===== BASIC OPERATIONS =====")

    years_to_retirement = 65 - age
    height_feet_decimal = round(height_meters * 3.28084, 2)

    print(f"Years to retirement at age 65: {years_to_retirement}")
    print(f"Height in decimal feet: {height_feet_decimal}")

    # Extra math examples.
    print(f"Age plus 10 years: {age + 10}")
    print(f"Age minus 5 years: {age - 5}")
    print(f"Age multiplied by 2: {age * 2}")
    print(f"Age divided by 2: {age / 2}\n")

    return years_to_retirement, height_feet_decimal


# ============================================================
# TYPE CONVERSION
# ============================================================

def type_conversion_examples(age, blood_type):
    """
    Show how Python can convert values from one type to another.
    """
    print("===== TYPE CONVERSION =====")

    age_as_string = str(age)
    sample_number_text = "42"
    converted_number = int(sample_number_text)

    print(f"Age as string: {age_as_string} (type: {type(age_as_string)})")
    print(f"Text '42' converted to int: {converted_number} (type: {type(converted_number)})")
    print(f"Blood type stays a string: {blood_type} (type: {type(blood_type)})\n")


# ============================================================
# CONDITIONALS
# ============================================================

def conditional_examples(age, is_married):
    """
    Demonstrate if / elif / else.

    CONDITIONALS help your program make decisions.
    """
    print("===== CONDITIONAL EXAMPLES =====")

    if age < 18:
        print("Minor: under 18")
    elif age < 65:
        print("Adult: between 18 and 64")
    else:
        print("Senior: 65 or older")

    if is_married:
        print("Marital status: Married")
    else:
        print("Marital status: Not married")

    print()


# ============================================================
# LIST BASICS
# ============================================================

def list_examples():
    """
    Introduce a list, one of Python's most common data structures.
    """
    print("===== LIST EXAMPLES =====")

    favorite_topics = [
        "Python basics",
        "Variables",
        "Strings",
        "Functions",
        "Conditionals",
    ]

    print(f"List: {favorite_topics}")
    print(f"First item: {favorite_topics[0]}")
    print(f"Number of items: {len(favorite_topics)}")

    print("Looping through the list:")
    for topic in favorite_topics:
        print(f"- {topic}")

    print()


# ============================================================
# VISUAL STRUCTURE HELP
# ============================================================

def visual_map():
    """
    Give the learner a visual map of the program flow.
    """
    print("===== VISUAL MAP OF THIS PROGRAM =====")
    print("main()")
    print("  -> show_intro()")
    print("  -> create_profile()")
    print("  -> display_profile()")
    print("  -> explain_basic_data_types()")
    print("  -> string_examples()")
    print("  -> run_operations()")
    print("  -> type_conversion_examples()")
    print("  -> conditional_examples()")
    print("  -> list_examples()")
    print("  -> self_test()")
    print()


# ============================================================
# SELF-TEST
# ============================================================

def self_test(name, age, height_meters, years_to_retirement):
    """
    Run simple checks to make sure important values make sense.

    assert means:
    'This condition must be True, or stop the program with an error.'
    """
    print("===== SELF-TEST =====")

    # Type checks
    assert isinstance(name, str), "Name should be a string."
    assert isinstance(age, int), "Age should be an integer."
    assert isinstance(height_meters, float), "Height in meters should be a float."

    # Logical checks
    assert age > 0, "Age must be positive."
    assert years_to_retirement == 65 - age, "Retirement calculation failed."

    # Value checks
    assert len(name) > 0, "Name should not be empty."

    print("All self-tests passed. Great job — the basics are working.\n")


# ============================================================
# EXTRA BEGINNER PRACTICE
# ============================================================

def beginner_practice_snippets():
    """
    Show a few small examples that beginners can experiment with.

    These are intentionally simple and connected to lesson 1.
    """
    print("===== EXTRA PRACTICE SNIPPETS =====")

    print("Snippet 1: Variable reassignment")
    score = 10
    print(f"Starting score: {score}")
    score = score + 5
    print(f"Updated score: {score}\n")

    print("Snippet 2: Comparing values")
    a = 7
    b = 10
    print(f"Is a greater than b? {a > b}")
    print(f"Is a less than b? {a < b}")
    print(f"Is a equal to b? {a == b}\n")

    print("Snippet 3: A very small function")
    def add_numbers(x, y):
        return x + y

    print(f"add_numbers(3, 4) = {add_numbers(3, 4)}\n")


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    """
    Control the order of the lesson.

    WHY USE main()?
    - It keeps your program organized.
    - It gives your file a clear starting point.
    - It makes large programs easier to read and maintain.
    """
    show_intro()
    visual_map()

    # Change this to True if you want the program to ask for DOB input.
    use_input = False

    (
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    ) = create_profile(use_input)

    display_profile(
        name,
        age,
        height_feet,
        height_inches,
        height_meters,
        eye_color,
        blood_type,
        is_married,
        spouse_name,
        dob,
    )

    explain_basic_data_types(age, height_meters, eye_color, is_married)
    string_examples(name, eye_color, spouse_name)

    years_to_retirement, height_feet_decimal = run_operations(age, height_meters)

    type_conversion_examples(age, blood_type)
    conditional_examples(age, is_married)
    list_examples()
    beginner_practice_snippets()

    self_test(name, age, height_meters, years_to_retirement)

    print("Lesson 1 complete.")
    print("Review the comments, rerun the program, and experiment with values.")
    print("Try changing a variable and predict what the output will be before running it.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()