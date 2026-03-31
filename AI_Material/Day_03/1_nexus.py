# ═══════════════════════════════════════════════
#  1_NEXUS — Day 03: The Conversation
#  Open 1_my_nexus.py beside this.
#  Read one section. Type it yourself. Never copy-paste.
# ═══════════════════════════════════════════════

# ⏱ Estimated: 90-120 minutes

# ═══════════════════════════════════════════════
#  CONCEPT 1: The `input()` function
# ═══════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# All our programs so far are monologues. They run from top to bottom and do
# the exact same thing every time. A script to calculate velocity will always
# use the same hard-coded numbers. It's like a movie playing on a loop.
# To be useful, a program must be interactive. It needs to be able to pause,
# ask for information, and then use that information to change what it does next.
# How do we get data from the human user into our running program?

# LAYER 2 — THE CONCEPT
# The `input()` function is Python's way of listening to the user. When you
# call `input()`, your program freezes. It displays a prompt (if you provide
# one), and then waits for the user to type something and press Enter.
# Whatever the user types is then returned by the function as a STRING.

# Simplest possible example:
print("Querying for user's name...")
user_name = input("Enter your name: ") # The text inside is the prompt
print("Processing...")
print("Hello, Captain", user_name)

# LAYER 3 — THE MECHANICS
# When Python hits the line `user_name = input("Enter your name: ")`, this is the sequence:
# 1. It calls the built-in `input()` function.
# 2. The function takes the string `"Enter your name: "` and displays it in the terminal.
# 3. The `input()` function then puts the entire program on PAUSE. It is now waiting for a signal from the operating system that the user has finished typing.
# 4. You type your name, "Aditya", and press the Enter key.
# 5. The terminal captures this sequence of characters.
# 6. The `input()` function receives these characters and bundles them up into a BRAND NEW STRING object: `"Aditya"`.
# 7. This new string object is then RETURNED as the result of the function.
# 8. The assignment operator `=` takes over. The name `user_name` is made to point to this new string object `"Aditya"`.
# 9. The program un-pauses and continues to the next line.

# The most critical part: `input()` ALWAYS gives you a string, no matter what you type. If you type `58`, you don't get the number 58, you get the string `"58"`.

# LAYER 4 — THE WRONG WAY
# This is the single most common mistake with `input()`.

# Mistake: Assuming `input()` gives you a number.
# age = input("How old are you? ")
# age_in_a_decade = age + 10
# print(age_in_a_decade)

# Why it's wrong: Let's say you type `17`. The `age` variable now points to the STRING `"17"`.
# The next line becomes `age_in_a_decade = "17" + 10`.
# Python sees the `+` operator. On one side is a string, on the other is an integer.
# It doesn't know what to do. Should it convert the string to a number? The number to a string?
# Rather than guess, it raises an error.
# Approximate Error: TypeError: can only concatenate str (not "int") to str
# This is the exact same error from Day 1, but now we see a common cause for it.

# The Correct Way (for now):
# We can't do math with it yet, but we can treat it like a string.
age = input("How old are you? ")
print("You have entered the string:", age)
print("The type of the 'age' variable is:", type(age))

# LAYER 5 — REAL EXAMPLES

# Example 1: AGI Assistant Greeting
# A simple, personalized welcome.
print("J.A.R.V.I.S. v0.1 Initializing...")
operator_name = input("Please state your designation: ")
print("Welcome,", operator_name, ". All systems online.")

# Example 2: Arch Linux Script Configurator
# A script might ask for a target directory to run a command.
print("--- Arch Linux Maintenance Script ---")
target_dir = input("Enter target directory for cleanup (e.g., /home/addi/Downloads): ")
print("Now processing files in", target_dir, "...")
# (The script wouldn't actually do anything yet, but it has the info it needs)

# Example 3: Raspberry Pi Threshold Setting
# A script to monitor temperature might need a threshold from the user.
print("--- Raspberry Pi CPU Temp Monitor ---")
print("Connects to sensor and reports if temp exceeds a threshold.")
temp_threshold = input("Enter the maximum safe CPU temperature in C: ")
print("Monitoring enabled. Alert will be triggered if temp exceeds", temp_threshold, "C.")

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Predict the output of the following code if the user enters `10` for the
# first prompt and `25` for the second.

val_1 = input("Enter the first number: ")
val_2 = input("Enter the second number: ")

result = val_1 + val_2
print("The result is:", result)

# Does it print `35`? Or something else? Why?
# This is a direct test of the most critical rule of `input()`.

# LAYER 7 — EDGE CASES AND GOTCHAS

