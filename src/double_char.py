def double_char(string):
    doubles = [char + char for char in string]
    return ''.join(doubles)
