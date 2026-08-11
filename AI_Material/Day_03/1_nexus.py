# AI_Material/Day_03/1_nexus.py
# TODAY IS DAY 03 - input(), type casting: int(), float(), str()
# BOUNDARY: Day 01 -> Day 03 only
# TOPIC LOCK: This file teaches only Day 03 concepts.
# STYLE: Master class, not cheatsheet. Deep understanding. Learn by doing.

# ============================================================
# HOW TO USE THIS NEXUS FILE
# ============================================================
# 1. Read one section at a time.
# 2. Run the file after each small change.
# 3. This file runs without waiting for keyboard input.
# 4. Real input() practice lines are commented at the end.
# 5. When you practice live input, uncomment one block at a time.
#
# Example of real input:
# name = input("Enter your name: ")
#
# In this file, many examples use simulated input like this:
# name = "Aditya"  # simulated input()
#
# This lets you study the mechanics first, then practice live input.
#
# RUN SAFETY:
# - No active line in this file waits for input().
# - All crashing examples are kept inside comments.
# - You can run this file safely from start to finish.


print("========================================")
print("DAY 03 NEXUS - INPUT AND TYPE CASTING")
print("========================================")
print("Today we answer three big questions:")
print("1. How does Python receive data from a user?")
print("2. Why is user data always text at first?")
print("3. How do we safely turn text into numbers?")
print()


# ============================================================
# CONCEPT 1 - input() ALWAYS RETURNS A STRING
# ============================================================

print("--- CONCEPT 1: input() always returns a string ---")
print()

# ------------------------------------------------------------
# 1) THE PROBLEM
# ------------------------------------------------------------
# A program needs information from the outside world.
#
# Examples:
# - A user types their name.
# - An operator types a robot speed.
# - A scientist types a fuel amount.
#
# Python needs a simple way to pause the program and wait for
# the keyboard. That tool is input().

# ------------------------------------------------------------
# 2) THE CONCEPT
# ------------------------------------------------------------
# input() does three things:
#
# 1. It shows a prompt to the user.
# 2. It waits for the user to type something and press Enter.
# 3. It returns what the user typed as a STRING.
#
# Important rule:
# input() ALWAYS returns a str object.
#
# Even if the user types:
# 42
# Python receives:
# "42"
#
# That is text, not a number.

# ------------------------------------------------------------
# 3) THE MECHANICS (MEMORY)
# ------------------------------------------------------------
# When you write:
#
# name = input("Enter your name: ")
#
# Python does this:
#
# KEYBOARD -> text characters -> string object -> variable points to object
#
# Memory picture:
#
# name ----> "Aditya"
#
# The variable name is NOT a box containing a person.
# It is a name tag pointing to a string object.
#
# If the user types 42:
#
# age_text = input("Enter age: ")
#
# Memory picture:
#
# age_text ----> "42"
#
# The object is still a string.

# MEMORY BUG EXAMPLE
# This reinforces Day 01: variables are names pointing to objects.

mission = "Moon"
target = mission
mission = "Mars"

print("Memory bug example:")
print("mission:", mission)
print("target:", target)
print()
print("Why is target still Moon?")
print("Because target points to the old string object.")
print("Reassigning mission makes mission point to a new object.")
print("It does NOT change target.")
print()

# ------------------------------------------------------------
# 4) THE WRONG WAY
# ------------------------------------------------------------
# Wrong thinking:
# "If the user types a number, Python automatically knows it is a number."
#
# That is false.

# This would be wrong:
#
# age = input("Enter age: ")
# print(age + 1)
#
# If the user types 17, age is "17".
# Python tries to do:
# "17" + 1
#
# That causes TypeError:
# TypeError: can only concatenate str (not "int") to str
#
# Python is not being mean. It is being exact.
# Text and numbers are different kinds of objects.

# ------------------------------------------------------------
# 5) REAL EXAMPLES (3+, progressive)
# ------------------------------------------------------------

# Example 1: Simulated name input
# In a real terminal, you could use:
# name = input("Enter your name: ")

name = "Aditya"  # simulated input()
print("Example 1 - name input")
print("Hello,", name)
print("Type of name:", type(name))
print()

# Example 2: Simulated age input
# In a real terminal, you could use:
# age_text = input("Enter your age: ")