# Gotcha 1: Empty input.
# What happens if the user just presses Enter without typing anything?
# The `input()` function returns an empty string `""`.
# This is valid, and your program needs to be able to handle it (later).
empty_response = input("Just press Enter: ")
print("You entered the string:", empty_response)
print("The length of your input is:", len(empty_response))

# Gotcha 2: The prompt is optional.
# You can call `input()` with no prompt. The program will just pause with a
# blinking cursor, waiting for input. This is less user-friendly.
print("Now waiting for secret key...")
secret_key = input() # No prompt string given
print("Secret key received.")

# LAYER 8 — THE CONNECTION
# Every single command-line interface (CLI) tool you use, from `git` to `pacman`,
# is built on this foundation. They might have complex parsers for arguments
# and flags, but the core interaction is the same: the program receives strings
# from the user and acts on them. In your AGI, `input()` is the first step
# towards a real conversational interface. Later, this simple text input will be
# replaced by speech-to-text engines, but the principle remains: get a string from
# the user, parse it, and determine the user's *intent*.

# ═══════════════════════════════════════════════
#  CONCEPT 2: Type Casting: `int()` and `float()`
# ═══════════════════════════════════════════════

# ⏱ Estimated: 45 minutes

# LAYER 1 — THE PROBLEM
# We can now get input from the user. Great. But it's always a string.
# We tried to add `10` to the user's age and the program crashed.
# We want to perform mathematical calculations, compare numbers, and use numerical
# data. How do we convert the string `"17"` into the integer `17`?

# LAYER 2 — THE CONCEPT
# Type casting (or type conversion) is the process of explicitly changing an
# object from one data type to another. Python provides built-in functions
# that look just like the types themselves: `int()`, `float()`, and `str()`.
# To convert a string to an integer, you pass the string to the `int()` function.

# Simplest possible example:
string_age = input("Enter your age again: ") # e.g., you type 17
integer_age = int(string_age) # This is the conversion step

age_in_a_decade = integer_age + 10
print("In a decade, you will be:", age_in_a_decade)
print("The type of string_age is:", type(string_age))
print("The type of integer_age is:", type(integer_age))

# LAYER 3 — THE MECHANICS
# Let's trace `integer_age = int("17")`:
# 1. Python calls the `int()` function, passing it the string object `"17"`.
# 2. The `int()` function's internal logic kicks in. It examines the characters in the string, one by one: '1', then '7'.
# 3. It recognizes these as valid digits for a base-10 number.
# 4. It performs a calculation to figure out the numerical value (1*10 + 7*1).
# 5. It then creates a brand new object in memory, this time of type `int`, containing the value 17.
# 6. This new integer object is returned from the `int()` function.
# 7. The assignment operator `=` makes the name `integer_age` point to this new integer object `17`.

# The original string `"17"` is still in memory, and `string_age` still points to it.
# We haven't changed any objects; we have created a new one of a different type.

# LAYER 4 — THE WRONG WAY

# Mistake 1: Trying to convert a non-numeric string.
#
# number = int("hello")
#
# Why it's wrong: The `int()` function looks at the string "hello" and has no idea
# how to turn that into a whole number. It's a nonsensical request. Instead of
# failing silently, Python raises a very specific error to tell you exactly what's wrong.
# Approximate Error: ValueError: invalid literal for int() with base 10: 'hello'
# The `ValueError` is new. It means the *value* of the data is wrong for the operation,
# whereas `TypeError` means the *type* of the data is wrong.

# Mistake 2: Trying to convert a float string directly to an integer.
#
# number = int("34.5")
#
# Why it's wrong: The `int()` function is strict. It looks for whole numbers. The moment
# it sees the decimal point `.`, it decides this is not a valid integer string.
# Approximate Error: ValueError: invalid literal for int() with base 10: '34.5'

# The Correct Way (for float strings):
# You must convert it to a float first, then to an int.
float_string = "34.5"
float_number = float(float_string) # Gives the float 34.5
int_number = int(float_number) # Truncates (chops off) the decimal part

print("Original string:", float_string)
print("Converted to float:", float_number)
print("Converted to int:", int_number) # Note that it doesn't round, it truncates!

# LAYER 5 — REAL EXAMPLES

# Example 1: Basic Kinematics Calculator
# Using your HSC Physics knowledge.
print("--- Uniform Acceleration Calculator ---")
u_str = input("Enter initial velocity (m/s): ")
a_str = input("Enter acceleration (m/s^2): ")
t_str = input("Enter time (s): ")

# Convert all inputs to floats, because physics uses decimals.
u = float(u_str)
a = float(a_str)
t = float(t_str)

# Calculate final velocity: v = u + at
v = u + (a * t)

