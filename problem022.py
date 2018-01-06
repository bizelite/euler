# Calcualte Sum of All Names

import sys
import string

filename = sys.argv[1]

def sum_of_each_name(name):
    alphabet = string.ascii_uppercase
    total = 0
    d = {}
    for i, j in zip(alphabet, range(1, 27)):
        d[i] = j

    for c in name:
        if c in d.keys():
            total += d[c]

    return total


def serial(lst, name):
    return sorted(lst).index(name)+1


if __name__ == '__main__':
    with open(filename, 'r') as fread:
        name_list = fread.read().split(',')
        for i in range(len(name_list)):
            name_list[i] = name_list[i].strip('"')
    
    sum_of_all_names = 0

    for name in name_list:
        result = sum_of_each_name(name) * serial(name_list, name)
        sum_of_all_names += result

    print(sum_of_all_names)





        