age_text = "17"  # simulated input()
print("Example 2 - age input")
print("age_text:", age_text)
print("Type of age_text:", type(age_text))
print("Notice: it looks like a number, but it is a string.")
print()

# Example 3: input() removes the Enter key, not extra spaces
# If the user types:
# "   Aditya   "
# input() gives you:
# "   Aditya   "
# The newline from Enter is removed, but spaces remain.

raw_name = "   Aditya   "  # simulated messy user input
clean_name = raw_name.strip()
print("Example 3 - messy spaces")
print("raw_name:", raw_name)
print("clean_name:", clean_name)
print("len(raw_name):", len(raw_name))
print("len(clean_name):", len(clean_name))
print()

# Example 4: Method chaining practice
# Day 02 taught string methods.
# Day 03 reinforces chaining them.

raw_command = "  launch  "
clean_command = raw_command.strip().upper()
print("Example 4 - method chain")
print("raw_command:", raw_command)
print("clean_command:", clean_command)
print()

# ------------------------------------------------------------
# 6) PAUSE AND THINK
# ------------------------------------------------------------
# ⏱ PAUSE AND THINK
#
# 1. If a user types 42, why does input() return "42" instead of 42?
#
# 2. Why is this dangerous?
#    age = input("Age: ")
#    print(age + 1)
#
# 3. What is the difference between these two objects?
#    "42"
#    42
#
# 4. If mission = "Moon" and target = mission,
#    then mission = "Mars",
#    why does target stay "Moon"?
#
# Write your answers in My_Work/Day_03/1_nexus_notes.py

# ------------------------------------------------------------
# 7) EDGE CASES (include weak areas)
# ------------------------------------------------------------

print("Edge cases for input():")
print()

# Edge Case 1: Empty input
empty_text = ""  # user pressed Enter without typing
print("Empty input:")
print("empty_text:", empty_text)
print("len(empty_text):", len(empty_text))
print("type(empty_text):", type(empty_text))
print()

# Edge Case 2: Spaces only
space_text = "     "  # user typed spaces
print("Spaces only:")
print("len(space_text):", len(space_text))
print("len(space_text.strip()):", len(space_text.strip()))
print()

# Edge Case 3: Leading zeros stay as text
code_text = "007"
print("Leading zeros:")
print("code_text:", code_text)
print("type(code_text):", type(code_text))
print("If we cast this to int later, the zeros disappear.")
print("But as a string, they are still there.")
print()

# Edge Case 4: Method chaining order matters
dirty_code = "  r03  "
print("Method chaining order:")
print("dirty_code:", dirty_code)
print("dirty_code.strip().upper():", dirty_code.strip().upper())
print("dirty_code.upper().strip():", dirty_code.upper().strip())
print()
print("Both can work here, but strip() is usually best first")
print("when you want to remove useless spaces before processing.")
print()

# ------------------------------------------------------------
# 8) SYSTEM CONNECTION
# ------------------------------------------------------------
# AI connection:
# When you talk to an AI, your message first arrives as text.
# The system must parse that text before it can understand intent.
#
# Linux connection:
# Many Linux commands read standard input as text.
# Text in, text out is the Unix way.
#
# Robotics connection:
# A robot may receive commands like:
# "MOVE 20"
# The robot controller must convert the useful part into a number
# before it can control motors.
#
# Space connection:
# A ground operator may send a command as text.
# The spacecraft software must validate and convert it safely.
# A bad conversion can cause mission failure.

print("Concept 1 complete.")
print("Rule: input() always gives a string.")
print()


# ============================================================
# CONCEPT 2 - TYPE CASTING: int(), float(), str()
# ============================================================

print("--- CONCEPT 2: int(), float(), str() ---")
print()

# ------------------------------------------------------------
# 1) THE PROBLEM
# ------------------------------------------------------------
# User data arrives as text.
# But math needs numbers.
#
# So we need a way to convert:
# "42" -> 42
# "3.14" -> 3.14
#
# We also need the reverse:
# 42 -> "42"
# because text output needs strings.

# ------------------------------------------------------------
# 2) THE CONCEPT
# ------------------------------------------------------------
# Python gives us converter functions:
#
# int("42")     -> 42
# float("3.14") -> 3.14
# str(42)       -> "42"
#
# These functions try to create a NEW object of the requested type.
#
# int() creates an integer.
# float() creates a decimal number.
# str() creates a string.
#
# If conversion is impossible, Python raises an error.

