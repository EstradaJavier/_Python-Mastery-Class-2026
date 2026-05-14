# 🐍 Python as an Object-Oriented Language

**Yes – Python is fully object-oriented** (and multi-paradigm)

Everything in Python is an object (even functions, classes, and basic types like int/str).

### Key OOP Features in Python
- **Classes & Objects** – `class` keyword
- **Inheritance** – Single and multiple
- **Encapsulation** – Name mangling with `__private`
- **Polymorphism** – Duck typing ("if it walks like a duck...")
- **Abstraction** – Abstract Base Classes (ABC module)

### Simple Example
```python
class Veteran:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def introduce(self):
        return f"I'm {self.name}, 100% P&T veteran."

javier = Veteran("Javier P. Estrada", 100)
print(javier.introduce())