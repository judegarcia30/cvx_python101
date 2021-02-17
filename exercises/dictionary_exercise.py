# Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Access the value of key ‘history’
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
# Expected output:
# 80

# Create a new dictionary by extracting the following keys from a given dictionary
# Given dictionary:
sampleDict = {
  "hostname": "PHRCRG1",
  "ip": "192.168.1.1",
  "device_type": "router",
  "location": "Philippines"  
}
# Keys to extract
# keys = ["hostname", "ip"]

# Expected output:
# {'hostname': 'PHRCRG1', 'ip': '192.168.1.1'}

# Delete set of keys from Python Dictionary
# Given dictionary:
sampleDict = {
  "hostname": "PHRCRG1",
  "ip": "192.168.1.1",
  "device_type": "router",
  "location": "Philippines"  
}
keysToRemove = ["hostname", "ip"]
# Expected output:
# {'device_type': 'router', 'location': Philippines}

# Rename key location to snmp_location in the following dictionary
sampleDict = {
  "hostname": "PHRCRG1",
  "ip": "192.168.1.1",
  "device_type": "router",
  "location": "Philippines"  
}
# Expected output:
# {
#   "hostname": "PHRCRG1",
#   "ip": "192.168.1.1",
#   "device_type": "router",
#   "snmp_location": "Philippines"  
# }

# Given a Python dictionary, Change us device_type to router
sampleDict = {
     'apac': {'hostname': 'PHRCSL05F03', 'device_type': "switch"},
     'emea': {'hostname': 'WFCSL5E1', 'device_type': "switch"},
     'us': {'hostname': 'HOU150-PE1', 'device_type': "switch"}
}
# Expected output:
# sampleDict = {
#     'apac': {'hostname': 'PHRCSL05F03', 'device_type': "switch"},
#     'emea': {'hostname': 'WFCSL5E1', 'device_type': "switch"},
#     'us': {'hostname': 'HOU150-PE1', 'device_type': "router"}
# }
