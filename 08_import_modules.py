import my_module # import my_module from current dir
# import my module as mm
# from my_module import username, password as pw, find_index

network_devices = ['router', 'switch', 'firewall', 'steelhead', 'access_point']

creds_username = my_module.username
creds_password = my_module.password
print(creds_username, creds_password)

index = my_module.find_index(network_devices, 'firewall')
print(index)

# directory list on where to look for module
import sys
print(sys.path) # First in the list will be the current directory
# Append a directory to sys.path if you have a module in different directory
# sys.path.append('path\to\directory')

# Standard library modules
import datetime, math, os
print(os.__file__) # Modules are just another python file, this will show the location of the file for you to view