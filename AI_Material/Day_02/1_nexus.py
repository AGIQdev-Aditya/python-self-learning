# ══════════════════════════════════════════════════════════════════════════════
#  1_NEXUS — Day 02: Strings - The Sequence Protocol
#  Open 1_my_nexus.py beside this.
#  Read one section. Type it yourself. Never copy-paste.
# ══════════════════════════════════════════════════════════════════════════════

# ⏱ Estimated Time: 120 minutes

# ══════════════════════════════════════════════════════════════════════════════
#  CONCEPT 1: Indexing — Finding Your Position
# ══════════════════════════════════════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# You've captured a command from your AGI terminal: "INITIATE_CORE_SYNC".
# You don't need the whole thing. You just need to check the very first 
# character to see if it's 'I' for Initiate. If you treat a string as 
# one giant, untouchable block of text, you can't reach inside and grab 
# what you need. You're stuck on the outside.

# LAYER 2 — THE CONCEPT
# Every character in a Python string has a numerical address, called an INDEX.
# In the world of computer science (and Python), we start counting at 0.
# The first character is at index 0, the second at 1, the third at 2, and so on.
# We access these addresses using square brackets `[]`.

# LAYER 3 — THE MECHANICS (MEMORY MODEL)
# In your 8GB RAM, when you create `name = "ADITYA"`, Python allocates memory 
# for the string object. Internally, this object is a contiguous array 
# of characters. The variable `name` points to the start of this array.
# When you write `name[0]`, Python:
# 1. Finds the memory address where the string starts.
# 2. Jumps exactly 0 "offsets" (character widths) forward.
# 3. Reads the data at that spot and returns it.
# This "Zero-Based Indexing" is standard because it simplifies the math 
# for the CPU.

# Forward Indexing:
#  A  D  I  T  Y  A
#  0  1  2  3  4  5

# Backward Indexing (Negative Indexing):
# Python lets you count from the end using negative numbers!
#  A   D   I   T   Y   A
# -6  -5  -4  -3  -2  -1

# LAYER 4 — THE WRONG WAY
# Mistake 1: Out of Bounds
# drone_id = "X-78"
# print(drone_id[10])
# Why: You're asking Python to read memory that isn't yours.
# Error: IndexError: string index out of range

# Mistake 2: Strings are IMMUTABLE
# name = "Aditya"
# name[0] = "B"
# Why: Once a string is created in Python memory, you CANNOT change it.
# You must create a NEW string if you want to change it.
# Error: TypeError: 'str' object does not support item assignment

# LAYER 5 — REAL EXAMPLES
# Example 1: Basic Terminal Input
cmd = "STATUS_REPORT"
print("First character:", cmd[0]) # 'S'
print("Last character:", cmd[-1]) # 'T'

# Example 2: Checking a Raspberry Pi Serial Number
# Imagine a serial like "RPi4-00123"
serial = "RPi4-00123"
model_prefix = serial[0] # 'R'
print("Device Type:", model_prefix)

# Example 3: Spacecraft Signal Check
# Signals often start with a priority bit.
signal = "9-TX-ALPHA"
priority = signal[0]
print("Signal Priority Level:", priority)

# ══════════════════════════════════════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ══════════════════════════════════════════════════════════════════════════════
# Predict the output of these. Write it down. Then test in 1_my_nexus.py.

# target = "MARS_ROVER"
# 1. print(target[4])
# 2. print(target[-1])
# 3. print(target[-5])

# ⏱ Estimated: 10 minutes

# LAYER 7 — EDGE CASES AND GOTCHAS
# 1. Empty Strings: `s = ""`. `s[0]` will ALWAYS raise an IndexError.
# 2. White Space: Space is a character too! `s = " "`. `s[0]` is a space.
# 3. Multi-byte characters (Emojis/Hindi): `s = "नमस्ते"`. 
#    Python 3 handles these as single indexes correctly. Try `s[0]`.

# LAYER 8 — THE CONNECTION
# In robotics firmware (C++ or Python), indexing is how you parse "Packets". 
# A sensor might send 8 bytes of data. The first byte is the ID, the next 
# 4 are the value. Without indexing, your autonomous systems are blind 
# to the data they receive.

# ══════════════════════════════════════════════════════════════════════════════
#  CONCEPT 2: Slicing — The Surgical Blade
# ══════════════════════════════════════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# You have a string from your Arch Linux system logs: "ERROR: [DISK_FULL] at 12:00".
# You don't just want one character. You want the word "DISK_FULL".
# Indexing is a needle. Slicing is a scalpel.

# LAYER 2 — THE CONCEPT
# Slicing lets you extract a "substring" (a range of characters).
# The syntax is: variable[start : stop : step]
# - START: The index where you begin (Inclusive).
# - STOP: The index where you end (Exclusive - it stops BEFORE this index).
# - STEP: How many characters to jump each time (Optional, defaults to 1).

# LAYER 3 — THE MECHANICS (MEMORY MODEL)
# When you slice a string, e.g., `new_str = old_str[1:4]`, Python:
# 1. Creates an entirely NEW string object in memory.
# 2. Copies the characters from index 1, 2, and 3 into the new memory space.
# 3. Makes `new_str` point to this new object.
# The original string remains untouched. This is why we say strings are "immutable".

