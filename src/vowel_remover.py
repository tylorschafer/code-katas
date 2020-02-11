def shortcut (input):
    vowels = ['a','e','i','o','u']
    output = ''
    for char in input:
        if char not in vowels:
            output += char
    return output
