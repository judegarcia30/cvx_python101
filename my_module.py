print('Imported my_module')

username = 'jude'
password = 'jude123'

def find_index(to_search, target):
    for index, value in enumerate(to_search):
        if value == target:
            return index