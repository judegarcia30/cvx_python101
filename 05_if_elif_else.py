# Comparisons:
# Equal:                ==
# Not Equal:            != 
# Greater than:         >
# Less than:            <
# Greater or Equal:     >=
# Less or Equal:        <=

languange = 'Python'

if languange == 'Python':
    print(f'Languange is Python')
elif languange == 'Java':
    print(f'Languange is Java')
else:
    print('No match')

# Boolean Operators
# and
# or
# not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Logged in')
else:
    print('Authentication error')

# False values
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '', (), [].
#     Any empty mapping. For example, {}.

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')