# LAYER 4 — THE WRONG WAY
# Mistake: Forgetting the "Exclusive Stop"
# word = "Python"
# slice = word[0:2] 
# Predict: You might think this gives "Pyt" (0, 1, 2).
# Reality: It gives "Py" (only 0 and 1). It stops AT index 2 but doesn't include it.

# Correct way to get the first 3:
# slice = word[0:3]

# LAYER 5 — REAL EXAMPLES
# Example 1: Parsing a Unix Path
path = "/usr/bin/python3"
folder = path[1:4] # "usr"
print("Root folder:", folder)

# Example 2: Reverse a String (The Step Trick)
# A very common interview question! Use a step of -1.
secret_key = "12345-X-6789"
reversed_key = secret_key[::-1]
print("Reversed:", reversed_key)

# Example 3: Extracting Domain from Email
email = "aditya@stark-industries.com"
# Let's say we know the domain starts at index 7
domain = email[7:] # Leaving 'stop' empty means "go to the very end"
print("Domain:", domain)

# Example 4: Space Engineering - Telemetry Decimation
# Imagine a high-speed sensor stream from a Mars Rover. 
# It sends interleaved data: A1_B2_A3_B4_A5_B6_A7_B8... (A=Temp, B=Volt)
# We want to extract Sensor A values only, and only from the first 20 characters,
# but our bandwidth is low, so we skip every second A-reading.
telemetry_stream = "A1_B2_A3_B4_A5_B6_A7_B8_A9_B0"
# Index 1 is the first '1'. 
# Logic: 'A1' is index 0,1. 'B2' is index 3,4. 'A3' is index 6,7.
# The distance between A-readings (1 to 3) is 6 characters.
# To skip every second A-reading, we double that distance: 6 * 2 = 12.
decimated_a_readings = telemetry_stream[1:20:12] 
print("Decimated Sensor A readings:", decimated_a_readings) # '1' and '4'

# ══════════════════════════════════════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ══════════════════════════════════════════════════════════════════════════════
# Predict the output. 

# text = "STARK_AGI_v1.0"
# 1. print(text[0:5])
# 2. print(text[6:9])
# 3. print(text[::2]) # Every second character

# ⏱ Estimated: 15 minutes

# LAYER 7 — EDGE CASES AND GOTCHAS
# 1. Out of Bounds Slicing: Unlike indexing, slicing is FORGIVING.
#    `"ABC"[0:100]` will just return "ABC". It won't crash.
# 2. Start > Stop: `"ABC"[2:0]` returns an EMPTY string. 
# 3. Negative Slices: `"ABC"[:-1]` means "everything except the last character".

# LAYER 8 — THE CONNECTION
# In Space Engineering, data from satellites comes in "Frames". 
# A frame might be 1024 characters long. Bits 0-64 might be 
# identity, 65-128 might be checksum. Slicing is how you unpack 
# the universe's data.

# ══════════════════════════════════════════════════════════════════════════════
#  CONCEPT 3: The `len()` Function — Measuring the Universe
# ══════════════════════════════════════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# You're writing a script to monitor your Arch Linux logs. 
# You need to know if a log message is too long to display on your 
# small 16x2 Raspberry Pi LCD screen. How do you count the characters?
# Counting manually is impossible if the data is dynamic.

# LAYER 2 — THE CONCEPT
# `len()` is a built-in function that returns the total number of characters
# in a sequence (including spaces and punctuation).

# LAYER 3 — THE MECHANICS
# Python string objects actually store their length as a separate integer 
# in memory. When you call `len(my_str)`, Python doesn't actually count 
# the characters 1, 2, 3... it just looks up that pre-stored value. 
# This makes `len()` extremely fast, even for a string with a billion 
# characters.

# LAYER 4 — THE WRONG WAY
# Mistake: Trying to get the last character using len() directly.
# word = "Arch"
# last = word[len(word)]
# Why: `len("Arch")` is 4. But indexes are 0, 1, 2, 3. Index 4 is out of range!
# Correct Way: `word[len(word)-1]` or better yet, `word[-1]`.

# LAYER 5 — REAL EXAMPLES
# Example 1: Standardizing User Data
username = "aditya_stark_2026"
print("Length of username:", len(username))

# Example 2: Validation Logic
password = "admin"
print("Password length is:", len(password))

# Example 3: Spacecraft Telemetry Packet Audit
# Telemetry packets must often be exactly 32 or 64 characters.
# Let's check a header from a simulated deep-space probe.
packet_header = "0xAF_ID77_SEQ001_CHECKSUM_STABLE"
header_size = len(packet_header)
print("Incoming header size:", header_size, "bytes")
# Check if we have the full 'STABLE' status at the end
print("Status word length:", len(packet_header[-6:])) 

# ══════════════════════════════════════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ══════════════════════════════════════════════════════════════════════════════
# Predict the output of these:

# s1 = "SpaceX"
# s2 = "Space X"
# s3 = ""
# 1. print(len(s1) == len(s2))
# 2. print(len(s3))
# 3. print(len("Python"[1:4]))

