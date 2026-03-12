# ═══════════════════════════════════════════════
#  1_NEXUS — Day 01: The Core Operations
#  Open 1_my_nexus.py beside this.
#  Read one section. Type it yourself. Never copy-paste.
# ═══════════════════════════════════════════════

# ⏱ Estimated: 30 minutes

# ═══════════════════════════════════════════════
#  CONCEPT 1: The `print()` function
# ═══════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# Imagine you write a program to calculate the trajectory of a rocket.
# The program runs, does thousands of calculations, and then... nothing.
# It finishes, but you can't SEE the final trajectory. You can't check if it's
# correct. You have no way of knowing what happened inside the machine.
# We need a way to make the computer talk back to us.

# LAYER 2 — THE CONCEPT
# The `print()` function is our window into the program's soul. It takes
# whatever you put inside its parentheses and displays it on the screen.
# It's the most fundamental tool for seeing the results of your code.

# Simplest possible example:
print("System online. Welcome, Aditya.")

# LAYER 3 — THE MECHANICS
# What is Python actually doing when you run `print("Hello")`?
# 1. The Python interpreter reads your code line by line.
# 2. It sees the keyword `print`. This is a built-in function it recognizes.
# 3. It looks inside the parentheses `()` to find the *arguments* — the data
#    you want it to work with.
# 4. It finds the sequence of characters `"System online. Welcome, Aditya."`. This is
#    called a "string" of text.
# 5. The `print` function's job is to send these characters to the "standard
#    output" stream, which is, by default, your terminal screen.
# 6. It also adds a special invisible character at the end: a newline.
#    That's why the next time you print, it appears on a new line.

# LAYER 4 — THE WRONG WAY
# Mistakes are how we learn. Here are the most common `print` errors.

# Mistake 1: Forgetting the parentheses (a common error for people coming
# from the older Python 2).
#
# print "This will not work in modern Python"
#
# Why it's wrong: In Python 3 (which we are using), `print` is a function,
# and functions ALWAYS require parentheses `()` to be called, even if there's
# nothing inside them.
# Approximate Error: SyntaxError: Missing parentheses in call to 'print'

# Mistake 2: Mismatched quotes.
#
# print("Hello, world!')
#
# Why it's wrong: A string must start and end with the same type of quote.
# You can use single quotes `'` or double quotes `"`, but you can't mix them
# for the same string. Python gets to the end of the line looking for another
# double quote and can't find it.
# Approximate Error: SyntaxError: EOL while scanning string literal (EOL means End Of Line)

# The Correct Way:
print("This works.")
print('This also works.')

# LAYER 5 — REAL EXAMPLES

# Example 1: Simple status message (like a video game starting)
print("Loading assets...")
print("Establishing neural link...")
print("J.A.R.V.I.S. online.")

# Example 2: Reporting data from a Raspberry Pi sensor (we're simulating for now)
print("Temperature Sensor Reading:")
print(28.5) # Printing a number, not text

# Example 3: Core AGI diagnostic output
print("Cognitive Core Status: Stable")
print("Heuristic Matrix: Optimized")
print("Probability of success: 99.8%")

# LAYER 7 — EDGE CASES AND GOTCHAS (Layer 6 is later)

# Gotcha 1: Printing multiple things.
# `print` can take multiple arguments, separated by commas. It will automatically
# add a space between them when it prints.
print("Mission Time:", 1400, "hours. Status:", "All Clear")

# Gotcha 2: Printing nothing.
# What does an empty print call do? It just prints the newline character.
# This is a simple way to add a blank line for spacing in your output.
print("First line.")
print() # This will print a blank line
print("Third line.")

# Gotcha 3: The `sep` and `end` parameters.
# You can control the separator and what happens at the end.
# Let's create a file path for your Arch Linux system.
print("home", "addi", "python-self-learning", sep="/") # Separator is now '/'

# Let's print a progress bar without jumping to a new line.
print("Processing...", end="")
print("Complete.")
# This prints: Processing...Complete.

# LAYER 8 — THE CONNECTION
# In professional AI systems, you don't just print randomly. You use a
# "logging" framework, which is basically a super-powered version of `print`.
# It allows you to print messages with different severity levels (info, warning,
# error), save them to files, and control them across massive, distributed
# systems. But at its heart, it's the same idea: sending information from the
# program back to the human. Every time you debug a neural network that isn't
# learning, your first tool will be a logger, which is a fancy print.

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Before you run the code, predict the output of these two lines.
# Write down your prediction. Then, run it in `1_my_nexus.py` and see if you were right.

# Prediction 1: What will this line produce?
# print("Core", "Voltage", 1.2, "V")

# Prediction 2: And this one?
# print("STATUS: OK", end=" | ")
# print("SYSTEM: ARMED")

# ═══════════════════════════════════════════════
#  CONCEPT 2: Variables
# ═══════════════════════════════════════════════

