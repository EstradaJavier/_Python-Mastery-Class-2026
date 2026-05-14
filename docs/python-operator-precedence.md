# Python Operator Precedence Cheat Sheet (2026)

> "Parentheses are your best friend.  
> When in doubt — use them. Explicit is better than implicit."  
> — The Zen of Python + every experienced ML engineer

## 1. Plain Mathematics (School PEMDAS/BODMAS)

Most people learn this order:

| Priority | Operation                  | Symbol(s)       | Example                  | Result |
|----------|----------------------------|-----------------|--------------------------|--------|
| 1        | Parentheses                | `( )`           | `(2 + 3) × 4`            | 20     |
| 2        | Exponents (powers)         | `²` `³` etc.    | `2 + 3²`                 | 11     |
| 3        | Multiplication & Division  | `×` `÷`         | `10 ÷ 2 × 5`             | 25     |
| 4        | Addition & Subtraction     | `+` `−`         | `10 + 6 − 2`             | 14     |

**Left-to-right** for same priority (except exponents — right-to-left)

## 2. Python Reality — Full Operator Precedence Table (Python 3.10–3.14+)

Python follows roughly PEMDAS but with **many more operators** that frequently appear in AI/ML/LLM code.

From **highest** to **lowest** precedence (official order — January 2026):

| Priority | Operators                                      | Description / Common Name                        | Associativity     | AI/ML/LLM Relevance & Gotchas                                                                 |
|----------|------------------------------------------------|--------------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------|
| 1        | `()`                                           | Parentheses                                      | —                 | Your best protection tool — always use them in complex tensor/math expressions               |
| 2        | `**`                                           | Exponentiation (power)                           | **Right-to-left** | Very common in activation functions, attention scores, normalization (e.g. `x ** 0.5`)      |
| 3        | `+x`, `-x`, `~x`                               | Unary plus, unary minus, bitwise NOT             | Right-to-left     | Careful with `-x ** 2` → `-(x**2)` vs `(-x)**2`                                               |
| 4        | `*`, `@`, `/`, `//`, `%`                       | Multiplication, matrix mul, div, floor div, mod  | Left-to-right     | `@` = matrix multiplication — **extremely common** in PyTorch/TensorFlow/LLM layers         |
| 5        | `+`, `-`                                       | Addition, subtraction                            | Left-to-right     | Normal math — but watch out when mixed with `@` or broadcasting                              |
| 6        | `<<`, `>>`                                     | Bitwise left/right shift                         | Left-to-right     | Rare in modern deep learning, more in low-level optimizations or token ids                   |
| 7        | `&`                                            | Bitwise AND                                      | Left-to-right     | Used in masking operations (attention masks, padding masks)                                  |
| 8        | `^`                                            | Bitwise XOR                                      | Left-to-right     | Occasionally in custom hashing or bitwise tricks                                              |
| 9        | `|`                                            | Bitwise OR                                       | Left-to-right     | Used in some mask combinations                                                                |
| 10       | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons + identity + membership | Chaining (left-to-right) | Very frequent in conditions, masking, shape checks                                            |
| 11       | `not x`                                        | Logical NOT                                      | Right-to-left     | Careful — higher than `and`/`or`                                                              |
| 12       | `and`                                          | Logical AND (short-circuit)                      | Left-to-right     | Very common in conditions — **short-circuits** (important for performance & safety)         |
| 13       | `or`                                           | Logical OR (short-circuit)                       | Left-to-right     | Also short-circuits — common in default value patterns                                        |
| 14       | `if – else`                                    | Conditional expression (ternary)                 | Right-to-left     | `x if condition else y` — frequent in list comprehensions & functional code                  |
| 15       | `:=`                                           | Walrus (assignment expression) — Python 3.8+     | —                 | Increasingly used in ML for inline assignments & performance                                 |
| 16       | `=`, `+=`, `-=`, `*=`, `**=`, etc.             | Assignment operators                             | Right-to-left     | Lowest — almost always last                                                                   |

### Quick Reference — Most Dangerous Patterns in AI/ML/LLM Code

```python
# Classic traps people fall into:

a = -3 ** 2               # -9   (unary minus has LOWER precedence than **)
b = (-3) ** 2             # 9    ← correct / safer

x = 2 + 3 * 4 @ A         # (2 + (3*4)) @ A  ← @ after * but before +
y = 2 + 3 * (4 @ A)       # much clearer

mask = scores > threshold & attention_mask   # Wrong precedence!
mask = (scores > threshold) & attention_mask  # Correct & very common

loss = criterion(output, target) if training else 0   # ternary is low precedence