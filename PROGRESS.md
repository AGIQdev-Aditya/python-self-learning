Last generated: Day 03

Topics covered so far:
- `print()` function, including `sep` and `end` parameters
- Variables (assignment, naming rules, re-assignment)
- Data Types: `int`, `float`, `str`, `bool`
- `type()` function for checking data types
- The memory model (names pointing to objects)
- String Indexing (Forward and Negative)
- String Slicing (`[start:stop:step]`)
- The `len()` function
- String methods (`.upper()`, `.lower()`, `.strip()`, `.replace()`, `.find()`, `.startswith()`, `.endswith()`, `.join()`)
- The `in` operator for membership testing
- String Immutability
- The `input()` function to get user data as a string
- The `int()`, `float()`, and `str()` functions for type casting
- `ValueError` for invalid casting, `TypeError` for invalid operations

Key concepts carrying forward:
- The INPUT-PROCESS-OUTPUT pattern is the fundamental structure of most programs.
- `input()` always returns a string. You MUST cast it to `int` or `float` before doing math.
- Operations can fail with a `ValueError` (bad data) or `TypeError` (wrong type).
- Always `strip()` user input before casting to handle leading/trailing whitespace.
- Everything is an object in Python.
- Variables are just names/pointers to these objects.
- Strings are immutable sequences.
- Zero-based indexing is the standard.

Next day: 04 — f-strings, formatting, multi-line strings

Position: Day 03 of 43

Notes:
- Aditya seems to have a slight misunderstanding of variable assignment mechanics, specifically how names point to objects. The incorrect variable swap logic in Day 01's work is evidence. Day 03's material included a "Pause and Think" section to directly address this.
- While string methods are being used, the concept of method chaining (e.g., `data.strip().upper()`) might not be fully solidified. This was reinforced in the Day 03 warm-up problems.
- The INPUT-PROCESS-OUTPUT pattern is now central. The core challenge will be remembering to cast `input()` strings to numbers (`int()`/`float()`) before doing math, and casting numbers back to `str()` for concatenation. This will be a major source of `TypeError` and `ValueError` going forward.

FULL CURRICULUM (43 Days):
Day 01 — print(), variables, data types (int, float, str, bool), type()
Day 02 — Strings: indexing, slicing, len(), methods
Day 03 — input(), type casting: int(), float(), str()
Day 04 — f-strings, formatting, multi-line strings
Day 05 — Numbers: arithmetic, modulo, floor division, math module
Day 06 — if / elif / else, comparison operators
Day 07 — Logical operators: and, or, not, nested conditions
Day 08 — while loops, counters, break, continue
Day 09 — for loops, range(), looping strings
Day 10 — CAPSTONE 1
Day 11 — Lists: create, index, slice, nested
Day 12 — List methods: append, remove, pop, sort, reverse
Day 13 — Loops with lists, enumerate()
Day 14 — Tuples and Sets + unpacking
Day 15 — Dictionaries
Day 16 — Loops with dicts
Day 17 — List and dict comprehensions
Day 18 — Functions: define, call, parameters
Day 19 — Return values, scope
Day 20 — CAPSTONE 2
Day 21 — Default args, *args, **kwargs
Day 22 — Recursion
Day 23 — Lambda, map(), filter()
Day 24 — File handling: read, write, append, with statement
Day 25 — Error handling: try, except, finally, custom exceptions
Day 26 — Modules: math, random, os, sys, datetime + write your own module
Day 27 — Debugging: reading errors, stack traces, breakpoint(), print debugging
Day 28 — pip, virtualenv, requests, json basics
Day 29 — APIs deep dive: authentication, headers, real API projects
Day 30 — Type hints + PEP8 + best practices
Day 31 — CAPSTONE 3
Day 32 — OOP 1: classes, objects, __init__, attributes
Day 33 — OOP 2: methods, self, class vs instance variables
Day 34 — OOP 3: inheritance, super()
Day 35 — OOP 4: Magic methods (__str__, __len__, __eq__, __repr__)
Day 36 — Generators and yield
Day 37 — Decorators
Day 38 — Testing: unittest + pytest + assert
Day 39 — DSA basics: linear search, binary search, Big O intro
Day 40 — Standard library mastery + packaging with __init__.py
Day 41 — Web scraping: requests + BeautifulSoup
Day 42 — CAPSTONE 4
Day 43 — FINAL CAPSTONE
