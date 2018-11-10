def insert_star_between_pairs(a_string):
    if a_string is None:
        return None
    elif len(a_string) <= 1:
        return a_string
    elif a_string[0:1] == a_string[1:2]:
        return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])

    return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])
print(insert_star_between_pairs("ccc"))