# ═══════════════════════════════════════════════
#  2_MY_GAUNTLET — Day 01
#  Solve every challenge from AI_Material/Day_01/2_gauntlet.py here.
#  There are no solutions visible, so you are on your own.
#  Trust your knowledge from the Nexus.
# ═══════════════════════════════════════════════

# Your solutions go here...

# 1. Personal Welcome

name = 'Aditya'
city = 'mumbai'

print('welcome, ' + name + '!' + 'we are glade you are here in ' + city + '.')

# 2. Rover Status

name = 'preserverance'
temperature = -63.5
status = 'active'

print('rover:', name)
print('termperature:', temperature, 'C')
print('ststus:', status)
 
# 3. Data Type Check

a = 'addi'
b = 10
c = 3.141592653589793238462643
d = False

print(a, 'is a' , type(a))
print(b, 'is a' , type(b))
print(c, 'is a' , type(c))
print(d, 'is a' , type(d))
  
# 4. Kinematics Calculator

u = 10
a = 2
t = 5

s = u*t + (0.5*a*(t**2))
print('displacement (s):', s, 'm')

# 5. Ideal Gas Law (Chemistry)

n = 1
T = 298
V = 22.4
R = 0.0821

P = (n*R*T) / V
print('pressure (p):', P, 'atm')

# i got ans as 1.0922232142857144 atm  but  expected output is 1.0922232142857143 atm but i think its just a rounding error and it is correct answer.

# 6. ASCII Art


print('       /^\\')
print('      /   \\')
print('     / ___ \\')
print('    |  (  ) ||     ')
print('    |   --  ||     ')
print('    | _____ ||     ')
print(' /\ |/     \|| /\  ')
print(' ||-|\_____/||-||  ')
print(' || |/     \|| ||  ')
print(' || |  ( )  || ||  ')
print(' || |   .   || ||  ')
print(' /\ |_______|| /\  ')
print('   /         \\    ')

print('rocket ship is ready to launch!')

# 7. Variable Swap

a = 100
b = 200

z = b
b = a

a  = z

print('now a =', a, 'and b =', b)

print('not hard right? we just used a temporary variable z to hold the value of b while we assigned a to b, and then we assigned z (which holds the original value of b) back to a. This way, we successfully swapped the values of a and b.')

# also this whole para was in my mind but i was not going to type it here but the ai did so why not

# 8. Arch Linux 'neofetch' Stub
os = 'archlinux'
host = 'addi'
kernal_version = 'hai kuch toh'
uptime = 'i won"t tell '
shell = 'zsh 5.9 i guess'

print('os', os, sep=': ')
print('host', host, sep=': ')
print('kernal_version', kernal_version, sep=': ')
print('uptime', uptime, sep=': ')
print('shell', shell, sep=': ')

# i am not sure about the expected output for this one but i think it is correct as it is showing the system info in a neat format using the sep parameter of print function.
print('also now i guess its fastfetch not neofetch but its ok ')

# 9. Raspberry Pi Data Packet


packet_id = 1024
voltage = 3.3
humidity = 75.4
status_ok = True

print('packet_id', packet_id, type(packet_id), sep=': ')
print('voltage', voltage, type(voltage), sep=': ')
print('humidity', humidity, type(humidity), sep=': ')
print('status_ok', status_ok, type(status_ok), sep=': ')

# 10. AGI Core Diagnostics

logic_core_temp = 75.0
memory_usage_percent = 81.2
anomaly_detected = False

is_temp_critical = False
is_mem_critical = True
is_anomaly_critical = False

critical_score = is_temp_critical + is_mem_critical + is_anomaly_critical

print('--- AGI Core Diagnostics ---')

print('Logic Core Temp:', logic_core_temp, 'C')
print('Memory Usage:', memory_usage_percent, '%')
print('Anomaly Detected:', anomaly_detected)

print("--- status ---")

print("temp critical:", is_temp_critical)
print("mem critical:", is_mem_critical)
print("anomaly critical:", is_anomaly_critical)

print('--- final ---')

print('critical score:', critical_score)

print('okayy done soo byeee')