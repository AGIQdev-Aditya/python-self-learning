# ═══════════════════════════════════
#  3_MY FORGE — Day 02
#  Build every project from 3_forge.py here.
#  Make something real.
# ═══════════════════════════════════


# so here I start

# is still don't know how to take input but will try

raw_log = input("Enter Log: ").strip()
print('so your log is:', raw_log.strip())

module = raw_log[raw_log.find('[') + 1 : raw_log.find(']')]
print('Module is:', module)

e = print('if there is error:', 'ERROR' in raw_log)
w = print('if there is warning:', 'WARNING' in raw_log)
i = print('if there is info:', 'INFO' in raw_log)

# pretty much done  
# i haven't yet learned input function and if else elif stuff 



# so heres teh second one of the day 2 teaching 

message = input("Message: ")

reversed_msg = message[::-1]

first = reversed_msg[0]
last = reversed_msg[-1]
middle = reversed_msg[1:-1]

salt = '::ENCRYPTED::'

scrembled_rev_msg = last + middle + first + salt

print(scrembled_rev_msg)


# done thsi one was more eassy i guess 

# now for decryption 

removed_mark = scrembled_rev_msg.replace(salt, '')

r_first = removed_mark[-1]

r_last = removed_mark[0]

decrypted_msg = r_first + middle + r_last

re_revewrsed_msg = decrypted_msg[::-1]

print('decrypted msg is:', re_revewrsed_msg)




