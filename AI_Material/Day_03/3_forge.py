# ═══════════════════════════════════
#  3_FORGE — Day 03
# ═══════════════════════════════════

# Today's session is about building something real with the INPUT-PROCESS-OUTPUT
# pattern. This project will test everything you've learned so far:
# `print()`, variables, `int()`, `float()`, `str()`, `input()`, string
# manipulation, and basic arithmetic.

# ═══════════════════════════════════
#  PROJECT 1: ROBO-ARM
# ═══════════════════════════════════

# COOL NAME
# ROBO-ARM: A Motion Calculator

# DESCRIPTION
# A Python script that runs on your Raspberry Pi to help you calculate the
# movement of a robotic arm. It solves for one of the key variables in the
# first equation of motion: `v = u + at`. This is a real tool you could use
# to prototype a robotics project, proving that with just a few lines of code,
# you can build tools that have a real-world physical application.

# FEATURES
# - Asks the user which variable they want to solve for: final velocity (v),
#   initial velocity (u), acceleration (a), or time (t).
# - Based on their choice, it asks for the values of the other three variables.
# - It correctly calculates and prints the result with its proper units.
# - It handles floating-point numbers for all inputs.

# SAMPLE INTERACTION
# This is what it should look like when the user wants to solve for 'a' (acceleration).
#
# --- ROBO-ARM: A Motion Calculator ---
# Which variable do you want to solve for? (v, u, a, t): a
#
# --- Solving for Acceleration (a) ---
# The formula is: a = (v - u) / t
#
# Enter final velocity (v) in m/s: 0.5
# Enter initial velocity (u) in m/s: 0.1
# Enter time (t) in seconds: 2
#
# Calculation complete.
# The acceleration (a) is: 0.2 m/s^2

# HINT SYSTEM

# Hint 1: Thinking Direction
# The program has to have different "paths." How can you ask the user which path
# to take at the start? You can't use `if/elif/else` yet. So... maybe you just
# make four separate mini-programs and tell the user which one to comment/uncomment?
# No, that's messy.
#
# Think about the structure. You can have one block of code for solving for 'v',
# one for 'u', and so on. But how do you run only one of them? The simplest way
# without conditions is to just code one path. For this project, just implement
# the path for solving for 'a' (acceleration) as shown in the sample. In a few
# days, we'll learn how to make the program choose the path itself.

# Hint 2: Concept and Approach
# 1. Print the welcome message and ask the user which variable to solve for.
# 2. For now, assume they type 'a' and proceed.
# 3. Print the header for the "Solving for Acceleration" section.
# 4. Use `input()` to get the string values for `v`, `u`, and `t`.
# 5. Use `float()` to convert each of these input strings into a number.
# 6. Perform the calculation `a = (v - u) / t`.
# 7. Use `print()` and `str()` to create the final, formatted output string.
# The core pattern is `input()` -> `float()` -> calculate -> `print()`.

# Hint 3: Structural Skeleton
# (This is not runnable code, just a blueprint for your `3_my_forge.py`)
#
# # Print a welcome message for the main tool
#
# # Ask the user which variable they want to solve for.
# # For now, we will just assume they choose 'a'.
#
# # --- Solving for 'a' ---
# # Print the header for the acceleration section
# # Print the formula that will be used
#
# # Get `v` from the user (input) and store it in a variable
# # Get `u` from the user (input) and store it in a variable
# # Get `t` from the user (input) and store it in a variable
#
# # Convert the string version of v to a float
# # Convert the string version of u to a float
# # Convert the string version of t to a float
#
# # Calculate 'a' using the formula and the float variables
#
# # Print the final result, nicely formatted with units.
# # Remember to cast your calculated 'a' back to a string for concatenation!

# ASSERT TESTS
# This project doesn't use functions yet, so we can't use `assert` tests in the
# same way. The "test" is running your program and checking if your output
# exactly matches the sample interaction for the same inputs.

# EXTENSIONS
# 1. Implement the other three paths: solving for `v`, `u`, and `t`. You can
#    just write them one after the other in the same file.
# 2. Add another calculator for a different equation of motion, like
#    `s = ut + 0.5 * a * t^2`.
# 3. Add a "unit converter" at the start of your program. Ask the user if their
#    velocity is in km/h or m/s. If it's km/h, do the math to convert it to m/s
#    before using it in the physics formula. (1 km/h = 5/18 m/s).

# PROFESSIONAL VIEW
# At a production level, a tool like this wouldn't just be a single script.
# It would be part of a larger library of physics calculations. Each formula
# would be a separate, well-documented function. Instead of crashing on bad input
# (like typing "hello" for velocity), it would use error handling (`try/except`
# blocks) to catch the `ValueError` and give the user a friendly message. It
# would also have a full suite of automated tests (`pytest`) to verify every
# calculation is correct without needing a human to run it manually.

# EMPIRE CONNECTION
# This simple calculator is the direct ancestor of the simulation software used to calculate rocket trajectories, model robotic arm movements, and predict the behavior of complex systems for your AGI to analyze.