# ⏱ Estimated: 5 minutes

# LAYER 7 — EDGE CASES AND GOTCHAS
# 1. Newlines and Tabs: `s = "\n\t"`. `len(s)` is 2. Even though they look 
#    like two characters (backslash + n), Python treats escape sequences 
#    as a single character in memory.
# 2. Leading/Trailing Spaces: `len(" Aditya ")` is 8, not 6. Spaces 
#    are data! This is why `.strip()` is so important.

# LAYER 8 — THE CONNECTION
# In Network Programming and Cyber Security, `len()` is used for 
# "Buffer Validation". If a system expects a 16-character password 
# and receives 10,000, it might be a "Buffer Overflow" attack. 
# `len()` is your first line of defense to ensure data fits the 
# containers you've built.

# ══════════════════════════════════════════════════════════════════════════════
#  CONCEPT 4: String Methods — The Power Tools
# ══════════════════════════════════════════════════════════════════════════════

# LAYER 1 — THE PROBLEM
# Users are messy. One user types " Aditya ", another types "ADITYA", 
# another types "aditya". If your AGI system is looking for exactly "Aditya", 
# it will fail 2 out of 3 times. We need a way to "clean" and "standardize" 
# text.

# LAYER 2 — THE CONCEPT
# "Methods" are functions that belong to an object. Because strings are 
# objects, they have built-in "tools" you can call using the dot `.` notation.

# LAYER 3 — THE MECHANICS
# When you call `name.upper()`, Python looks at the `name` object, runs 
# the code for the `upper` method, and produces a BRAND NEW string object 
# with all characters capitalized. The original `name` remains lowercase 
# in memory.

# LAYER 4 — THE WRONG WAY
# Mistake: Forgetting that methods RETURN a value.
# name = "aditya"
# name.upper() 
# print(name) # Output is still "aditya"!
# Correct Way:
# name = name.upper() 

# LAYER 5 — REAL EXAMPLES
# Example 1: Cleaning User Input
raw_input = "   admin_user   "
clean_input = raw_input.strip().upper() 
# .strip() removes spaces from ends, .upper() makes it "ADMIN_USER"
print("Cleaned:", clean_input)

# Example 2: Finding and Replacing
msg = "The system is OFFLINE"
new_msg = msg.replace("OFFLINE", "ONLINE")
print(new_msg)

# Example 3: Protocol & Log Checking (New Tools)
url = "https://archlinux.org"
log_line = "CRITICAL: Kernel panic"

print("Is it secure?", url.startswith("https")) # True
print("Is it a kernel issue?", log_line.endswith("panic")) # True
print("Position of 'failed':", log_line.find("failed")) # -1 (not found)

# Example 4: Searching
log = "ERROR: Connection failed at 09:00"
print("Does it contain ERROR?", "ERROR" in log) # Using 'in' operator

# Example 5: Joining Sequences
words = ["AI", "will", "win"]
sentence = "_".join(words)
print(sentence)  # AI_will_win
# NOTE: We will cover 'Lists' (the square brackets part) in depth on Day 11,
# but .join() is too powerful to wait for. It glues text together.

# ══════════════════════════════════════════════════════════════════════════════
#  PAUSE AND THINK (LAYER 6)
# ══════════════════════════════════════════════════════════════════════════════
# Predict output:
# text = "Python is Great"
# 1. print(text.lower().replace("python", "AGI"))
# 2. print(text.count("t"))
# 3. print(text.split(" ")) # This is a bonus, try it!

# ⏱ Estimated: 20 minutes

# LAYER 7 — EDGE CASES AND GOTCHAS
# 1. `.find()` returns `-1` if the string isn't found. It doesn't crash.
# 2. `.replace()` replaces ALL occurrences. 
#    `"ha ha ha".replace("ha", "ho")` -> "ho ho ho".
# 3. Chaining: You can do `text.strip().lower().replace(...)`. 
#    It executes from left to right.
# 4. `.join()` with one item: If the list has only one item, e.g., 
#    `"-".join(["AI"])`, it just returns "AI" without the hyphen.

# LAYER 8 — THE CONNECTION
# In AGI (Natural Language Processing), string methods are the first 
# step of "Pre-processing". Before a Neural Network even sees the 
# text, we strip punctuation, convert to lowercase, and split into 
# "tokens". Without this, the AI sees "Apple" and "apple" as two 
# completely different concepts.

# ══════════════════════════════════════════════════════════════════════════════
#  WHAT'S COMING TOMORROW
# ══════════════════════════════════════════════════════════════════════════════
# Today we handled data that was already inside our code. 
# But a program that only talks to itself is a toy. 
# Tomorrow, we break the wall between the machine and the human.
# We will learn `input()` — how to make your Python scripts actually 
# ASK Aditya for information. 
# But there's a catch: Everything `input()` touches becomes a STRING. 
# If you ask for "2" and try to add "2", you might get "22" instead of "4".
# We will master "Type Casting" (int(), float(), str()) to control 
# the transformation of data. 
# Your scripts are about to become interactive. 
# Get some rest, Aditya. The empire awaits.