print("Calculated final velocity is:", v, "m/s")

# Example 2: Simple AGI Confidence Check
# Check if an AI's output meets a required confidence level.
required_confidence_str = input("Enter minimum required confidence (0.0 to 1.0): ")
required_confidence = float(required_confidence_str)

# A hard-coded AI score for this example
ai_score = 0.87

print("AI Score:", ai_score)
print("Required Score:", required_confidence)
# Later, we'll learn to use an `if` statement here to see if the AI passed.

# Example 3: Raspberry Pi GPIO Pin Selector
# Your RPi library needs an INTEGER pin number.
print("--- LED Control Panel ---")
pin_str = input("Enter GPIO pin number to activate (e.g., 17): ")

# Convert to integer
pin_number = int(pin_str)

print("OK. Initializing GPIO pin", pin_number, "for output.")
print("Type of pin_number is:", type(pin_number))

# LAYER 7 — EDGE CASES AND GOTCHAS

# Gotcha 1: Converting Booleans
# On Day 1, we learned that `True` is like `1` and `False` is like `0`.
# Type casting makes this explicit.
print("int(True) is:", int(True))     # -> 1
print("int(False) is:", int(False))   # -> 0
print("float(True) is:", float(True))   # -> 1.0
print("float(False) is:", float(False)) # -> 0.0

# Gotcha 2: User input with whitespace.
# What if the user types `"  25  "` with spaces? Good news.
# Python's `int()` and `float()` functions are smart enough to handle this.
spaced_input = "  25  "
number = int(spaced_input) # This works perfectly!
print("Stripped and converted:", number)

# The functions automatically ignore leading and trailing whitespace.
# This is a convenience feature. Note that it only applies to space at the
# beginning or end. `int("2 5")` would still be a ValueError.

# Gotcha 3: Negative numbers
# The conversion functions handle negative signs perfectly.
neg_int = int("-100")
neg_float = float("-34.99")
print("Converted negative int:", neg_int)
print("Converted negative float:", neg_float)

# LAYER 8 — THE CONNECTION
# Data rarely comes in the format you need. In any real system, data cleaning
# and conversion is 80% of the work. You'll get sensor data from a robot as a
# raw string of bytes, and you'll need to convert parts of it into floats. You'll
# scrape data from a website and get numbers as strings that need to be
# converted to integers for analysis. A configuration file for your AGI might
# store all its settings as strings, which your program must convert to the
# correct types (`int`, `float`, `bool`) upon loading. Mastering type casting is
# mastering the art of data preparation.

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Predict the final output of this block of code.
# This one directly revisits the "swap" problem from Day 1.
# On Day 1, you might have tried `a = b; b = a`, which doesn't work.
# Now, we see the correct way to do it. Trace it carefully.

a = "100"
b = "200"

print("Initial a:", a, "type:", type(a))
print("Initial b:", b, "type:", type(b))

# The swap logic
temp = a
a = b
b = temp

print("Final a:", a, "type:", type(a))
print("Final b:", b, "type:", type(b))

# Now consider this variation. What will `c` and `d` be at the end?
c = 100
d = 200
c = d
d = c
# print("Final c:", c)
# print("Final d:", d)

# Why does the first swap work, but the second one doesn't produce a swap?
# This is a deep check on your understanding of assignment.

# ═══════════════════════════════════════════════
#  CONCEPT 3: Type Casting: `str()`
# ═══════════════════════════════════════════════

# ⏱ Estimated: 30 minutes

# LAYER 1 — THE PROBLEM
# We've solved the problem of turning strings into numbers. But what about the
# other way around? We've calculated the final velocity is `88.5`. We want to
# build a nice summary string: `"Final velocity is: 88.5 m/s"`.
# If we try `print("Final velocity is: " + v + " m/s")`, we get the old, familiar
# `TypeError: can only concatenate str (not "float") to str`.
# How do we convert our number back into a string so we can join it with other strings?

# LAYER 2 — THE CONCEPT
# The `str()` function is the universal converter. It can take almost any
# object in Python—an integer, a float, a boolean—and return its string
# representation.

# Simplest possible example:
final_velocity = 88.5
final_velocity_str = str(final_velocity) # The conversion

summary = "Final velocity is: " + final_velocity_str + " m/s"
print(summary)
print("The type of final_velocity is:", type(final_velocity))
print("The type of final_velocity_str is:", type(final_velocity_str))