# ⏱ Estimated: 45 minutes

# LAYER 1 — THE PROBLEM
# Our last program was static. The values were "hard-coded".
# `print(28.5)` will ONLY ever print 28.5.
# What if we want to run a calculation, and then print the *result*?
# What if we want to ask for the user's name, and then greet them?
# We need a way to store information that can change, be updated, and be
# referred to by a name. We need a memory box.

# LAYER 2 — THE CONCEPT
# A variable is a named storage location in your computer's memory.
# You give it a name, and you use the equals sign `=` (the assignment operator)
# to place a value inside it. The value can be text, a number, or anything else.

# Simplest possible example:
mission_name = "Project Chimera"
mission_duration_hours = 72

print("Starting mission:")
print(mission_name)
print("Estimated duration:")
print(mission_duration_hours)

# LAYER 3 — THE MECHANICS
# This is one of the most important concepts to understand deeply.
# When you write `x = 100`, Python does the following:
# 1. It sees the value `100`. It says, "Ah, this is a whole number, an integer."
# 2. It allocates a small chunk of your computer's RAM to store this value, 100.
#    Think of it like Python creating a new object, the number 100.
# 3. It sees the name `x` and the assignment operator `=`.
# 4. It creates a "name" or "label" called `x`.
# 5. It makes the name `x` act as a pointer, or a reference, to the memory
#    location where the object `100` is stored.
#
# It does NOT put `100` "inside" `x`. This is a crucial distinction. `x` just
# knows the memory address of `100`.
#
# When you later write `print(x)`, Python does this:
# 1. It sees `x`.
# 2. It looks up the name `x` in its internal table of names.
# 3. It follows the pointer from `x` to the object in memory.
# 4. It finds the object is `100`.
# 5. It passes `100` to the `print` function.

# LAYER 4 — THE WRONG WAY

# Mistake 1: Using a variable before it's created.
#
# print(unassigned_variable)
#
# Why it's wrong: Python reads code from top to bottom. If it reaches this
# line and has never seen `unassigned_variable` being assigned a value with `=`,
# it has no idea what memory address to look up. It doesn't exist in its table of names.
# Approximate Error: NameError: name 'unassigned_variable' is not defined

# Mistake 2: Invalid names. Variable names have rules.
# They can contain letters, numbers, and underscores, but they CANNOT start with a number.
# They are also case-sensitive (`age` is different from `Age`).
#
# 1st_mission_target = "Moon" # Starts with a number
# mission-target = "Mars"   # Contains a hyphen, which is the minus operator
#
# Why it's wrong: The interpreter has strict rules for what constitutes a valid
# name, so it can distinguish names from other parts of the syntax like numbers or operators.
# Approximate Error: SyntaxError: invalid syntax

# The Correct Way:
mission_target_1 = "Moon"
mission_target = "Mars"
Age = 21
age = 17 # This is a different variable from Age

# LAYER 5 — REAL EXAMPLES

# Example 1: Basic kinematics (from your HSC Physics)
initial_velocity = 0.0  # m/s
acceleration = 9.8      # m/s^2
time = 10               # seconds
final_velocity = initial_velocity + (acceleration * time)

print("Final velocity after 10s of freefall:")
print(final_velocity)

# Example 2: Simple AGI confidence score
# An AI might assign a confidence score to its prediction.
object_identified = "Cat"
confidence_score = 0.95 # 95% confident

print("AI Prediction:")
print(object_identified)
print("Confidence:")
print(confidence_score)

# Example 3: Raspberry Pi GPIO Pin configuration
# Your RPi has pins you can control. You assign numbers to them.
led_pin = 17
motor_pin_a = 23
motor_pin_b = 24

print("System Configuration:")
print("LED connected to GPIO pin:", led_pin)
print("Motor controller on pins:", motor_pin_a, "and", motor_pin_b)

# LAYER 7 — EDGE CASES AND GOTCHAS

# Gotcha 1: Re-assignment
# A variable can be updated to hold a new value. The old value is "forgotten"
# (unless another variable is still pointing to it). The name now points to a new object.
x = 10
print(x) # Prints 10

x = 20 # The name x now points to a new object, 20. The old 10 is gone.
print(x) # Prints 20

# Gotcha 2: Chaining assignments
# You can assign the same value to multiple variables at once.
a = b = c = "Standby"
# In memory, only ONE string object "Standby" is created.
# The names a, b, and c all point to that same single object.
print(a)
print(b)
print(c)

# Gotcha 3: The `=` sign is NOT for equality.
# In math, `x = x + 1` is impossible. In programming, it's one of the most
# common things you'll do. It's called an "increment".
# It means:
# 1. Look up the value of `counter` (on the right side).
# 2. Add 1 to it.
# 3. Assign the result of that calculation back to the name `counter` (on the left side).
counter = 0
print("Counter:", counter)
counter = counter + 1
print("Counter:", counter)
counter = counter + 1
print("Counter:", counter)

