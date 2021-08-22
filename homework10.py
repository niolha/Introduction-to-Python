import random
from random import randint
import string

# 1.###################################################


def create_new_list1(my_list):
    new_list = []
    for index in range(len(my_list)):
        if index % 2 != 0:
            new_list.append(my_list[index][::-1])
        else:
            new_list.append(my_list[index])
    return new_list


animals = ['cats', 'dogs', 'birds', 'insects', 'and', 'people']
print(create_new_list1(animals))

# 2.###################################################


def create_new_list2(my_list):
    new_list = [value for value in my_list if value.lower().startswith('a')]
    return new_list


fruits = ['bananas', 'apple', 'orange', 'strawberry', 'pear', 'melon', 'Apple']
print(create_new_list2(fruits))

# 3.###################################################


def create_new_list3(my_list):
    new_list = [value for value in my_list if 'a' in value.lower()]
    return new_list


fruits = ['bananas', 'apple', 'orange', 'strawberry', 'pear', 'melon', 'Apple']
print(create_new_list3(fruits))

# 4.###################################################


def create_new_list4(my_list):
    new_list = [value for value in my_list if type(value) == str]
    return new_list


values = [1, 2, 3, "11", "22", 33, ""]
print(create_new_list4(values))

# 5.###################################################


def create_new_list5(my_str):
    my_list = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
    # my_list1 = []
    # for symbol in set(my_str):
    #     if my_str.count(symbol) == 1:
    #         my_list.append(symbol)
    return my_list


symbols = 'qweqweasdzxczxc'
print(create_new_list5(symbols))

# 6.###################################################


def create_new_list6(my_str, my_str2):
    my_list = list(set(my_str) & set(my_str2))
    return my_list


first_str = 'mystrnotmystr'
second_str = 'hellomystr'
print(create_new_list6(first_str, second_str))

# 7.###################################################


def create_new_list7(my_str1, my_str2):
    my_set1 = set()
    for symbol in set(my_str1):
        if my_str1.count(symbol) == 1:
            my_set1.update(symbol)
    my_set2 = set()
    for symbol in set(my_str2):
        if my_str2.count(symbol) == 1:
            my_set2.update(symbol)
    my_list = list(my_set1.intersection(my_set2))
    return my_list


first_str = 'mystrnotmystr'
second_str = 'hellomystr'
print(create_new_list7(first_str, second_str))

# 8.###################################################
surnames = ["potter", "granger", "weasley", "malfoy"]
domains = ["com", "net", "ua", "org", "gov"]


def create_email(surname, domain):
    index_s = randint(0, len(surname)-1)
    surname = surname[index_s]
    number = randint(100, 999)
    index_d = randint(0, len(domain)-1)
    domain = domain[index_d]
    letters = string.ascii_lowercase
    length = randint(5, 7)
    r_str = ''.join(random.choice(letters) for _ in range(length))
    email = f"{surname}.{number}@{r_str}.{domain}"
    return email


print(create_email(surnames, domains))
