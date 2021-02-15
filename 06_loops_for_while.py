import ipaddress
nums = [1, 2, 3, 4, 5]
site_codes = ['PHRC', 'PHHQ', 'SGDC', 'SINQX']
device = {
    'hostname': 'PHRCRG1',
    'ip_address': '146.40.123.122',
    'location': ['makati', 'philippines'],
    'router_number': 1
}

# Break concept
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# List loop including index and value
for index, value in enumerate(site_codes, start=1):
    print(index, value)

# Dictionary loop
for key, value in device.items():
    print(key, value)

# Loop with range
ip = ipaddress.ip_address(device['ip_address'])
for i in range(1, 11):
    print(str(ip + i))

# While loops keeps going until certain condition are met
x = 0
ip = ipaddress.ip_address('10.1.1.0')
while x < 10:
    print(str(ip + x))
    x += 1

# For break
x = 0
ip = ipaddress.ip_address('10.1.1.1')
while True:
    if x == 5:
        break
    print(str(ip + x))
    x += 1