# LAYER 8 — THE CONNECTION
# Variables are the state of a system. The weights and biases in a neural
# network are just millions of variables. The current altitude, velocity, and
# orientation of a SpaceX rocket are stored in variables. In your AGI, the
# entirety of its "knowledge" and "beliefs" about the world will be stored in
# a vast, complex structure of variables. Mastering them is not optional.

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Predict the output of this code block. This is a classic.
# Write down what you think `a` and `b` will be at the end.

a = 100
b = 200

# We're going to try to swap them
a = b
b = a

# print("a is:", a)
# print("b is:", b)

# Think it through step-by-step using the memory model. What does `a` point
# to after the first assignment? What does `b` point to? Then what happens?

# ═══════════════════════════════════════════════
#  CONCEPT 3: Fundamental Data Types
# ═══════════════════════════════════════════════

# ⏱ Estimated: 45 minutes

# LAYER 1 — THE PROBLEM
# We have variables, but what kind of data can they hold? Can they hold a
# trajectory coordinate like 3.14159? A name like "Aditya"? A simple state
# like "on" or "off"? If we just throw data at the computer, it has no idea
# how to interpret it. Is `10` the number ten, or the text characters '1' and '0'?
# A program needs to understand the *type* of data it's working with.

# LAYER 2 — THE CONCEPT
# Python has several built-in data types. We'll focus on the four most
# fundamental ones today. Everything else is built from these.
#
# 1. Integer (`int`): Whole numbers, positive or negative. e.g., `-10`, `0`, `42`.
# 2. Floating-Point Number (`float`): Numbers with a decimal point. e.g., `-3.14`, `99.9`, `0.0`.
# 3. String (`str`): A sequence of text characters, enclosed in `'` or `"`. e.g., `"Hello"`, `'Arch Linux'`.
# 4. Boolean (`bool`): Represents truth values. Can only be one of two things: `True` or `False`.

# Code Examples:
ship_id = 7
launch_angle = 45.7
captain_name = "Aditya"
is_ready = True

print("Ship ID:")
print(ship_id)
print("Launch Angle:")
print(launch_angle)
print("Captain:")
print(captain_name)
print("Ready for Launch:")
print(is_ready)

# LAYER 3 — THE MECHANICS
# Your CPU and RAM treat these types very differently.
# - An `int` is stored in a simple, direct binary representation.
# - A `float` is more complex, stored using a standard (IEEE 754) that splits
#   the number into a sign, an exponent, and a mantissa (the significant digits).
#   This is why they can be imprecise! It's a trade-off for being able to
#   represent a huge range of numbers with decimals.
# - A `str` is stored as a sequence. The variable points to an object that
#   contains information about the string, including its length and a pointer
#   to the memory where the actual characters are stored one after another.
# - A `bool` is really just a special kind of integer. In memory, `True` is
#   stored as `1` and `False` is stored as `0`.

# LAYER 4 — THE WRONG WAY

# Mistake: The `TypeError`. This is the single most common error in Python.
# It happens when you try to perform an operation on two data types that
# don't support it.
#
# status_message = "System uptime: " + 900
#
# Why it's wrong: You're trying to use the `+` operator. For two strings, `+`
# means "join them together" (concatenation). For two numbers, `+` means
# mathematical addition. But what does it mean for a string and a number?
# Python refuses to guess. It's ambiguous. Does the user want to convert "System
# uptime: " to a number? Or convert 900 to a string? Rather than guess wrong,
# it throws an error.
# Approximate Error: TypeError: can only concatenate str (not "int") to str

# The Correct Way (we'll learn more about this later):
# You have to explicitly tell Python what you want.
status_message = "System uptime: 900" # Put the 900 in the string
print(status_message)

# LAYER 5 — REAL EXAMPLES

# Example 1: Spacecraft Telemetry Packet
# A real data packet from a probe would be a mix of types.
packet_id = 1138              # int: Unique identifier
temperature = -170.25           # float: From a sensor on the dark side
system_name = "Propulsion"      # str: The system reporting
status_ok = True                # bool: A simple health check

print("--- INCOMING TELEMETRY ---")
print("Packet:", packet_id)
print("System:", system_name)
print("Temp:", temperature, "C")
print("OK:", status_ok)

# Example 2: AGI Knowledge Base Fragment
# How an AI might store a simple fact.
entity_name = "Earth"
is_planet = True
population = 8000000000       # int
mass_kg = 5.972e24            # float, shorthand for 5.972 * 10^24

print("--- AGI FACT SHEET ---")
print("Entity:", entity_name)
print("Is Planet:", is_planet)
print("Population:", population)
print("Mass (kg):", mass_kg)

