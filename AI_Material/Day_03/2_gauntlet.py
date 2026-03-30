# ═══════════════════════════════════
#  2_GAUNTLET — Day 03
# ═══════════════════════════════════

# Today you learned:
# - The `input()` function to get user data as a string.
# - The `int()` function to cast strings to integers.
# - The `float()` function to cast strings to floats.
# - The `str()` function to cast numbers and other types to strings.
# - The `ValueError` that occurs with invalid casting.
# - Chaining `strip()` with casting functions to handle user input with whitespace.
# Every problem below tests these.

# ═══════════════════════════════════
#  TIER 1: WARM UP
# ═══════════════════════════════════

# Problem 1: Age Calculator
# Ask the user for their birth year and the current year. Calculate and print their age.
#
# EXPECTED INTERACTION:
# Enter your birth year: 2006
# Enter the current year: 2023
# You are 17 years old.


# Problem 2: Rectangle Area
# Ask the user for the length and width of a rectangle. Calculate and print its area.
#
# EXPECTED INTERACTION:
# Enter the length of the rectangle: 15.5
# Enter the width of the rectangle: 10
# The area of the rectangle is: 155.0


# Problem 3: AGI Core Monitor
# An AGI has 16 cognitive cores. Ask the user how many cores are currently active.
# Calculate and print the percentage of cores that are active.
#
# EXPECTED INTERACTION:
# How many AGI cores are active? 12
# AGI Core Usage: 75.0%


# Problem 4: Simple String Repeater
# Ask the user for a word and a number. Print the word repeated that many times.
# HINT: The `*` operator works on strings for repetition.
#
# EXPECTED INTERACTION:
# Enter a word: Stark
# How many times to repeat it? 5
# StarkStarkStarkStarkStark

# ═══════════════════════════════════
#  TIER 2: LEVEL UP
# ═══════════════════════════════════

# Problem 5: Kinematic Energy Calculator (HSC Physics)
# Calculate the kinetic energy of a moving object. The formula is KE = 0.5 * m * v^2
# Ask the user for the mass (in kg) and velocity (in m/s).
#
# EXPECTED INTERACTION:
# --- Kinetic Energy Calculator ---
# Enter mass in kg: 1000
# Enter velocity in m/s: 25
# The kinetic energy is: 312500.0 Joules.


# Problem 6: Ideal Gas Law (HSC Chemistry)
# The Ideal Gas Law is PV = nRT. Let's make a simple calculator for pressure (P).
# P = (nRT) / V. Use R = 8.314 J/(mol·K).
# Ask the user for moles (n), temperature in Kelvin (T), and volume in cubic meters (V).
#
# EXPECTED INTERACTION:
# --- Ideal Gas Law (Pressure) ---
# Enter moles (n): 1
# Enter temperature in Kelvin (T): 298
# Enter volume in cubic meters (V): 0.0224
# The pressure is: 110605.89285714285 Pascals.


# Problem 7: Dynamic Substring Search
# Ask the user for a main string and then a substring to search for.
# Use Day 2's `.find()` method to report where the substring is located.
#
# EXPECTED INTERACTION:
# Enter the main text: The quick brown fox jumps over the lazy dog.
# Enter the substring to find: fox
# The substring 'fox' was found at index 16.

# Problem 8: Whitespace Warrior
# The user will enter a number, but with unpredictable whitespace around it.
# Your code must strip the whitespace *before* converting it to a float and
# then perform a calculation.
#
# EXPECTED INTERACTION:
# Enter a number with messy whitespace:    -99.5
# The number multiplied by 2 is: -199.0


# ═══════════════════════════════════
#  TIER 3: BEAST MODE
# ═══════════════════════════════════

# Problem 9: Arch Linux Mirrorlist Generator
# An Arch Linux mirrorlist URL is composed of a server URL, a country, and a protocol.
# Ask the user for these three pieces of info and construct the final mirrorlist URL.
#
# EXPECTED INTERACTION:
# --- Arch Mirrorlist Generator ---
# Enter the base server URL (e.g., https://arch.mirror.provider.com): https://mirror.cse.iitk.ac.in/archlinux
# Enter the country code (e.g., US, IN): IN
# Enter the protocol (http or https): https
#
# Generated Mirrorlist Entry:
# Server = https://mirror.cse.iitk.ac.in/archlinux/$repo/os/$arch # Country: IN, Protocol: https


# Problem 10: Raspberry Pi CPU Throttling Estimator
# A simplified CPU throttling rule: for every degree Celsius above a "safe" temperature,
# the CPU clock speed is reduced by a certain number of MHz.
# Ask for the safe temp, the current temp, the base clock speed, and the reduction factor.
# Calculate the current, throttled clock speed.
#
# EXPECTED INTERACTION:
# --- RPi Throttling Estimator ---
# Enter base clock speed (in MHz): 1800
# Enter safe temperature (in C): 65
# Enter current temperature (in C): 72
# Enter reduction factor (MHz per degree): 50
#
# Temperature is 7.0 C over the safe limit.
# Clock speed is reduced by 350.0 MHz.
# Current throttled speed: 1450.0 MHz.


# Problem 11: AGI Data Packet Parser
# An AGI sends data packets as a single string: "source:core_A;dest:mem_bus;payload_len:256;crc:4A3B"
# The fields are separated by semicolons `;` and the key/value by colons `:`.
# Your task is to build a tool that can extract the value for a given key.
# This will require multiple steps of string manipulation from Day 2 and user input from today.
#
# HINT:
# 1. Ask the user for the full packet string.
# 2. Ask the user for the key they want to find (e.g., `payload_len`).
# 3. Find the key in the packet string.
# 4. From there, find the very next colon.
# 5. From the colon, find the very next semicolon.
# 6. Slice out the value between the colon and the semicolon.
#
# EXPECTED INTERACTION:
# Enter the full AGI data packet: source:core_A;dest:mem_bus;payload_len:256;crc:4A3B
# Enter the key to extract: payload_len
# The value for 'payload_len' is: 256
