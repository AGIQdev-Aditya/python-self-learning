# ═══════════════════════════════════════════════
#  2_GAUNTLET — Day 01: The Basics
#  Solve every challenge from 2_gauntlet.py here.
# ═══════════════════════════════════════════════

# Today you learned: print(), variables, int, float, str, bool, and type().
# Every problem below tests these concepts.

# ═══════════════════════════════════════════════
#  TIER 1: WARM UP
# ═══════════════════════════════════════════════

# 1. Personal Welcome
# Create a variable `name` with your name.
# Create a variable `city` with your city.
# Print a welcome message using these variables.
#
# EXPECTED OUTPUT:
# Welcome, Aditya! We're glad you're here in Mumbai.

# 2. Rover Status
# A Mars rover sends back data. Create variables for its name, the temperature
# on Mars (as a float), and whether it's active (as a boolean).
# Print these out in a status report.
#
# EXPECTED OUTPUT:
# Rover: Perseverance
# Temperature: -63.5 C
# Status: Active

# 3. Data Type Check
# Create four variables, one for each of the fundamental data types we learned:
# an integer, a float, a string, and a boolean.
# Print the value and the type of each variable.
#
# EXPECTED OUTPUT:
# 42 is a <class 'int'>
# 3.14 is a <class 'float'>
# Hello is a <class 'str'>
# True is a <class 'bool'>

# ═══════════════════════════════════════════════
#  TIER 2: LEVEL UP
# ═══════════════════════════════════════════════

# 4. Kinematics Calculator
# From your HSC Physics, recall the equation of motion: s = ut + 0.5at^2
# Create variables for initial velocity `u` (10 m/s), acceleration `a` (2 m/s^2),
# and time `t` (5 s). Calculate the displacement `s` and print the result.
#
# EXPECTED OUTPUT:
# Displacement (s): 75.0 m

# 5. Ideal Gas Law (Chemistry)
# The Ideal Gas Law is PV = nRT. Let's find the pressure P. P = (nRT) / V.
# Create variables for moles `n` (1 mol), temperature `T` (298 K), volume `V` (22.4 L),
# and the gas constant `R` (0.0821 L·atm/(K·mol)).
# Calculate the pressure `P` and print it.
#
# EXPECTED OUTPUT:
# Pressure (P): 1.0922232142857143 atm

# 6. ASCII Art
# Use multiple `print()` statements to draw a simple rocket ship.
# Get creative! Use different characters.
#
# EXPECTED OUTPUT (example):
#      / 
#     / _ 
#    | ( ) |
#    |  .  |
#    |     |
#   /|/   \| 
#  / | ( ) | 
# |  |  .  |  |
# |  |     |  |
#    '-----'

# 7. Variable Swap
# In the Nexus, we saw that a simple assignment `a = b; b = a` doesn't work.
# How *can* you swap the values of two variables?
# Create two variables, `a` and `b`, with initial values.
# Find a way to swap their values, then print them.
# Hint: You might need a third, temporary variable.
#
# a = 100
# b = 200
#
# EXPECTED OUTPUT:
# a was 100, now is: 200
# b was 200, now is: 100


# ═══════════════════════════════════════════════
#  TIER 3: BEAST MODE
# ═══════════════════════════════════════════════

# 8. Arch Linux `neofetch` Stub
# `neofetch` is a cool Arch Linux tool that displays system info.
# Let's make a simplified, fake version.
# Create variables for your OS, Host, Kernel version, Uptime, and Shell.
# Use `print()` with multiple arguments and the `sep` parameter to format it.
# Make it look as close to a real terminal tool as you can.
#
# EXPECTED OUTPUT:
# OS: Arch Linux
# Host: MyLaptop-9300H
# Kernel: 6.1.9-arch1-1
# Uptime: 4 hours, 21 minutes
# Shell: /bin/bash

# 9. Raspberry Pi Data Packet
# Your Raspberry Pi is sending a data packet as a single stream of text, but
# you know the format. Values are separated by semicolons.
# `packet_string = "1024;3.3;75.4;True"`
# This represents ID;Voltage;Humidity;Status_OK
# For today, you can't "parse" the string automatically.
# You must manually create four separate variables (`packet_id`, `voltage`,
# `humidity`, `status_ok`) and assign them the correct values and, crucially,
# the correct DATA TYPES (`int`, `float`, `float`, `bool`).
# Then print each variable and its type.
#
# EXPECTED OUTPUT:
# Packet ID: 1024 (<class 'int'>)
# Voltage: 3.3 (<class 'float'>)
# Humidity: 75.4 (<class 'float'>)
# Status OK: True (<class 'bool'>)

# 10. AGI Core Diagnostics
# An AGI's status is determined by three factors: logic_core_temp (float),
# memory_usage_percent (float), and anomaly_detected (bool).
# A system is "CRITICAL" if the temperature is over 75.5 C, or if memory usage
# is over 80.0%, or if an anomaly has been detected. Otherwise, it's "STABLE".
#
# You don't know how to write `if` statements yet! So, you must use boolean math.
# Remember `True` is 1 and `False` is 0.
#
# Create three variables for the factors.
# Create three more boolean variables: `is_temp_critical`, `is_mem_critical`,
# `is_anomaly_critical`. Set them to True or False based on the rules.
#
# Now, create a final integer variable `critical_score`. It should be the SUM
# of the three boolean critical variables.
# A score of 0 means stable. Any score greater than 0 means critical.
#
# Set these initial values:
# logic_core_temp = 75.0
# memory_usage_percent = 81.2
# anomaly_detected = False
#
# Calculate the score and print all the diagnostic info.
#
# EXPECTED OUTPUT:
# --- AGI Core Diagnostics ---
# Logic Core Temp: 75.0 C
# Memory Usage: 81.2 %
# Anomaly Detected: False
# --- Status ---
# Temp Critical: False
# Mem Critical: True
# Anomaly Critical: False
# --- Final ---
# Critical Score: 1