# ------------------------------------------------------------
# 3) THE MECHANICS (MEMORY)
# ------------------------------------------------------------
# Example:
#
# text_number = "42"
# real_number = int(text_number)
#
# Memory picture:
#
# text_number ----> "42"   (string object)
# real_number ----> 42     (integer object)
#
# int() did NOT change the original string.
# It created a new integer object.
#
# This is important:
# Casting does not edit the original object.
# Casting creates a new object if possible.

# Memory proof:

text_number = "42"
real_number = int(text_number)

print("Memory proof for casting:")
print("text_number:", text_number)
print("type(text_number):", type(text_number))
print("real_number:", real_number)
print("type(real_number):", type(real_number))
print()

# MEMORY BUG EXAMPLE
# Casting does not link variables magically.

raw_value = "100"
number_value = int(raw_value)
raw_value = "999"

print("Memory bug example with casting:")
print("raw_value:", raw_value)
print("number_value:", number_value)
print()
print("number_value is still 100.")
print("Changing raw_value later does not change number_value.")
print("They point to different objects.")
print()

# ------------------------------------------------------------
# 4) THE WRONG WAY
# ------------------------------------------------------------
# Wrong Way 1:
# Forcing impossible text into int().
#
# int("forty")
# This causes:
# ValueError: invalid literal for int() with base 10: 'forty'
#
# Wrong Way 2:
# Trying to turn a decimal string directly into int().
#
# int("3.14")
# This causes:
# ValueError: invalid literal for int() with base 10: '3.14'
#
# If you want 3.14 as a number, use float("3.14").
#
# Wrong Way 3:
# Concatenating text and numbers directly.
#
# age = 17
# print("Next year you will be " + age + 1)
#
# This causes TypeError because Python cannot add string + int.
# You must convert numbers to strings before concatenation.

# ------------------------------------------------------------
# 5) REAL EXAMPLES (3+, progressive)
# ------------------------------------------------------------

# Example 1: String to integer
score_text = "95"
score_value = int(score_text)

print("Example 1 - string to integer")
print("score_text:", score_text)
print("type(score_text):", type(score_text))
print("score_value:", score_value)
print("type(score_value):", type(score_value))
print("score_value + 1:", score_value + 1)
print()

# Example 2: String to float
fuel_text = "3.5"
fuel_value = float(fuel_text)

print("Example 2 - string to float")
print("fuel_text:", fuel_text)
print("type(fuel_text):", type(fuel_text))
print("fuel_value:", fuel_value)
print("type(fuel_value):", type(fuel_value))
print("fuel_value + 1.0:", fuel_value + 1.0)
print()

# Example 3: Number to string
age_value = 17
age_next_year = age_value + 1
message = "Next year you will be " + str(age_next_year)

print("Example 3 - number to string")
print("age_value:", age_value)
print("type(age_value):", type(age_value))
print("age_next_year:", age_next_year)
print("type(age_next_year):", type(age_next_year))
print("message:", message)
print("type(message):", type(message))
print()

# Example 4: Casting creates separate objects
raw_speed = "80"
speed_value = int(raw_speed)
raw_speed = "120"

print("Example 4 - casting creates separate objects")
print("raw_speed:", raw_speed)
print("speed_value:", speed_value)
print("speed_value stayed 80 because it points to its own int object.")
print()

# ------------------------------------------------------------
# 6) PAUSE AND THINK
# ------------------------------------------------------------
# ⏱ PAUSE AND THINK
#
# 1. Why does int("3.14") fail?
#
# 2. Why does float("3") work?
#
# 3. What is the difference between:
#    "100" + "1"
#    and
#    100 + 1
#
# 4. Why must we use str() when building this message?
#    "Score: " + str(score_value)
#
# Write your answers in My_Work/Day_03/1_nexus_notes.py

# ------------------------------------------------------------
# 7) EDGE CASES (include weak areas)
# ------------------------------------------------------------

print("Edge cases for casting:")
print()

# Edge Case 1: int() ignores surrounding whitespace
padded_number = "   7   "
print("padded_number:", padded_number)
print("int(padded_number):", int(padded_number))
print("But stripping first is still a professional habit.")
print()

