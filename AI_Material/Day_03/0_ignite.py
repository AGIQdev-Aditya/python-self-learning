# ═══════════════════════════════════
#  0_IGNITE — Day 03: The Conversation
# ═══════════════════════════════════

# Aditya,

# Let's get into it. Yesterday was all about taking strings apart and putting them back together. We saw that strings are like blueprints — a fixed sequence of characters, totally immutable. You can't change a string, you can only create a new one from the old one.

# We used indexing `[ ]` to pinpoint a single character, like `name[0]` for the first letter. And we used slicing `[start:stop:step]` to pull out whole sections. You seemed to get the hang of negative indexing (working from the end) and the `[::-1]` trick to reverse a string, which is great.

# Then we unleashed the power of string methods — those built-in tools like `.upper()`, `.lower()`, `.strip()`, and `.replace()`. Remember, a method is a function that belongs to an object. When you write `my_string.upper()`, you're telling the `my_string` object to run its `upper` code and give you back a *new* string, all in uppercase.

# We also looked at `.find()`, which was a bit different. If it finds the substring, it gives you the starting index. But if it *doesn't* find it, it returns `-1`. It doesn't crash; it just gives you a special signal value that means "not found." It's a way for the string to report a result without causing an error.

# The most powerful idea from yesterday was chaining these methods together. Something like `data.strip().upper()` first removes whitespace, then takes the result of that and makes it uppercase, all in one clean, readable line. It's like an assembly line for data.

# Let's lock that in.

# ═══════════════════════════════════
#  PROVE YOU REMEMBER
# ═══════════════════════════════════

# Write your code in `My_Work/Day_03/0_ignite.py` and run it.
# Does your output match exactly?

# Problem 1: Method Chaining
# A piece of telemetry from a Mars rover is sent as a string. It has extra
# whitespace and is in the wrong case. Fix it.
telemetry = "   tEMperATuRe: 25.5 C   "
# Your code here
# cleaned_telemetry = ?
# print(cleaned_telemetry)
# print(len(telemetry))
# print(len(cleaned_telemetry))
#
# EXPECTED OUTPUT:
# TEMPERATURE: 25.5 C
# 28
# 20


# Problem 2: Slicing and Indexing
# An access code is embedded backwards within a longer string. Extract it.
security_log = "INFO: User login successful. Access Code: 3481-edoc-ssecca"
# Your code here
# reversed_code = ?
# access_code = ?
# print(access_code)
#
# EXPECTED OUTPUT:
# access-code-1843


# Problem 3: The `find()` Method's Signal
# A data packet is supposed to contain a 'session_id'. Check if it exists.
# The `.find()` method returns the index where the substring starts, or -1 if not found.
# Use this to your advantage.
data_packet_1 = "user_id=1234;payload='hello'"
data_packet_2 = "user_id=5678;session_id=zyxw;payload='world'"
# Your code here
# found_index_1 = ?
# found_index_2 = ?
# print("Packet 1 search result:", found_index_1)
# print("Packet 2 search result:", found_index_2)
#
# EXPECTED OUTPUT:
# Packet 1 search result: -1
# Packet 2 search result: 13


# Problem 4: Slicing with Steps
# Extract the vital signs from a packed data string. The format is
# "TYPE,VALUE,TYPE,VALUE,...". We only want the values.
vitals_string = "HR,80,BP,120,TEMP,37.0,SPO2,98"
# HINT: If you start at the right index and take the right size step...
# Your code here
# heart_rate = ?
# blood_pressure = ?
# temperature = ?
# print("HR:", heart_rate)
# print("BP:", blood_pressure)
# print("SPO2:", vitals_string[31:]) # A little freebie for the last one
#
# EXPECTED OUTPUT:
# HR: 80
# BP: 120
# SPO2: 98


# ═══════════════════════════════════
#  BRIDGE TO TODAY
# ═══════════════════════════════════

# So far, all our data has been "hard-coded." The strings, the numbers, everything was written by us directly into the `.py` file. But a program that only talks to itself isn't very useful. Your AGI assistant can't be an assistant if you can't ask it questions. Your Raspberry Pi sensor script is worthless if it can't take a reading from the real world. Today, we break down that wall. We open a channel for the user to speak to the program *while it is running*. We're going to learn how to have a conversation.
