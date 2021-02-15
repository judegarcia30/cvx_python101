# Dictionary are key value pairs
device = {
    'hostname': 'PHRCRG1', # Key is hostname, value is PHRCRG1
    'ip_address': '146.40.123.122',
    'location': ['makati', 'philippines'],
    'router_number': 1
}

# To access dictionary value
print(device['hostname'])
print(device.get('ip_address')) # Returns none if KeyError

# To add new key and value pair to an existing dictionary
device['vendor'] = 'Cisco'

# If key exists, it will just update the value for that key
device['router_number'] = 2

# To update or add multiple key value pair
device.update({'router_number': 3, 'role': 'router', 'hostname': 'PHRCRG2'})

# To delete a key value pair
del device['hostname']
device.pop('ip_address', None) # Throws None value if the key doesnt exist

# Dictionary methods
dir(dict())
help(dict())