# LAYER 3 — THE MECHANICS
# When you call `str(88.5)`, Python does the following:
# 1. It sees the float object `88.5`.
# 2. Every well-designed object in Python, including floats, has a built-in
#    protocol for how to represent itself as a string.
# 3. The `str()` function invokes this protocol.
# 4. The float object `88.5` follows the protocol and generates the sequence of characters '8', '8', '.', '5'.
# 5. The `str()` function takes this sequence and creates a new STRING object in memory: `"88.5"`.
# 6. This new string object is returned.

# You can actually do this with any object, which is incredibly useful for debugging.
# If you're ever unsure what a variable is, just `print(str(my_variable))`.

# LAYER 4 — THE WRONG WAY
# It's actually quite hard to go wrong with `str()`, as it's designed to work
# on almost anything. The most common "mistake" is simply forgetting to use it.

# Mistake: Forgetting to cast before concatenation.
score = 1500
# message = "Your final score is: " + score
# print(message)

# Why it's wrong: As we know, this is a `TypeError`. You're asking Python to add
# a string and an integer, which is ambiguous.
# Approximate Error: TypeError: can only concatenate str (not "int") to str

# The Correct Way:
message = "Your final score is: " + str(score)
print(message)

# An alternative, and often cleaner way, is to use the comma in `print`.
# Remember from Day 1, `print` can take multiple arguments and will convert
# them to strings for you and put a space in between.
print("Your final score is:", score) # This is usually easier!

# So why do we need `str()`? For when you are building the string BEFORE printing it.
# The `message` variable above is a good example.

# LAYER 5 — REAL EXAMPLES

# Example 1: Generating a dynamic filename
# You want to save a log file with the current date/time (we'll just use numbers for now).
run_id = 412
temperature_reading = 98.6

# We need to build the filename string: "log_run_412_temp_98.6.txt"
filename = "log_run_" + str(run_id) + "_temp_" + str(temperature_reading) + ".txt"
print("Saving data to:", filename)

# Example 2: Formatting an AGI status report
# You have raw data and need to create a human-readable line of text.
cognitive_cores_active = 8
last_error_code = 0
is_online = True

status_line = "Cores:" + str(cognitive_cores_active) + " | LastErr:" + str(last_error_code) + " | Online:" + str(is_online)
print("AGI STATUS:", status_line)

# Example 3: Sending a command to a device on your Arch Linux system
# Let's say you have a command-line tool that takes a value.
# (This is a simulation of building a command)
base_command = "set_brightness --level="
brightness_level = 0.75 # A float from 0.0 to 1.0

# The command requires a string.
full_command = base_command + str(brightness_level)
print("Executing command in shell:", full_command)

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Predict the final output and the final type of the `report` variable.

core_count = 8
efficiency_rating = 0.981

report = "Status: " + core_count + " cores running at " + efficiency_rating + "%"

# What error will the line above cause?
# How would you fix it using `str()` casting?
# What would the output be if you used commas in print instead, like this?
# print("Status:", core_count, "cores running at", efficiency_rating, "%")

# LAYER 7 — EDGE CASES AND GOTCHAS

# Gotcha 1: `str()` on a string.
# What happens if you call `str()` on something that's already a string?
# Nothing! It just returns the same string. It's safe and doesn't cause an error.
name = "Aditya"
name_str = str(name)
print("Stringifying a string:", name_str)

# Gotcha 2: `str()` on Booleans.
# As you saw in the AGI example, `str(True)` gives the string `"True"` and
# `str(False)` gives `"False"`. This is very predictable.
print("str(True) gives the string:", str(True))
print("The type of str(True) is:", type(str(True)))

# LAYER 8 — THE CONNECTION
# You've now come full circle. You can get data from the user as a string with
# `input()`. You can convert it to a number (`int()`, `float()`) to perform
# calculations. And now you can convert it back to a string (`str()`) to display
# it in a clean, formatted way. This three-step process (INPUT-PROCESS-OUTPUT)
# is the fundamental structure of almost every computer program ever written.
# In robotics, you get sensor data (input), run it through calculations (process),
# and send new commands to the motors (output). In AGI, you get a user query
# (input), search your knowledge base (process), and generate a response (output).
# These type casting functions are the glue that lets you move data between these stages.

# ═══════════════════════════════════════════════
#  WHAT'S COMING TOMORROW
# ═══════════════════════════════════════════════
# We've been building strings with the `+` operator, but it can get clumsy.
# `str(a) + " and " + str(b) + " are values."` is a lot of typing.
# And what about formatting? Our floats print with messy, unpredictable numbers
# of decimal places. How do we get `3.14159265` to display simply as `3.14`?
# Tomorrow, we'll learn the modern, powerful, and clean way to build strings
# in Python: f-strings. They are a game changer for creating readable output,
# and once you learn them, you'll never go back.
# See you on Day 4.
