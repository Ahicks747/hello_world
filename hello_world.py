# print("Hello World!")
# x = "Hello Python"
# print(x)
# y = 42
# print(y)

# 1. TASK: print "Hello World"
print( "Hello World!" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Austin"
print( "Hello ",name,'!')	# with a comma
print( "Hello " + name +'!')	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 8
print( "Hello ", name, '!')	# with a comma
print( "Hello " + str(name) + '!')	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Chicken"
fave_food2 = "Fries"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

#Bonus
#Different ways to do string.upper
print("I love to eat Chicken and Fries.".upper())
print("I love to eat {} and {}.".format(fave_food1, fave_food2).upper())
print(f"I love to eat {fave_food1} and {fave_food2}.".upper() )

#Different ways to do string.isalnum()
print("I love to eat Chicken and Fries.".isalnum())

