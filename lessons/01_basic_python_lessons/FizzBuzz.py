FizzBuzz Program
----------------
Prints numbers from 1 to 100 with the following rules:
- If the number is divisible by 3, print "Fizz"
- If the number is divisible by 5, print "Buzz"
- If the number is divisible by both 3 and 5, print "FizzBuzz"
- Otherwise, print the number
"""

def fizzbuzz(start=1, end=100):
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == "__main__":
    fizzbuzz()