#String data types

#literal assignment

first = "Ridge"
last = "Junior"

# print(type(first))
# print(type((first)) == str)
# print(isinstance(first, str))

#constructor

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type((pizza)) == str)
# print(isinstance(pizza, str))

#Concatenation - adding two strings together to form a larger string
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)


decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the "  + decade + "S."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                                All good?
                            
'''
print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence) 

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)



