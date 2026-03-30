# ═══════════════════════════════════
#  2_MY GAUNTLET — Day 02
#  Solve every challenge from 2_gauntlet.py here.
#  No solutions visible anywhere.
# ═══════════════════════════════════


# P1

name = 'Aditya'
print('names first letter: ', name[0], 'names last letter: ', name[-1])

# sorry going to sleep right will come stronger tomorrow morning  

# am back 

# P2

world = 'STARK'
a = len(world) // 2
print(world[a])

# P3

cmd = "   reboot_system_now   "
d = cmd.strip().upper()

# P4    

log = "system_ok: memory_stable"
print('ERROR' in log)

# P4.5

data = "     X-1      "
print(data.strip()[0])
print(data[0])

# got it 

# P5

reading = "velocity=25.5m/s"
print(reading[-6:-1])

# p6

ELEMENT = 'magnesium'
print(ELEMENT[0:3:2].upper())

# P7

a = 'AGI_CORE_BETA'
print(a[::-1])

# P8

c = 'system_update.tar.gz'
print(c.replace('.tar.gz', ''))

# P9

d = 'Server = https://mirror.rackspace.com/archlinux/$repo/os/$arch'
start_index = d.find('//') + 2
end_index = d.find('/', start_index)
print(d[start_index:end_index])

# p10

rp = 'ID:007|MODULE:KERNEL|TEMP:24.85'

# 1. Find the Module (Start after "MODULE:", end at the next "|")
mod_start = rp.find('MODULE:') + 7
mod_end = rp.find('|', mod_start)
module_name = rp[mod_start:mod_end].lower() # Only call lower() once!

# 2. Find the Temperature (Start after "TEMP:" and go to the end)
temp_start = rp.find('TEMP:') + 5
temperature = rp[temp_start:]

print('module:', module_name + ',', 'temp:', temperature)

# p11

a = 'http://insecure.com'
b = 'https://stark-industries.com'
c = 'ftp://files.org'

print(a.startswith('https') and a.endswith('.com'))
print(b.startswith('https') and b.endswith('.com'))
print(c.startswith('https') and c.endswith('.com'))
