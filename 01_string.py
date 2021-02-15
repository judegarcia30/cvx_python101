print('Hello World') # Literal string
message = 'Hello World' # String stored in Variable
print(message)
print(str('This is a string - 123456')) # Another way to create a string - str()

multiline_string = '''
This is a multiline string.
Next line of the string.
''' # To create multiline string, use triple quotes '''
print(multiline_string)

# Handle quote inside a string
my_message = 'Python\'s quote' # use backslash '\' to escape the character
my_message = "Python's quote" # use double quote
print(my_message)

# String methods
help(str())

# concatenate and formatting string
message = 'Hello' + ' ' + 'World'
hello = 'Hello'
name = 'Python'
message = '{0} {1}'.format(hello, name)
message = f"{hello} {name}"
print(message)