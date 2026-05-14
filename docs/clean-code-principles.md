# 🧹 CLEAN Code Principles in Python

**C.L.E.A.N.** – A mnemonic for writing maintainable, professional Python code  
(Adapted from clean code philosophy by Robert C. Martin and Python best practices)

| Letter | Principle | Explanation | Python Example |
|-------|-----------|-------------|--------------|
| **C** | **Clear** | Code should be easy to understand at a glance | Use descriptive names: `calculate_salary_increase` not `csi` |
| **L** | **Logical** | Flow should follow natural reasoning | Guard clauses instead of nested ifs |
| **E** | **Efficient** | Avoid unnecessary computation | Use list comprehensions over loops when appropriate |
| **A** | **Adaptable** | Easy to change or extend | Follow SOLID principles, especially Single Responsibility |
| **N** | **No Duplication** (DRY) | Don't Repeat Yourself | Extract repeated code into functions or classes |

### Quick Tips for CLEAN Python
- Functions < 30 lines
- Classes do one thing
- Use type hints (`def func(name: str) -> int:`)
- Docstrings for every function/class
- PEP 8 + Black formatter
- Meaningful commit messages

**Goal**: Write code that your future self (or a recruiter reviewing your repo) can understand in seconds.

*Inspired by "Clean Code" by Uncle Bob – adapted for Python Mastery 2026*