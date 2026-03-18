# ══════════════════════════════════════════════════════════════════════════════
#  3_FORGE — Day 02: Engineering Real Systems
# ══════════════════════════════════════════════════════════════════════════════

# 🏗️ PROJECT 1: THE LOG SURGEON
# ──────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
# Every Arch Linux user knows the 'journalctl' command. It spits out thousands
# of lines of logs. You need a script that takes a raw log line and extracts
# the "Severity" and the "Module" for quick filtering.

# FEATURES:
# 1. Take a raw log string (preview Day 03: use input() to get this from the user).
# 2. Identify if the log is an [ERROR], [WARNING], or [INFO].
# 3. Extract the module name (the part between the brackets).
# 4. Clean any leading/trailing whitespace.

# SAMPLE INTERACTION:
# Enter Log: "  2026-03-18 [KERNEL] ERROR: CPU Overheat Detected   "
# Output:
# Log Level: ERROR
# Module: KERNEL
# Message: CPU Overheat Detected

# HINTS:
# Hint 1: Use `raw_log = input("Enter Log: ")` first.
# Hint 2: Use .find("[") and .find("]") to find where the module name is.
# Hint 3: Use slicing `line[start:stop]` to grab the text between the brackets.

# ASSERT TESTS:
# line = "  [SYSTEM] INFO: Boot complete  "
# cleaned = line.strip()
# module = cleaned[cleaned.find("[")+1 : cleaned.find("]")]
# assert module == "SYSTEM"
# assert "INFO" in cleaned

# EXTENSIONS:
# 1. Extract the timestamp if it exists at the start of the line.
# 2. Calculate the length of the actual "Message" part only.
# 3. Create a "Summary" string that joins Module and Level with a hyphen.

# PROFESSIONAL VIEW:
# In production, sysadmins use 'awk' or 'grep' with Regular Expressions (Regex).
# Since you're building your own AGI, you need to understand how to build 
# these parsers from scratch using basic string methods before moving to Regex.

# EMPIRE CONNECTION:
# Robotics: Your autonomous drones will generate thousands of logs per second;
# your parsing must be surgical and fast.
# ──────────────────────────────────────────────────────────────────────────────

# 🏗️ PROJECT 2: CRYPTO-CORE ALPHA
# ──────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
# You're worried about corporate espionage at Stark Industries. You need a
# simple way to scramble a message before sending it over an unencrypted
# neural link.

# FEATURES:
# 1. A message "The eagle has landed" needs to be scrambled.
# 2. Scrambling Logic: Reverse the whole string, then swap the first and 
#    last characters of the result.
# 3. Add a "salt" (a dummy string) like "::ENCRYPTED::" to the end.

# SAMPLE INTERACTION:
# Message: "Launch Alpha"
# Scrambled: "ahplA hcnuaL" -> "lhplA hcnuaA" -> "lhplA hcnuaA::ENCRYPTED::"

# HINTS:
# Hint 1: Remember `[::-1]` for reversing.
# Hint 2: To swap first and last, grab them with indexes [0] and [-1], 
#         then build a new string: last + middle_part + first.
# Hint 3: `middle_part` is a slice: `string[1:-1]`.

# ASSERT TESTS:
# message = "HELLFIRE"
# reversed_msg = message[::-1] # ERIFLLEH
# final = reversed_msg[-1] + reversed_msg[1:-1] + reversed_msg[0]
# assert final == "HRIFLLEE"

# EXTENSIONS:
# 1. Make the "salt" dynamic based on the length of the message.
# 2. Try to "Double Scramble" by reversing every second character only.
# 3. Create a "Decoder" that does the exact opposite to get the message back.

# PROFESSIONAL VIEW:
# Real encryption (AES, RSA) uses complex mathematical transformations on 
# binary data. What you're doing here is "Obfuscation" — making text hard 
# for a human to read. It's the first step toward understanding data security.

# EMPIRE CONNECTION:
# Space Engineering: Satellite uplinks require robust encoding to prevent 
# unauthorized command injection.
# ──────────────────────────────────────────────────────────────────────────────

# ARCH LINUX / RASPBERRY PI TASK:
# Create a string variable called `mirror` containing: 
# "Server = http://arch.mirror.constant.com/archlinux/$repo/os/$arch"
# Use your new skills to extract just the protocol (http) and the 
# base URL (arch.mirror.constant.com).
