# List and Tuples allows us to work with sequential data
# Sets are unordered collection of values with no duplicates

network_devices = [] # Empty List; create list using square bracket []
network_devices = ['router', 'switch', 'firewall', 'steelhead', 'access_point'] # List
print(len(network_devices)) # number of values of the list

# To access values of the list, use the index location using square bracket
print(network_devices[0]) # First Value
print(network_devices[-1]) # Last Value
print(network_devices[0:2]) # Access range values

# List methods
dir(list())
help(list())
network_devices.append('loadbalancer') # Added at the end of the list
network_devices.insert(0, 'wlc') # Takes 2 argument, location/index and value
add_devices = ['wlc', 'loadbalancer']
network_devices.extend(add_devices)

# Convert list into a string using string join method
network_list_to_string = ', '.join(network_devices)
print(network_list_to_string)

# Convert string into a list using string split method
network_string_to_list = network_list_to_string.split(', ')
print(network_string_to_list)

# Tuples are very similar to list but they cannot be modified.
# List - Mutable; Tuples - Immutable
my_tuple = ('Chevron', 'Holdings', 'Inc') # Create tuple using parenthesis ()


# Sets; doesnt care with order and throw away duplicate values
network_devices = {'router', 'switch', 'firewall', 'steelhead', 'access_point'}
security_devices = {'firewall', 'loadbalancer', 'proxy'}

print(network_devices.intersection(security_devices)) # Check what sets have in common
print(network_devices.difference(security_devices)) # Difference between network and security devices
print(network_devices.union(security_devices)) # combine the 2 sets