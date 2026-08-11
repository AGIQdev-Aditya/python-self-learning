# AI_Material/Day_03/2_gauntlet_merged.py
# DAY 03 GAUNTLET - Input, Casting, and String Manipulation
#
# THEME:
# You are building a simple robot/AGI control console.
# The console must accept messy human input, clean it, convert it to the
# correct data type, and print exact reports.
#
# STUDENT INSTRUCTIONS:
# - Write your solutions in My_Work/Day_03/2_gauntlet_merged.py.
# - Solve each problem in order.
# - Your printed output must match the expected output exactly.
# - Do not add extra spaces, labels, or blank lines unless shown.
# - Do not paste the expected output as text only.
#   Your code must produce the output.
#
# RULES:
# - Use ONLY Day 01 to Day 03 concepts.
# - Allowed:
#   variables, print(), input(), int(), float(), str(), len(), type(),
#   strip(), upper(), find(), slicing, string concatenation with +,
#   and basic math.
# - NOT allowed:
#   f-strings, try/except, split(), lists, dictionaries, functions,
#   loops, if statements, imports, or external libraries.
# - Assume the user enters valid data unless the problem says otherwise.
# - If input is described as messy, it may have spaces before or after it.
#   You must remove those spaces before casting or processing.

# ALLOWED TOOLS ONLY:
# variables, print(), input(), int(), float(), str(), len(), type(),
# strip(), upper(), find(), slicing, string concatenation with +, basic math

# NOT ALLOWED:
# f-strings, try/except, split(), lists, dictionaries, functions,
# loops, if statements, imports, external libraries

# Do not paste the expected output as plain text — your code must
# actually produce it when run.


# ============================================================
# TIER 1 - DIRECT APPLICATION (30%)
# ============================================================

# PROBLEM 01 - TIER 1
# Task:
# Print the exact name of the error Python would raise if you tried:
#
# int("3.14")
#
# Do not actually cause the error.
# Print the error name as text.
#
# EXPECTED OUTPUT:
# ValueError


# PROBLEM 02 - TIER 1
# Task:
# Ask the user for their age.
# The user may type spaces before or after the age.
#
# Prompt text:
# "Enter your age: "
#
# Requirements:
# 1. Read the age as a string.
# 2. Remove spaces from the left and right.
# 3. Convert it to an integer.
# 4. Print the integer.
# 5. Print its type using type().
#
# EXPECTED INTERACTION:
# Enter your age:   17
# 17
# <class 'int'>


# PROBLEM 03 - TIER 1
# Task:
# Ask the user for a robot command.
# The user may type spaces before or after the command.
#
# Prompt text:
# "Enter robot command: "
#
# Requirements:
# 1. Read the command as a string.
# 2. Remove spaces from the left and right.
# 3. Convert the command to uppercase.
# 4. Print the cleaned command.
# 5. Print its length.
#
# EXPECTED INTERACTION:
# Enter robot command:   stop
# STOP
# 4


# ============================================================
# TIER 2 - COMBINED CONCEPTS (40%)
# ============================================================

# PROBLEM 04 - TIER 2
# Task:
# Ask for two motor states.
# Then swap their values using a temporary variable.
#
# Prompt texts:
# "Enter first motor state: "
# "Enter second motor state: "
#
# Requirements:
# 1. Read both motor states as strings.
# 2. Remove spaces from the left and right of both.
# 3. Swap the values using a temporary variable.
# 4. Print the new first value.
# 5. Print the new second value.
#
# EXPECTED INTERACTION:
# Enter first motor state: ON
# Enter second motor state: OFF
# OFF
# ON


# PROBLEM 05 - TIER 2
# Task:
# Build a kinetic energy calculator.
#
# Physics formula:
# KE = 0.5 * m * v ** 2
#
# Requirements:
# 1. Print the header exactly as shown.
# 2. Ask for mass in kg.
# 3. Ask for velocity in m/s.
# 4. Remove spaces from both inputs.
# 5. Convert both inputs to floats.
# 6. Calculate kinetic energy.
# 7. Print the result using string concatenation with +.
#
# Prompt texts:
# "--- Kinetic Energy Calculator ---"
# "Enter mass in kg: "
# "Enter velocity in m/s: "
#
# EXPECTED INTERACTION:
# --- Kinetic Energy Calculator ---
# Enter mass in kg:   1000
# Enter velocity in m/s:  25
# The kinetic energy is: 312500.0 Joules.


