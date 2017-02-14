while True:
    print('Enter your age:')
    age = raw_input()
    if age.isdigit():
        break
    print('Please enter your name.')

while True:
    print('Select a new passoword(letters and numbers only):')
    password = raw_input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
