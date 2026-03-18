# ══════════════════════════════════════════════════════════════════════════════
#  0_IGNITE — Day 02: The Foundation Recap & The Bridge
# ══════════════════════════════════════════════════════════════════════════════

# 1. YESTERDAY IN 2 MINUTES
# ──────────────────────────────────────────────────────────────────────────────
# Namaste, Aditya! Yesterday was about the "Atoms" of Python. You learned that
# `print()` isn't just a command; it's your window into the machine's soul. 
# You met the four fundamental data types: the solid Integers (`int`), the 
# precise but tricky Floats (`float`), the textual Strings (`str`), and the 
# binary logic of Booleans (`bool`).
#
# Most importantly, you learned the "Pointer Model." When you write `x = 10`, 
# `x` is just a label (a name) pointing to an object `10` sitting in your 
# RAM. If you change it to `x = 20`, the label moves. This is the secret 
# to how Python handles memory, and it's what makes it so flexible for 
# building everything from simple scripts on your Arch machine to complex 
# AGI logic.
#
# Quick reminder:
# mission = "Mars"           # A string object is created, 'mission' points to it.
# gravity = 3.71             # A float object is created.
# print(type(gravity))       # Tells you exactly what you're dealing with.

# 2. PROVE YOU REMEMBER
# ──────────────────────────────────────────────────────────────────────────────
# Solve these in a temporary file or your head before moving to 1_nexus.py.
# No looking back at Day 01! Use your i5-9300H brainpower.

# PROBLEM 1: The Telemetry Setup
# Create three variables: `altitude` (int: 100), `velocity` (float: 250.5), 
# and `is_stable` (bool: True). Print them all on one line separated by 
# a " >> " symbol.
# EXPECTED OUTPUT: 100 >> 250.5 >> True

# PROBLEM 2: The Name Swap (The Classic)
# You have: `primary_core = "Core_A"` and `backup_core = "Core_B"`.
# Swap their values so `primary_core` points to "Core_B" and vice versa.
# You MUST use a third temporary variable. Print both at the end.
# EXPECTED OUTPUT: primary: Core_B, backup: Core_A

# PROBLEM 3: The Type Detective
# What is the `type()` of the result of `10 / 2`? 
# And what is the `type()` of `10 // 2`? (Try it in your terminal!)
# EXPECTED OUTPUT: <class 'float'> and <class 'int'>

# PROBLEM 4: Path Builder
# Use `print()` with the `sep` parameter to build this Arch Linux path:
# /home/aditya/projects/agi_alpha
# Hint: Your first argument should be an empty string if you want it to 
# start with a slash!

# 3. BRIDGE
# ──────────────────────────────────────────────────────────────────────────────
# Yesterday, strings were just "labels" or "messages" we printed. Today, we 
# stop treating them as single chunks of text and start treating them as 
# SEQUENCES. Think of a string like a train: it has a total length, and 
# every carriage (character) has a specific position (index).
#
# Why does this matter? Because in the real world, data is messy. Your 
# Raspberry Pi might send you a string like "TEMP:24.5C". To use that 
# temperature, you need to cut out the "TEMP:" and the "C". Today is about 
# the surgical tools of Python: Indexing and Slicing. 
# Let's sharpen the blade.
