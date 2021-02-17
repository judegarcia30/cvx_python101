# Given a Python list you should be able to display Python list in the following order
aList = [100, 200, 300, 400, 500]
# Expected output:
# [500, 400, 300, 200, 100]

# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# Remove empty strings from the list of strings
devices = ["Router", "", "Switch", "Access-Point", "", "Firewall"]
# Expected output:
# ["Router", "Switch", "Access-Point", "Firewall"]

# Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list
# Given List:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist_to_be_added = ["h", "i", "j"]

# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# Find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:
# list1 = [5, 10, 15, 200, 25, 50, 20]

# remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]