# PROBLEM 06 - TIER 2
# Task:
# Ask for a raw HSC practice score.
#
# Prompt text:
# "Enter raw HSC practice score: "
#
# Requirements:
# 1. Read the score as a string.
# 2. Remove spaces from the left and right.
# 3. Convert it to an integer.
# 4. Add 1 bonus mark.
# 5. Print the adjusted score as part of a complete sentence.
# 6. Use string concatenation with + and str().
#
# EXPECTED INTERACTION:
# Enter raw HSC practice score:  85
# Your adjusted HSC score is: 86


# PROBLEM 07 - TIER 2
# Task:
# Ask the user for a main string and then a substring to search for.
#
# Prompt texts:
# "Enter the main text: "
# "Enter the substring to find: "
#
# Requirements:
# 1. Read both inputs as strings.
# 2. Remove spaces from the left and right of both.
# 3. Use .find() on the cleaned main text.
# 4. Print the result using string concatenation.
# 5. Assume the substring exists.
#
# EXPECTED INTERACTION:
# Enter the main text:   The quick brown fox
# Enter the substring to find:  fox
# The substring 'fox' was found at index 16.


# ============================================================
# TIER 3 - MULTI-STEP PLANNING (30%)
# ============================================================

# PROBLEM 08 - TIER 3
# Task:
# Ask for a machine tag.
#
# Prompt text:
# "Enter machine tag: "
#
# Requirements:
# 1. Read the machine tag as a string.
# 2. Remove spaces from the left and right.
# 3. The first two characters are the machine ID.
# 4. Convert those two characters to an integer and print the ID.
# 5. The remaining characters are the machine name.
# 6. Convert the remaining characters to uppercase and print them.
#
# EXPECTED INTERACTION:
# Enter machine tag:   42nano
# 42
# NANO


# PROBLEM 09 - TIER 3
# Task:
# Create a mission report.
#
# Prompt texts:
# "Enter crew count: "
# "Enter fuel amount: "
#
# Requirements:
# 1. Read the crew count as a string.
# 2. Read the fuel amount as a string.
# 3. Remove spaces from both inputs.
# 4. Convert the crew count to an integer.
# 5. Convert the fuel amount to a float.
# 6. Add 1.0 to the fuel amount as a reserve.
# 7. Print the report exactly as shown below.
# 8. Use string concatenation with + and str().
#
# EXPECTED INTERACTION:
# Enter crew count:  4
# Enter fuel amount:  2.5
# CREW:4
# FUEL:2.5
# RESERVE:3.5
# STATUS:READY


# PROBLEM 10 - TIER 3
# Task:
# An AGI sends data packets as a single string.
# Fields are separated by semicolons (;).
# Keys and values are separated by colons (:).
#
# Example packet:
# source:core_A;dest:mem_bus;payload_len:256;crc:4A3B
#
# Prompt texts:
# "Enter full AGI packet: "
# "Enter key to extract: "
#
# Requirements:
# 1. Ask for the full packet string.
# 2. Ask for the key to extract.
# 3. Remove spaces from both inputs.
# 4. Find the start index of the key.
# 5. Find the colon immediately after that key.
# 6. Find the semicolon immediately after that colon.
# 7. Slice the value between the colon and the semicolon.
# 8. Cast the sliced value to an integer.
# 9. Print the result using string concatenation.
#
# Assumptions:
# - The packet is valid.
# - The requested key appears exactly once.
# - The requested key is not the last field.
# - The value can be safely converted to an integer.
# - Do not use .split(). Use .find() and slicing.
#
# EXPECTED INTERACTION:
# Enter full AGI packet:  source:core_A;dest:mem_bus;payload_len:256;crc:4A3B
# Enter key to extract:  payload_len
# The integer value for 'payload_len' is: 256


# ============================================================
# SELF-CHECK BEFORE SUBMITTING
# ============================================================
# - Did you strip messy input before casting or processing?
# - Did you use + concatenation instead of f-strings?
# - Did you avoid try/except?
# - Did you avoid .split()?
# - Did you match capitalization exactly?
# - Did you match punctuation exactly?
# - Did you avoid extra spaces in printed output?
# - Did you convert numbers with int() or float() when needed?
# - Did you use str() when concatenating numbers with text?
# - Did your code produce the output instead of just printing fixed text?


# ============================================================
# SELF-CHECK BEFORE SUBMITTING
# ============================================================
# - Did you strip messy input before casting or processing?
# - Did you use + concatenation instead of f-strings?
# - Did you match capitalization and punctuation exactly?
# - Did you avoid extra/missing spaces in printed output?
# - Did you use str() when concatenating numbers with text?