# Edge Case 2: Negative numbers
negative_text = "-3"
negative_number = int(negative_text)
print("negative_text:", negative_text)
print("negative_number:", negative_number)
print("type(negative_number):", type(negative_number))
print()

# Edge Case 3: float() can convert whole-number text
whole_text = "3"
whole_float = float(whole_text)
print("whole_text:", whole_text)
print("whole_float:", whole_float)
print("type(whole_float):", type(whole_float))
print()

# Edge Case 4: Decimal strings cannot go directly to int()
decimal_text = "3.14"
print("decimal_text:", decimal_text)
print("float(decimal_text):", float(decimal_text))
print("int(decimal_text) would cause ValueError.")
print()

# Edge Case 5: Empty text fails
empty = ""
print("empty:", empty)
print("int(empty) would cause ValueError.")
print("float(empty) would also cause ValueError.")
print()

# Edge Case 6: str() always creates text
number = 42
text = str(number)
print("number:", number)
print("type(number):", type(number))
print("text:", text)
print("type(text):", type(text))
print()

# ------------------------------------------------------------
# 8) SYSTEM CONNECTION
# ------------------------------------------------------------
# AI connection:
# Models receive text. If a user says:
# "Set temperature to 0.7"
# the system must extract "0.7" and cast it to float.
#
# Linux connection:
# Configuration files and terminal input are text.
# Programs cast text into numbers before calculations.
#
# Robotics connection:
# A motor controller needs numbers, not words.
# If a command says:
# "SPEED 55"
# the robot must convert "55" into 55.
#
# Space connection:
# Telemetry often arrives as text.
# Engineers cast values into floats before graphing or analysis.
# But casting must be careful. Bad data can break a pipeline.

print("Concept 2 complete.")
print("Rule: cast text to numbers before math.")
print("Rule: cast numbers to strings before concatenation.")
print()


# ============================================================
# CONCEPT 3 - INPUT-PROCESS-OUTPUT
# ============================================================

print("--- CONCEPT 3: INPUT-PROCESS-OUTPUT ---")
print()

# ------------------------------------------------------------
# 1) THE PROBLEM
# ------------------------------------------------------------
# Real programs are not one random line of code.
# They usually follow a pattern:
#
# 1. Get data.
# 2. Process data.
# 3. Show result.
#
# This is called INPUT-PROCESS-OUTPUT.
#
# Day 03 is where this pattern becomes real.

# ------------------------------------------------------------
# 2) THE CONCEPT
# ------------------------------------------------------------
# The pattern is:
#
# INPUT:
# Get raw data, usually as a string.
#
# PROCESS:
# Clean it, cast it, and calculate.
#
# OUTPUT:
# Print a useful result.
#
# For user input, the professional version is:
#
# raw_text = input("Prompt: ")
# clean_text = raw_text.strip()
# number = int(clean_text)       # or float(clean_text)
# result = number + 1
# print("Result:", result)

# ------------------------------------------------------------
# 3) THE MECHANICS (MEMORY)
# ------------------------------------------------------------
# Suppose the user types:
# " 21 "
#
# Step-by-step memory:
#
# memory_raw_age = " 21 "
# memory_raw_age ----> " 21 "
#
# memory_clean_age = memory_raw_age.strip()
# memory_clean_age ----> "21"
#
# memory_age = int(memory_clean_age)
# memory_age ----> 21
#
# memory_age_next_year = memory_age + 1
# memory_age_next_year ----> 22
#
# Each variable points to its own object.
# That is why we can track the transformation clearly.

memory_raw_age = " 21 "
memory_clean_age = memory_raw_age.strip()
memory_age = int(memory_clean_age)
memory_age_next_year = memory_age + 1

print("INPUT-PROCESS-OUTPUT memory chain:")
print("memory_raw_age:", memory_raw_age)
print("memory_clean_age:", memory_clean_age)
print("memory_age:", memory_age)
print("memory_age_next_year:", memory_age_next_year)
print()

# VARIABLE SWAP REMINDER
# This reinforces Day 01 variable assignment.
# A correct swap uses a temporary name.

left_motor = "ON"
right_motor = "OFF"

temp = left_motor
left_motor = right_motor
right_motor = temp

print("Variable swap reminder:")
print("left_motor:", left_motor)
print("right_motor:", right_motor)
print()
print("Correct swap logic:")
print("temp = left_motor")
print("left_motor = right_motor")
print("right_motor = temp")
print()