# Example 3: Arch Linux Script Variable
# A script to check your disk space
# (This is simplified, we'd use a command to get the real values)
is_root_user = False
device_name = "/dev/sda1"
gb_free = 27.8
files_indexed = 131072

print("--- DISK UTILITY ---")
print("Device:", device_name)
print("Root Access:", is_root_user)
print("GB Free:", gb_free)
print("Files:", files_indexed)

# LAYER 7 — EDGE CASES AND GOTCHAS
# Strings can look like numbers: "123" is a string, not an int. 
# You can't do math with it until you convert it (which we'll learn later).
# Large numbers: Python ints can be as large as your RAM allows! 
# Try printing 2 to the power of 1000: print(2**1000). Python handles it easily.

# LAYER 8 — THE CONNECTION
# In your AGI, everything is a data type. The text you type is a 'str'. 
# The probability of an action is a 'float'. The number of neurons is an 'int'. 
# Whether the system is active is a 'bool'. Understanding these is like 
# understanding the atoms that make up the universe of your program.


# ═══════════════════════════════════════════════
#  CONCEPT 4: The `type()` function
# ═══════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# You have a variable. Maybe it came from a file, a network request, or
# another part of a large program. You *think* it contains a number, but your
# program is crashing with a `TypeError`. How can you be sure? How can you
# inspect the *kind* of data a variable is pointing to?

# LAYER 2 — THE CONCEPT
# The `type()` function is our debugging multi-tool. You give it a variable
# or a value, and it tells you its data type.

# Use it with our telemetry variables:
print("Type of packet_id is:")
print(type(packet_id))
print("Type of temperature is:")
print(type(temperature))
print("Type of system_name is:")
print(type(system_name))
print("Type of status_ok is:")
print(type(status_ok))

# The output `<class 'int'>` means "the type (or class) of this object is int".

# LAYER 3 — THE MECHANICS
# When you call `type(my_variable)`, Python does this:
# 1. It looks up the name `my_variable`.
# 2. It follows the pointer to the object in memory.
# 3. Every object in Python has a little bit of extra information stored with it,
#    including a reference to its "class" or "type".
# 4. The `type()` function reads this information and returns it.
# It's a direct way of asking the object itself, "What are you?"

# LAYER 4 — THE WRONG WAY
# The most common mistake is not doing anything with the result.
#
# type(captain_name)
#
# Why it's "wrong": This line of code runs perfectly! Python dutifully finds
# the type (`<class 'str'>`) and then... throws it away, because you didn't
# tell it to do anything with that information. It doesn't print it, it doesn't
# save it. To see the result, you must pass it to `print()`.

# The Correct Way:
print(type(captain_name))

# LAYER 7 — EDGE CASES AND GOTCHAS

# Gotcha 1: The type of a number you write is obvious.
print(type(10))   # int
print(type(10.0)) # float. The decimal point makes it a float, even if the value is whole.
print(type("10")) # str. The quotes make it a string.

# Gotcha 2: Booleans are secretly integers.
# This is a deep cut. Because `True` is 1 and `False` is 0 in memory, you can
# do math with them! This is sometimes useful, but often just confusing.
# Don't write code like this, but you need to understand it when you see it.
result = True + True # This is 1 + 1
print(result) # Prints 2
print(type(result)) # The result is an integer!

# LAYER 8 — THE CONNECTION
# In professional code, `type()` is used less for printing and more for control.
# An advanced concept is "type checking", where a function says "I only accept
# integers as input." Before running its main logic, it might check `if type(input) is not int: ...`
# and raise an error immediately. This makes programs more robust and easier
# to debug. In static analysis tools that check your code for errors before you
# even run it (a standard in large projects), checking and inferring types is
# their primary job.

# ═══════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ═══════════════════════════════════════════════
# Predict the output, including the TYPE for each of these.

# Prediction 1:
value_a = 5
# print(value_a)
# print(type(value_a))

# Prediction 2:
value_b = 5 / 1
# print(value_b)
# print(type(value_b))

# Prediction 3:
value_c = 6 / 2
# print(value_c)
# print(type(value_c))

# There's a subtle but critical rule being revealed here about the `/` division operator.
# What do you think it is?

# ═══════════════════════════════════════════════
#  WHAT'S COMING TOMORROW
# ═══════════════════════════════════════════════
# We've touched on strings (`str`), but we've only scratched the surface.
# They are one of the most powerful and common data types you'll ever work with.
# Tomorrow, we're going to tear them apart. We'll learn how to access
# individual characters, slice out substrings, find their length, and use
# built-in methods to manipulate them in powerful ways. You'll learn how to
# take a string like "DATA-OK:192.168.1.10" and surgically extract just the IP address.
# It's the first step to parsing real data, and it's essential for everything from
# reading log files on your Arch machine to interpreting commands for your AGI.
# See you on Day 2.
