def shortcut (input):
    vowels = ['a','e','i','o','u']
    for char in input:
        if char in vowels:
            output = input.replace(char, '')
    return output
