def count_words(file):
    words = len(file.split())
    return words


def count_chars(file):
    file = file.lower()
    chars_dict = {}
    for char in file:
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict


def sort_on(dict):
    return dict["num"]


def sort_chars(counted_dict):
    sorted = []
    for char in counted_dict:
        if char.isalpha():
            temp_dict = {}
            temp_dict["char"] = char
            temp_dict["num"] = counted_dict[char]
            sorted.append(temp_dict)
    sorted.sort(reverse=True, key=sort_on)
    return sorted