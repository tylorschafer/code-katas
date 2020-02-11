def shortcut (input):
    vowels = ['a','e','i','o','u']
    output = ''
    for char in input:
        if char in vowels:
            pass
        else:
            output += char
    return output
