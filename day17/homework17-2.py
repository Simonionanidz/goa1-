def filter_long_strings(string_list):
    result_list = []
    for string in string_list:
        if len(string) > 5:
            result_list.append(string)
    return result_list


input_list = ["apple", "banana", "orange", "kiwi", "strawberry", "pineapple"]
filtered_list = filter_long_strings(input_list)
print("Strings with length greater than 5:", filtered_list)