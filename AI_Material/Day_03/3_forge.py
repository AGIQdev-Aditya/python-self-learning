# AI_Material/Day_03/3_forge.py
# DAY 03 FORGE — INPUT / CLEAN / CAST / REPORT
# Boundary: Day 01, Day 02, Day 03 only.
# No solutions. Build your answers in My_Work/Day_03/.
#
# TODAY: Day 03
# CORE SKILLS:
# - input()
# - string cleaning with .strip()
# - string transformation with .upper()
# - casting with int(), float(), str()
# - type() awareness
# - len(), indexing, slicing
# - string methods: .find(), .startswith(), .replace()
# - print() with concatenation or sep
#
# NON-NEGOTIABLE QUALITY BAR:
# 1. Every input starts as a string.
# 2. Every text input must be cleaned before use.
# 3. Every numeric input must be cast after cleaning.
# 4. Every report line must match the expected output exactly.
# 5. Variables must show their stage:
#    raw input -> cleaned value -> converted value.
# 6. No future concepts are allowed.


# ============================================================
# PROJECT 1 — MISSION INTAKE CONSOLE
# ============================================================

# NAME:
# Mission Intake Console

# FEATURES:
# - Ask for a station name.
# - Ask for a fuel amount.
# - Ask for a crew count.
# - Ask for a cargo weight.
# - Store each raw answer in its own variable.
# - Remove side spaces from every input.
# - Convert the station name to uppercase.
# - Convert the fuel amount to float.
# - Convert the crew count to int.
# - Convert the cargo weight to float.
# - Compute RESERVE as fuel amount plus 1.0.
# - Compute TOTAL as fuel amount plus cargo weight.
# - Print a seven-line mission report.

# INTERACTION MODEL:
# The user runs the program.
# The program asks four questions in this exact order:
#
# 1. Station name
# 2. Fuel amount
# 3. Crew count
# 4. Cargo weight
#
# The program then prints exactly:
# STATION: cleaned station name in uppercase
# FUEL: fuel amount as float
# CREW: crew count as int
# CARGO: cargo weight as float
# RESERVE: fuel amount plus 1.0
# TOTAL: fuel amount plus cargo weight
# STATUS: READY

# SAMPLE SESSION VALUES:
# Station input: "  moon  "
# Fuel input: "2.5"
# Crew input: " 4 "
# Cargo input: " 1.25 "

# SAMPLE OUTPUT:
# STATION: MOON
# FUEL: 2.5
# CREW: 4
# CARGO: 1.25
# RESERVE: 3.5
# TOTAL: 3.75
# STATUS: READY

# VARIABLE MODEL TARGET:
# You should be able to explain each variable:
# - raw_station points to the exact string from input()
# - station points to the cleaned and uppercased string
# - fuel_amount points to a float object
# - crew_count points to an int object
#
# Remember: variables are names pointing to objects.
# Reassigning a variable makes the name point to a new object.

# METHOD CHAINING TARGET:
# You may clean and transform text in one expression,
# but the result must be stored in a variable.
# Example idea, not full solution:
# cleaned and uppercased station text should be stored as station.

# HINTS:
# 1. Clean text before casting it.
#    Side spaces should not survive into the final report.
# 2. Use separate variables for raw input, cleaned input,
#    and converted values.
# 3. When combining text and numbers in output,
#    convert numbers to text with str(), or use print() with sep.

# TESTS:

# Test 1 - Normal input
# Input line 1: "  moon  "
# Input line 2: "2.5"
# Input line 3: " 4 "
# Input line 4: " 1.25 "
# Expected output:
# STATION: MOON
# FUEL: 2.5
# CREW: 4
# CARGO: 1.25
# RESERVE: 3.5
# TOTAL: 3.75
# STATUS: READY

# Test 2 - Whole-number fuel and zero cargo
# Input line 1: "earth"
# Input line 2: "3"
# Input line 3: "0"
# Input line 4: "0"
# Expected output:
# STATION: EARTH
# FUEL: 3.0
# CREW: 0
# CARGO: 0.0
# RESERVE: 4.0
# TOTAL: 3.0
# STATUS: READY

