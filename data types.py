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

print(len(multiline))
multiline += "                                                 "
multiline = "                                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#Build a menu

title = "menu".upper()
print(title.center(20, "="))
print("Cofee".ljust(16,".")  + "$1".rjust(4))
print("Tea".ljust(16,".")  + "$5".rjust(4))
print("Mango Juice".ljust(16,".")  + "$13".rjust(4))

print("")



print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data
print(first.startswith("R"))
print(first.endswith("E"))


myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

#numeric data types
#integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float types ; have decimals
gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)






