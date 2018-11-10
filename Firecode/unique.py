def unique_chars_in_string(input_string):

    unique = {}
    for i in input_string:
        unique[i] = unique.get(i, 0) + 1
    maxval = max(unique.keys(), key=(lambda k: unique[k]))
    print(unique)
    if unique[maxval] > 1:
        return False
    else:
        return True
print(unique_chars_in_string("Language"))
