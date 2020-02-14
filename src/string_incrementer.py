import re

def increment_string(string):
    num = re.findall('\d+', string)
    plain_string = re.findall('\D+', string)
    if len(num) > 0:
        new_num = int(num[0]) + 1
        length_diff = len(num[0]) - len(str(new_num))
    else:
        new_num = 1
        length_diff = 0
    new_num_string = str(new_num).rjust(length_diff + 1, '0')
    if len(plain_string) > 0:
        return plain_string[0] + new_num_string
    else:
        return new_num_string
