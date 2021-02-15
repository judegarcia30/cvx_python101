
try:
    with open('./files/samples.txt', 'r') as f:
        data = f.read()
        # jude = garcia
except FileNotFoundError: # Specific error
    print(f'File Not Found')
except Exception: # General Error
    print(f'Something went wrong')

# Raising Manual exceptions using raise
username = 'jude'
if username != 'admin':
  raise Exception("User is not admin")