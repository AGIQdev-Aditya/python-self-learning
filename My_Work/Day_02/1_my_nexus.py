# ═══════════════════════════════════
#  1_MY NEXUS — Day 02
#  Code along with 1_nexus.py here.
#  Read one section. Type it yourself. Never copy-paste.
# ═══════════════════════════════════

print('so here i starts')
print('actually starting now')

print('actually today am starting sorry')

a = 'Aditya Agnihotri'
print('my name is:', a, 'with a single', '"' + a[0] + '"', 'in my first name')

laptop_available = 'yes'
available = laptop_available[0]
print('is laptop available:', available)


target = "MARS_ROVER"
print(target[4])
print(target[-1])
print(target[-5])

# i thing in output we will get _, R, R

s = "नमस्ते"
print(s[0])
print(s[1])
print(s[-1])

print(s[0] + s[1] + s[-1])

path = '/usr/bin/tin/kin/sin'
c = path[0:4]
print('root directory is:', c)

# email = 'aditya@gmail.com'
# domain = email[-1:4]
# print ('domain is:'+ domain)
#  this -1 is not working because it is not a valid index for slicing, I guess.

# oh got it just need to read more it6 just instead of -1 i just have to leave it blank and to make iot stoip make be put value in -  let try 

email = 'aditya@gmail.com'
domain = email[::-1]
print ('domain is:'+ domain)

# so it does nothing but reverse print  if we leave start and stop blank and put -1 in step it will reverse the string.

# also if we want to keep going untill end we just leve teh stop empty thats it.

# sorry i left now2 i am continuing sorry after days  excuse is i was sick and was not able to do it but now i am fine and will continue with the course.


telemetry_stream = "A1_B2_A3_B4_A5_B6_A7_B8_A9_B0"
decimated_a_readings = telemetry_stream[1::12]
print("Decimated Sensor A readings:", decimated_a_readings)

# so here we are starting from index 1 and then we are taking every 12th character which is the reading of sensor A and storing it in decimated_a_readings variable and then printing it.

text = "STARK_AGI_v1.0"
print(text[0:5])
print(text[6:9])
print(text[::2])

a = "ADITYA"
print(a[-1])
print(len(a))

packet = "PKT1234567890"
print(packet[-6:])

s1 = "SpaceX"
s2 = "Space X"
s3 = ""
print(len(s1) == len(s2))
print(len(s3))
print(len("Python"[1:4]))

# so i guess all correctly done and i am getting the output as expected.

# so continuing now yesterday i went to sleep.

z = '    astronaut    '
# so here in teh string there are spaces that might come so to remve them we can use strip() function which will remove the leading and trailing spaces from the string and return the new string without spaces.which is used bye typing .strip() after the string variable name and it will return the new string without spaces.

cleaned_z = z.strip()
print('cleaned string is:', cleaned_z)

# sonow if we want the whole string tyo be in uppercase we can use upper() function which will convert all the characters in the string to uppercase and return the new string with uppercase characters.which we can do by typing .upper() after the string variable name and it will return the new string with uppercase characters.

y = 'astronaut'
uppercase_y = y.upper()
print('uppercase string is:', uppercase_y)

# so now if we want the whole string to be in lowercase we can use lower() function which will convert all the characters in the string to lowercase and return the new string with lowercase characters.which we can do by typing .lower() after the string variable name and it will return the new string with lowercase characters.

x = 'ASTRONAUT'
lowercase_x = x.lower()
print('lowercase string is:', lowercase_x)

# so now if we want to replace a part of the string with another string we can use replace() function which will replace all the occurrences of the old string with the new string and return the new string with the replaced string.which we can do by typing .replace(old_string, new_string) after the string variable name and it will return the new string with the replaced string.We replace that specific part of the string by specifying the old string and the new string in the replace() function.

o = 'i am a student'
replaced_o = o.replace('student', 'engineer')
print('replaced string is:', replaced_o)

# so we uses .startswith() function to check if the string starts with a specific substring and it will return True if the string starts with the specified substring and False otherwise. We can do this by typing .startswith(substring) after the string variable name and it will return True or False based on whether the string starts with the specified substring or not.

p = 'Hello, World!'
print(p.startswith('Hello'))
print(p.startswith('World'))

# so we uses .endswith() function to check if the string ends with a specific substring and it will return True if the string ends with the specified substring and False otherwise. We can do this by typing .endswith(substring) after the string variable name and it will return True or False based on whether the string ends with the specified substring or not.

q = 'Hello, World!'
print(q.endswith('World!'))
print(q.endswith('Hello'))

#we use in operator to check if a specific substring is present in the string and it will return True if the substring is present in the string and False otherwise. We can do this by typing substring in string_variable_name and it will return True or False based on whether the substring is present in the string or not.

r = 'Hello, World!'
print('while learning python we traditionally start with hello world: ', 'World' in r)
print('while learning python we traditionally start with world hello: ', 'word' in r)

# also we uses .find() function to find the index of the first occurrence of a specific substring in the string and it will return the index of the first occurrence of the specified substring in the string or -1 if the substring is not found. We can do this by typing .find(substring) after the string variable name and it will return the index of the first occurrence of the specified substring in the string or -1 if the substring is not found.

s = 'Hello, World!'
index_of_world = s.find('World')
print('index of "World" in the string is:', index_of_world)

# we use .join() function to join a list of strings into a single string with a specified separator between each string. We can do this by typing separator.join(list_of_strings) and it will return a new string with the list of strings joined together with the specified separator.

list_of_strings = ['Hello', 'World', 'Python']
separator = ' '
joined_string = separator.join(list_of_strings)
print('joined string is:', joined_string)

# we can use .count() function to count the number of occurrences of a specific substring in the string and it will return the number of occurrences of the specified substring in the string. We can do this by typing .count(substring) after the string variable name and it will return the number of occurrences of the specified substring in the string.

t = 'Hello, World!'
count_of_o = t.count('o')
print('count of "o" in the string is:', count_of_o)

# we can use .split() function to split a string into a list of substrings based on a specified separator and it will return a list of substrings that are separated by the specified separator. We can do this by typing .split(separator) after the string variable name and it will return a list of substrings that are separated by the specified separator.

u = 'Hello, World, !, Python'
list_of_substrings = u.split(',')
print('list of substrings is:', list_of_substrings)

text = "Python is Great"
print(text.strip().lower().replace('p', 'J'))

# if no square brackets are use then there is a spce which is added between the string and the output will be 'P K' but if we use square brackets then there will be no space between the string and the output will be 'PK' which is what we want. So we need to use square brackets to avoid adding space between the string.

b = 'PK'
s = ' '.join(b)
print(s)

# if we use square brackets then there will be no space between the string and the output will be 'PK' but if we do not use square brackets then there will be a space between the string and the output will be 'P K' which is not what we want. So we need to use square brackets to avoid adding space between the string.

a = ('PK')
s = ' '.join([a])
print(s)


print('so day 2 is done after this long now going for questionsa dn problems bye')