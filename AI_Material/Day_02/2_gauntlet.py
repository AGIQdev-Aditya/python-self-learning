# ══════════════════════════════════════════════════════════════════════════════
#  2_GAUNTLET — Day 02: String Manipulation & Sequence Protocol
# ══════════════════════════════════════════════════════════════════════════════

# Today you learned: 
# - Zero-based Indexing (Forward and Negative)
# - Slicing syntax: [start:stop:step]
# - The len() function and its O(1) efficiency
# - String methods: .upper(), .lower(), .strip(), .replace(), .find()
# - New methods: .startswith(), .endswith()
# - The 'in' operator for membership testing
# - String Immutability and the Memory Model

# Every problem below tests these. Solve them in 2_my_gauntlet.py.

# ══════════════════════════════════════════════════════════════════════════════
#  TIER 1 — WARM UP
# ══════════════════════════════════════════════════════════════════════════════

# PROBLEM 1: The Initializer
# Given a name variable, extract the first and last letter and print them.
# name = "Aditya"
# EXPECTED OUTPUT: A a

# PROBLEM 2: The Middle Man
# Given a string of odd length (e.g., "STARK"), extract the middle character.
# Hint: Use len() and floor division // to find the index.
# word = "STARK"
# EXPECTED OUTPUT: A

# PROBLEM 3: The Shout Cleaner
# You have a messy command: "   reboot_system_now   ".
# Clean the spaces and make it all uppercase.
# cmd = "   reboot_system_now   "
# EXPECTED OUTPUT: REBOOT_SYSTEM_NOW

# PROBLEM 4: The Fragment Finder
# Check if the word "ERROR" exists in this log string: "SYSTEM_OK: Memory stable."
# print the result (True/False).
# log = "SYSTEM_OK: Memory stable."
# EXPECTED OUTPUT: False

# PROBLEM 4.5: The Stripped Index (TRAP)
# You have: data = "  X-1  ". 
# If you run `print(data.strip()[0])`, what is the output?
# If you run `print(data[0])`, what is the output?
# EXPECTED OUTPUT: 
# X
# (a blank space)

# ══════════════════════════════════════════════════════════════════════════════
#  TIER 2 — LEVEL UP
# ══════════════════════════════════════════════════════════════════════════════

# PROBLEM 5: The Kinematics Parser (HSC Physics)
# You receive a reading: "velocity=25.5m/s".
# Extract just the numerical part (25.5) using slicing.
# reading = "velocity=25.5m/s"
# EXPECTED OUTPUT: 25.5

# PROBLEM 6: The Chemical Symbol (HSC Chemistry)
# Given an element name (which might be lowercase) like "magnesium", 
# create a "symbol" by taking the first character and the 3rd character. 
# Ensure the result is ALWAYS uppercase.
# element = "magnesium"
# EXPECTED OUTPUT: MG

# PROBLEM 7: The Sequence Reverser
# Take the string "AGI_CORE_BETA" and print it backwards.
# EXPECTED OUTPUT: ATEB_EROC_IGA

# PROBLEM 8: The Extension Stripper
# You have a filename: "system_update.tar.gz".
# Remove the ".tar.gz" part and print just "system_update".
# Use .replace() or slicing.
# EXPECTED OUTPUT: system_update

# ══════════════════════════════════════════════════════════════════════════════
#  TIER 3 — BEAST MODE
# ══════════════════════════════════════════════════════════════════════════════

# PROBLEM 9: The Arch Linux Mirror List
# You have a line from /etc/pacman.d/mirrorlist:
# "Server = https://mirror.rackspace.com/archlinux/$repo/os/$arch"
# Extract JUST the domain: "mirror.rackspace.com".
# Use .find() to find the start and end of the domain.
# EXPECTED OUTPUT: mirror.rackspace.com

# PROBLEM 10: The RPi Sensor Packet (Hardcore)
# A Raspberry Pi sensor sends this raw packet: "ID:007|MODULE:KERNEL|TEMP:24.85"
# 1. Extract the Module name and convert it to lowercase.
# 2. Extract the Temperature.
# Challenge: Do not hardcode indexes. Use .find() and slicing.
# EXPECTED OUTPUT: module: kernel, temp: 24.85

# PROBLEM 11: The Secure Connection Checker
# You have a list of URLs (simulated as one string per check):
# "http://insecure.com", "https://stark-industries.com", "ftp://files.org"
# For each one, check if it starts with "https" AND ends with ".com".
# Print the results as Booleans.
# EXPECTED OUTPUT:
# False
# True
# False