# Test 3 - Leading zeros in crew count
# Input line 1: "  pad03  "
# Input line 2: "1.25"
# Input line 3: "007"
# Input line 4: "0.75"
# Expected output:
# STATION: PAD03
# FUEL: 1.25
# CREW: 7
# CARGO: 0.75
# RESERVE: 2.25
# TOTAL: 2.0
# STATUS: READY

# Test 4 - Edge case: empty station name
# Input line 1: "   "
# Input line 2: "2.0"
# Input line 3: "1"
# Input line 4: "0.5"
# Expected output:
# STATION:
# FUEL: 2.0
# CREW: 1
# CARGO: 0.5
# RESERVE: 3.0
# TOTAL: 2.5
# STATUS: READY

# Test 5 - Bad fuel input
# Input line 1: "mars"
# Input line 2: "abc"
# Expected result:
# ValueError occurs.
# The program is allowed to stop here.
# This is correct for Day 03 because bad data can fail casting.

# Test 6 - Bad crew input
# Input line 1: "mars"
# Input line 2: "2.0"
# Input line 3: "2.5"
# Expected result:
# ValueError occurs.
# int() cannot convert "2.5" directly.

# EXTENSIONS:
# 1. Add an oxygen reading as a float and print oxygen plus 1.0.
# 2. Print the type of fuel_amount and crew_count on separate lines.
# 3. Print the whole report on one line using print() with sep.
# 4. Replace spaces inside the station name with underscores.
#    Example: "moon base" becomes "MOON_BASE".

# PROFESSIONAL VIEW:
# Real systems often receive numbers as text from forms, terminals,
# sensors, APIs, or command-line tools. The program must clean that
# text, cast it safely, then produce a clean report.
# This exact pattern appears in data pipelines, dashboards, robotics
# control panels, and mission monitoring tools.

# EMPIRE CONNECTION:
# This maps directly to Raspberry Pi sensor work.
# A sensor may send fuel, temperature, battery, or cargo values as text.
# Your Pi code must clean and cast those values before they can be used
# in calculations or reports.


# ============================================================
# PROJECT 2 — ARCH/RPI SYSTEM IDENTITY CARD
# ============================================================

# NAME:
# Arch/RPi System Identity Card

# FEATURES:
# - Ask for a hostname.
# - Ask for a kernel release.
# - Ask for a board model.
# - Store each raw answer in its own variable.
# - Remove side spaces from all inputs.
# - Convert hostname, kernel release, and board model to uppercase.
# - Print the length of hostname.
# - Print the length of kernel release.
# - Print the length of board model.
# - Print the first three characters of kernel release.
# - Print the last three characters of kernel release.
# - Print the position of the first dot in kernel release.
# - Print whether hostname starts with ARCH.
# - Print a system tag in the form HOST/KERNEL/MODEL.

# INTERACTION MODEL:
# On your Arch Linux machine or Raspberry Pi, you can find real values with:
#
# hostname
# uname -r
#
# Then run your Python program.
# Enter the real hostname when asked.
# Enter the real kernel release when asked.
# Enter a board model, for example: RPi 5, Laptop, Desktop.
#
# If you are not on Arch/RPi, you may enter any values.

# OUTPUT CONTRACT:
# The program prints exactly:
# HOST: cleaned hostname
# KERNEL: cleaned kernel release
# MODEL: cleaned board model
# HOST_LENGTH: length of cleaned hostname
# KERNEL_LENGTH: length of cleaned kernel release
# MODEL_LENGTH: length of cleaned board model
# KERNEL_PREFIX: first three characters of cleaned kernel release
# KERNEL_SUFFIX: last three characters of cleaned kernel release
# DOT_POSITION: position of first dot in cleaned kernel release, or -1
# ARCH_STYLE: True if cleaned hostname starts with ARCH, otherwise False
# SYSTEM_TAG: HOST/KERNEL/MODEL

# SAMPLE SESSION VALUES:
# Hostname input: "  archpi  "
# Kernel input: "  6.6.2-v8  "
# Model input: "  rpi 5  "