# ------------------------------------------------------------
# 4) THE WRONG WAY
# ------------------------------------------------------------
# Wrong Way 1:
# Doing math before casting.
#
# raw = input("Enter a number: ")
# result = raw + 1
#
# This causes TypeError because raw is a string.
#
# Wrong Way 2:
# Forgetting to strip messy input.
#
# If the user types:
# " GO "
# and you search for "GO" without stripping,
# positions may be wrong.

dirty_command = " GO "
print("Wrong-way reminder: forgetting strip")
print("dirty_command:", dirty_command)
print("dirty_command.find('GO'):", dirty_command.find("GO"))
print("dirty_command.strip().find('GO'):", dirty_command.strip().find("GO"))
print()

# Wrong Way 3:
# Assuming all user text is valid.
#
# User may type:
# ""
# "abc"
# "3.14" when you wanted int
#
# These can cause ValueError.
# Later in the course, you will learn professional error handling.
# Today, your job is to know that bad input is normal.

# ------------------------------------------------------------
# 5) REAL EXAMPLES (3+, progressive)
# ------------------------------------------------------------

# Example 1: Clean a name
# Real terminal version:
# user_raw_name = input("Enter your name: ")

user_raw_name = "  aditya  "  # simulated input()
user_clean_name = user_raw_name.strip().upper()

print("Example 1 - clean a name")
print("user_raw_name:", user_raw_name)
print("user_clean_name:", user_clean_name)
print()

# Example 2: Age next year
# Real terminal version:
# user_raw_age = input("Enter your age: ")

user_raw_age = " 17 "  # simulated input()
user_clean_age = user_raw_age.strip()
user_age = int(user_clean_age)
user_age_next_year = user_age + 1

print("Example 2 - age next year")
print("user_raw_age:", user_raw_age)
print("user_clean_age:", user_clean_age)
print("user_age:", user_age)
print("user_age_next_year:", user_age_next_year)
print("Output message: You will be " + str(user_age_next_year) + " next year.")
print()

# Example 3: Robot throttle
# Real terminal version:
# raw_throttle = input("Enter throttle percent: ")

raw_throttle = " 87 "  # simulated input()
throttle = int(raw_throttle.strip())
throttle_next = throttle + 1

print("Example 3 - robot throttle")
print("raw_throttle:", raw_throttle)
print("throttle:", throttle)
print("throttle_next:", throttle_next)
print("Robot command:", "MOVE AT " + str(throttle))
print()

# Example 4: Space fuel reserve
# Real terminal version:
# raw_fuel = input("Enter fuel amount: ")

raw_fuel = " 3.5 "  # simulated input()
fuel = float(raw_fuel.strip())
fuel_with_reserve = fuel + 1.0

print("Example 4 - space fuel reserve")
print("raw_fuel:", raw_fuel)
print("fuel:", fuel)
print("fuel_with_reserve:", fuel_with_reserve)
print("Fuel status:", "READY WITH " + str(fuel_with_reserve))
print()

# Example 5: Full INPUT-PROCESS-OUTPUT with print parameters
raw_status = "  system check  "
clean_status = raw_status.strip().upper()

print("Example 5 - output formatting from Day 01")
print("Status:", clean_status)
print("A", "B", "C", sep=" | ")
print("Loading", end="...")
print("Done")
print()

# ------------------------------------------------------------
# 6) PAUSE AND THINK
# ------------------------------------------------------------
# ⏱ PAUSE AND THINK
#
# 1. Why do we strip() before casting?
#
# 2. Why is this safer?
#    number = int(raw_text.strip())
#    instead of:
#    number = int(raw_text)
#
# 3. What happens if raw_text is "abc"?
#
# 4. What happens if raw_text is "3.14" and we use int()?
#
# 5. In the INPUT-PROCESS-OUTPUT pattern, where does str() usually belong?
#
# Write your answers in My_Work/Day_03/1_nexus_notes.py

# ------------------------------------------------------------
# 7) EDGE CASES (include weak areas)
# ------------------------------------------------------------

print("Edge cases for INPUT-PROCESS-OUTPUT:")
print()

# Edge Case 1: Messy command
edge_raw_command = "   launch   "
edge_command = edge_raw_command.strip().upper()
print("edge_raw_command:", edge_raw_command)
print("edge_command:", edge_command)
print()

