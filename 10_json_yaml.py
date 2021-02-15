import json, yaml

# JSON/YAML File read will return a Python Dictionary
# Python Dictionary type is required in order to write a JSON/YAML file

# Reading YAML File
with open('./files/PHRCSL05F03.yml', 'r') as yml_readfile:
    yml_raw = yaml.safe_load(yml_readfile)
    print(yml_raw)

# Reading JSON File
with open('./files/PHRCSL38F21.json', 'r') as json_readfile:
    json_raw = json.load(json_readfile)
    print(json_raw)

# Writing YAML File
with open('./write_files/PHRCSL38F21.yml', 'w') as yml_writefile:
    yaml.safe_dump(json_raw, yml_writefile, sort_keys=False, indent=2)


# # Writing JSON File
with open('./write_files/PHRCSL05F03.json', 'w') as json_writefile:
    json.dump(yml_raw, json_writefile, sort_keys=False, indent=4)
