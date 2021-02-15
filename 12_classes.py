# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods. 
# A Class is like an object constructor, or a "blueprint" for creating objects.
# Data and functions inside a class are called attribute and methods

class Network_device:
    def __init__(self, hostname, ip_address, role, site): # Initialize your object
        # Attributes
        self.hostname = hostname
        self.ip_address = ip_address
        self.role = role
        self.site = site

    def domain_name(self, domain='chevrontexaco'): # Creating a Method
        return f"{self.hostname}.{self.site}.{domain}.com"

phrcrg1 = Network_device('PHRCRG1', '146.40.123.122', 'router', 'PHRC')
phrcsl05f03 = Network_device('PHRCSL05F03', '146.40.233.4', 'switch', 'PHRC')
# import ipdb; ipdb.set_trace()
# calling the method
print(phrcrg1.domain_name())
print(phrcsl05f03.domain_name(domain='devnet'))
# print(Network_device.domain_name(phrcrg1))
