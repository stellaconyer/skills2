# Write a function that takes an iterable (something you can loop through, ie: string, list, or tuple) and produces a dictionary with all distinct elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
        unique_dict = {}
        for item in some_iterable:
            unique_dict[item] = unique_dict.get(item, 0)+1
        return unique_dict

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
def common_items(list1, list2):
    common_list = []
    counter = 0
    second_counter = 0


    while counter < len(list1):
        item_to_check = list1[counter]
        counter += 1

        while second_counter < len(list2):
            if item_to_check == list2[second_counter]:
                common_list.append(item_to_check)
            second_counter += 1    
        second_counter = 0

    print common_list

long_list = ["a", "not", "as", "short", "list"]
short_list = ["a", "short", "list"]


common_items(long_list,short_list)

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    return []