# Edge Case 2: Negative integer text
raw_temperature = "-5"
temperature = int(raw_temperature.strip())
temperature_next = temperature + 1
print("raw_temperature:", raw_temperature)
print("temperature:", temperature)
print("temperature_next:", temperature_next)
print()

# Edge Case 3: Decimal text must use float()
raw_sensor = "2.75"
sensor = float(raw_sensor.strip())
sensor_next = sensor + 1.0
print("raw_sensor:", raw_sensor)
print("sensor:", sensor)
print("sensor_next:", sensor_next)
print()

# Edge Case 4: Invalid text expectations
bad_int_text = "abc"
print("bad_int_text:", bad_int_text)
print("int(bad_int_text) would raise ValueError.")
print()

bad_decimal_for_int = "9.99"
print("bad_decimal_for_int:", bad_decimal_for_int)
print("int(bad_decimal_for_int) would raise ValueError.")
print("float(bad_decimal_for_int) would work.")
print()

# Edge Case 5: Empty input
empty_input = ""
print("empty_input:", empty_input)
print("int(empty_input) would raise ValueError.")
print("Professional code expects messy users.")
print()

# ------------------------------------------------------------
# 8) SYSTEM CONNECTION
# ------------------------------------------------------------
# AI connection:
# A real AI system receives raw text input.
# Then it processes that text.
# Then it produces output.
# You just built a tiny version of that pipeline.
#
# Linux connection:
# Command-line tools often follow INPUT-PROCESS-OUTPUT.
# Input: file or keyboard text
# Process: transform data
# Output: terminal text
#
# Robotics connection:
# Robot control loops often follow:
# SENSOR INPUT -> PROCESS -> ACTION OUTPUT
# Today we used human input instead of sensors,
# but the structure is the same.
#
# Space connection:
# Mission software must handle dirty input.
# A single unclean value can break a calculation.
# Strong engineers do not assume data is perfect.
# They clean it, cast it carefully, and check it.

print("Concept 3 complete.")
print("Pattern: INPUT -> PROCESS -> OUTPUT")
print()


# ============================================================
# DAY 03 MASTER RULES
# ============================================================

print("DAY 03 MASTER RULES")
print("1. input() always returns a string.")
print("2. Use int() to convert whole-number text into an integer.")
print("3. Use float() to convert decimal text into a float.")
print("4. Use str() to convert numbers into text.")
print("5. Strip user input before processing.")
print("6. Expect ValueError from bad text-to-number casting.")
print("7. Expect TypeError when mixing strings and numbers incorrectly.")
print("8. Variables are names pointing to objects.")
print("9. Casting creates a new object; it does not edit the original.")
print("10. Real programs follow INPUT-PROCESS-OUTPUT.")
print()


# ============================================================
# LIVE PRACTICE ZONE
# ============================================================
# Uncomment ONE section at a time and run this file in your terminal.
# Do not uncomment everything at once.

# LIVE PRACTICE 1: Name
# raw_name = input("Enter your name: ")
# clean_name = raw_name.strip().upper()
# print("Hello,", clean_name)

# LIVE PRACTICE 2: Age next year
# raw_age = input("Enter your age: ")
# age = int(raw_age.strip())
# age_next_year = age + 1
# print("Next year you will be " + str(age_next_year))

# LIVE PRACTICE 3: Robot throttle
# raw_throttle = input("Enter throttle percent: ")
# throttle = int(raw_throttle.strip())
# print("Throttle accepted:", throttle)

# LIVE PRACTICE 4: Space fuel
# raw_fuel = input("Enter fuel amount: ")
# fuel = float(raw_fuel.strip())
# print("Fuel accepted:", fuel)

# LIVE PRACTICE 5: Break it safely
# Try entering:
# - empty input
# - spaces only
# - "abc"
# - "3.14" into an int() cast
#
# Observe the error messages.
# Errors are not failure. Errors are information.


# ============================================================
# WHAT'S COMING TOMORROW
# ============================================================
# Day 04: f-strings, formatting, multi-line strings
#
# Today you learned the foundation:
# "Age: " + str(age)
#
# Tomorrow you will learn a cleaner way to build output.
# You earned it because you now understand the raw mechanics.
