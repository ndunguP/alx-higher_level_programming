#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    sum = 0
    num_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    new_list = []
    for i in range(len(roman_string)):
        if roman_string[i] in num_dict.keys():
            new_list.append(num_dict[roman_string[i]])
        else:
            return 0
    x = 0
    while (x < len(new_list) - 1):
        if new_list[x] >= new_list[x + 1]:
            sum += new_list[x]
        elif new_list[x] <= new_list[x + 1]:
            sum -= new_list[x]
        else:
            sum += new_list[x]
        x += 1
    sum += new_list[x]
    return abs(sum)
