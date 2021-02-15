# Functions are block of codes that can be re-used on your script
# DRY (Don Repeat Your self)

def hello_world_function():
    print('Hello World')

hello_world_function() # To call the function

# Function that returns a value
def hello_world_return():
    return 'Hello World Return Function'

result = hello_world_return() # Return Value is stored in variable
print(result)

# Pass arguments to a function
def Greetings(firstname): # Positional argument
    return f'Hello {firstname}'

def Greetings_kwargs(firstname, lastname='Garcia'): # Keyword argument with default value
    return f'Hello {firstname} {lastname}'

print(Greetings('Jude'))
print(Greetings_kwargs('Jude'))
print(Greetings_kwargs('James', lastname='Bond')) # Passing value to the keyword argument

# ARGS And KWARGS

def device_info(*args, **kwargs):
    print(args)
    print(kwargs)

device_info('PHRCRG1', 'router', hostname='PHRCRG1', role='router', location='PHRC') # Positional Arguments will be stored in tuple while keyword args are in dictionary

list_info = ['PHRCRG1', 'router']
dict_info = {
    'hostname': 'PHRCRG1',
    'role': 'router',
    'location': 'PHRC'
}
device_info(list_info, dict_info) # Info are treated as positional arguments
device_info(*list_info, **dict_info)


### Function example
# Number of days per month. First value is 0 for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''Return True for leap years, False for non-leap years.'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    '''Return number of days in that month in that year'''
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2020, 2))