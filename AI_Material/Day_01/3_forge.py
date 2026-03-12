# ═══════════════════════════════════════════════
#  3_FORGE — Day 01: Make Something Real
#  Build every project from 3_forge.py here.
# ═══════════════════════════════════════════════

# ═══════════════════════════════════════════════
#  PROJECT 1: "ARC-STAT"
# ═══════════════════════════════════════════════

# COOL NAME
# ARC-STAT: A Simple Terminal Status Display

# DESCRIPTION
# A script that runs in your Arch Linux terminal and displays a clean,
# hard-coded summary of your system's (pretend) status. This project
# focuses on using variables of different types and precise `print()`
# formatting to create a tool that feels like a native command-line utility.

# FEATURES
# - Displays the hostname.
# - Shows (fake) CPU load as a float.
# - Shows (fake) available RAM in MB as an integer.
# - Shows the current user.
# - Displays a "System OK" status as a boolean.
# - Uses separators and spacing to create a clean, readable layout.

# SAMPLE INTERACTION
# (When you run `python 3_my_forge.py` in your terminal)
#
# +----------------------------------+
# |           ARC-STAT v0.1          |
# +----------------------------------+
# | HOSTNAME:   stark-tower-local    |
# | CPU LOAD:   15.7 %               |
# | RAM FREE:   6144 MB              |
# | USER:       addi                 |
# | SYSTEM OK:  True                 |
# +----------------------------------+


# HINT SYSTEM

# Hint 1:
# Think about structure first. How do you print the top border? The bottom
# border? The lines in between? All are just `print()` statements.

# Hint 2:
# Each piece of data (stark-tower-local, 15.7, 6144, etc.) should be stored
# in its own variable with a clear name and the correct data type. The `print`
# statements will then use these variables.

# Hint 3:
# Structural Skeleton:
#
# # 1. Define all your variables up top.
# hostname = "stark-tower-local"
# cpu_load = ...
# # ... and so on for all 5 pieces of data.
#
# # 2. Print the top border.
# print("+----------------------------------+")
#
# # 3. Print the title.
# print("|           ARC-STAT v0.1          |")
#
# # 4. Print the separator.
# print("+----------------------------------+")
#
# # 5. Print the data lines.
# # Use commas in print() to combine text and variables.
# # You will need to manually add spaces to make things line up!
# print("| HOSTNAME:   ", hostname, "   |") # This won't be aligned perfectly.
# # How can you fix the alignment? You'll have to experiment with adding
# # the right number of spaces inside the strings.
#
# # ... print the other data lines ...
#
# # 6. Print the bottom border.
# print("+----------------------------------+")


# ASSERT TESTS
# This project is visual and doesn't have functions to test with `assert`.
# The "test" is whether your output exactly matches the SAMPLE INTERACTION.

# EXTENSIONS
# 1. Colorize It: Research "ANSI escape codes". You can print special character
#    sequences to make your terminal text colored. Can you make the borders
#    blue and the "True" status green?
# 2. Add More Data: Add more fake stats. Disk space (float), Kernel version
#    (string), logged-in users (int). Pad the box to make it fit.
# 3. Create a "Warning" State: Create a second set of variables for a "warning"
#    state (e.g., high CPU load, low RAM). Create a boolean variable called
#    `is_warning_state`. For now, you can manually switch it between `True` and
#    `False` and have your script print the normal or warning data. (Later,
#    we'll learn to do this automatically with `if` statements).

# PROFESSIONAL VIEW
# In the real world, a tool like this wouldn't use hard-coded values. It
# would use a library like `psutil` (a cross-platform process and system
# utilities library). A professional version would call `psutil.cpu_percent()`
# to get the real CPU load and `psutil.virtual_memory().available` to get the
# real available RAM. The core concept is the same, though: get data, store it
# in variables, and present it to the user.

# EMPIRE CONNECTION
# Your AGI, J.A.R.V.I.S., needs a health dashboard. This is the first, tiny
# step towards building that complex, real-time monitoring system.
