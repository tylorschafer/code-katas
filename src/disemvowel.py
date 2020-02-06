def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U']
    for char in string:
        if char in vowels:
            string = string.replace(char, '')
    return string
