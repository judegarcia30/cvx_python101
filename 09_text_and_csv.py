# Read File objects
f = open('./files/sample.txt', 'r')
data = f.read()
f.close() # Always close the file

# Context manager
with open('./files/sample.txt', 'r') as f:
    # data_read = f.read() # Read everything
    # data_readline = f.readline() # first line of the text data is returned
    data_readlines = f.readlines() # return a list of lines for the text
    print(data_readlines)

# Write file
with open('./write_files/sample.txt', 'w') as f:
    f.write("Text write")

with open('./write_files/sample.txt', 'a') as f:
    f.write("\nAppended text line")


# Read CSV
import csv
# Reading csv using reader method
with open('./files/devices.csv', 'r') as csv_readfile:
    csv_reader = csv.reader(csv_readfile)
    for row in csv_reader:
        print(row)

# Reading csv using DictReader method
with open('./files/devices.csv', 'r') as csv_readfile:
    csv_reader = csv.DictReader(csv_readfile)
    for row in csv_reader:
        print(row)
        # print(f"{row['hostname']} :: {row['ip']} :: {row['os']} :: {row['serial_number']}")

# Writing csv using writer method
data_to_write = [
    ['PHRCSL37F19', '146.40.228.5', 'IOS', 'FXS1737Q4KD'],
    ['PHRCSL37F18' , '146.40.228.4' , 'IOS' , 'FOX1529GFGE'],
    ['PHRCSL36F17' , '146.40.227.5' , 'IOS' , 'SPE173800DJ'],
    ['PHRCSL36F16' , '146.40.227.4' , 'IOS' , 'FOX1529GFNC'],
    ['PHRCSL35F15' , '146.40.226.4' , 'IOS' , 'FOX1529GFGT']
]
with open('./write_files/csvwriter.csv', 'w') as csv_writefile:
    csv_writer = csv.writer(csv_writefile)
    for data in data_to_write:
        csv_writer.writerow(data)

# Writing csv using DictWriter method
data_to_write = [
    {'Hostname': 'PHRCSL37F19', 'IP address': '146.40.228.5', 'OS': 'IOS', 'Serial Number': 'FXS1737Q4KD'},
    {'Hostname': 'PHRCSL37F18', 'IP address': '146.40.228.4', 'OS': 'IOS', 'Serial Number': 'FOX1529GFGE'},
    {'Hostname': 'PHRCSL36F17', 'IP address': '146.40.227.5', 'OS': 'IOS', 'Serial Number': 'SPE173800DJ'},
    {'Hostname': 'PHRCSL36F16', 'IP address': '146.40.227.4', 'OS': 'IOS', 'Serial Number': 'FOX1529GFNC'},
    {'Hostname': 'PHRCSL35F15', 'IP address': '146.40.226.4', 'OS': 'IOS', 'Serial Number': 'FOX1529GFGT'}
]
with open('./write_files/csvdictwriter.csv', 'w') as csv_writefile:
    headers = ['Hostname', 'IP address', 'OS', 'Serial Number']
    writer = csv.DictWriter(csv_writefile, fieldnames=headers)
    writer.writeheader()
    for data in data_to_write:
        writer.writerow(data)