# SAMPLE OUTPUT:
# HOST: ARCHPI
# KERNEL: 6.6.2-V8
# MODEL: RPI 5
# HOST_LENGTH: 6
# KERNEL_LENGTH: 8
# MODEL_LENGTH: 5
# KERNEL_PREFIX: 6.6
# KERNEL_SUFFIX: -V8
# DOT_POSITION: 1
# ARCH_STYLE: True
# SYSTEM_TAG: ARCHPI/6.6.2-V8/RPI 5

# EDGE CASES TO RESPECT:
# - Empty strings are allowed.
# - Strings shorter than three characters are allowed.
# - Slicing must not crash on short strings.
# - If there is no dot, .find() should produce -1.
# - Length must be measured after stripping side spaces.

# HINTS:
# 1. Use strip before len so side spaces do not inflate the length.
# 2. A slice can extract the first three and last three characters.
# 3. .find() returns -1 when the character is not found.
# 4. When concatenating text with a length or boolean-related value,
#    convert non-string values to string first, or use print() with sep.

# TESTS:

# Test 1 - Normal Arch/RPi-style input
# Input line 1: "  archpi  "
# Input line 2: "  6.6.2-v8  "
# Input line 3: "  rpi 5  "
# Expected output:
# HOST: ARCHPI
# KERNEL: 6.6.2-V8
# MODEL: RPI 5
# HOST_LENGTH: 6
# KERNEL_LENGTH: 8
# MODEL_LENGTH: 5
# KERNEL_PREFIX: 6.6
# KERNEL_SUFFIX: -V8
# DOT_POSITION: 1
# ARCH_STYLE: True
# SYSTEM_TAG: ARCHPI/6.6.2-V8/RPI 5

# Test 2 - Edge case: empty kernel and model
# Input line 1: "pi"
# Input line 2: "   "
# Input line 3: "   "
# Expected output:
# HOST: PI
# KERNEL:
# MODEL:
# HOST_LENGTH: 2
# KERNEL_LENGTH: 0
# MODEL_LENGTH: 0
# KERNEL_PREFIX:
# KERNEL_SUFFIX:
# DOT_POSITION: -1
# ARCH_STYLE: False
# SYSTEM_TAG: PI//

# Test 3 - Mixed case, digits, and no dot
# Input line 1: "Alpha01"
# Input line 2: "5100"
# Input line 3: "  Raspberry Pi  "
# Expected output:
# HOST: ALPHA01
# KERNEL: 5100
# MODEL: RASPBERRY PI
# HOST_LENGTH: 7
# KERNEL_LENGTH: 4
# MODEL_LENGTH: 12
# KERNEL_PREFIX: 510
# KERNEL_SUFFIX: 100
# DOT_POSITION: -1
# ARCH_STYLE: False
# SYSTEM_TAG: ALPHA01/5100/RASPBERRY PI

# EXTENSIONS:
# 1. Print MODEL_CODE by replacing spaces in the cleaned model with hyphens.
#    Example: "RASPBERRY PI" becomes "RASPBERRY-PI".
# 2. Print whether KERNEL contains a dot using the in operator.
# 3. Print the first and last character of the cleaned hostname.
# 4. Print the whole system card on one line using print() with sep.

# PROFESSIONAL VIEW:
# System tools often collect machine identity data: hostname, kernel version,
# architecture, and device model. This data is usually text first, then cleaned,
# transformed, measured, and displayed or logged.
# This is common in CLI utilities, inventory tools, device dashboards,
# and remote fleet monitoring.

# EMPIRE CONNECTION:
# This project is directly usable on your Arch Linux setup or Raspberry Pi.
# You are taking real shell outputs and turning them into a cleaned Python
# system report. This is the beginning of real systems engineering:
# observe the machine, clean the data, and make the state visible.


# ============================================================
# FINAL FORGE CHECK
# ============================================================
# - No future concepts are required.
# - No if statements are required.
# - No loops are required.
# - No advanced formatting is required.
# - Only Day 01 to Day 03 concepts are used.
# - Weak areas targeted:
#   1. input() always returns a string.
#   2. Clean before casting.
#   3. Cast before doing math.
#   4. Use str() when combining numbers with text.
#   5. Variables are names pointing to objects.
#   6. Method chaining must still produce stored variables.
