# 1.###################################################
my_list = ['cats', 'dogs', 'birds', 'insects', 'and', 'people']
new_list = []
for index in range(len(my_list)):
    if index % 2 != 0:
        new_list.append(my_list[index][::-1])
    else:
        new_list.append(my_list[index])
print(new_list)

# my_list = ['cats', 'dogs', 'birds', 'insects', 'and', 'people']
# new_list = []
# for index, value in enumerate(my_list):
#     if index % 2 != 0:
#         new_list.append(value[::-1])
#     else:
#         new_list.append(value)
# print(new_list)

# 2.###################################################
my_list = ['asdf', 'hfyf', 'Aere', 'asefnbvhjnb']
new_list = [value for value in my_list if value.lower().startswith('a')]
print(new_list)

# my_list = ['asdf', 'hfyf', 'Aere', 'asefnbvhjnb']
# new_list = []
# for value in my_list:
#     if value.lower().startswith('a'):
#         new_list.append(value)
# print(new_list)

# 3.###################################################
my_list = ['asdf', 'hfyf', 'reA', 'asefnbaavhjnb']
new_list = [value for value in my_list if 'a' in value.lower()]
print(new_list)

# my_list = ['asdf', 'hfyf', 'reA', 'asefnbaavhjnb']
# new_list = []
# for value in my_list:
#     if 'a' in value.lower():
#         new_list.append(value)
# print(new_list)

# 4.###################################################
my_list = [1, 2, 3, "11", "22", 33, ""]
new_list = [value for value in my_list if type(value) == str]
print(new_list)

# my_list = [1, 2, 3, "11", "22", 33, ""]
# new_list = []
# for value in my_list:
#     if type(value) == str:
#         new_list.append(value)
# print(new_list)

# 5.###################################################
my_str = 'qweasdqwezxcqwe'
my_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

# my_str = 'qweasdqwezxcqwe'
# my_list = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]
# print(my_list)

# 6.###################################################
my_str = 'mystrnotmystr'
my_str2 = 'hellomystr'
my_list = list(set(my_str) & set(my_str2))
print(my_list)

# my_str = 'mystrnotmystr'
# my_str2 = 'hellomystr'
# my_set = set(my_str)
# my_set2 = set(my_str2)
# my_list = list(my_set.intersection(my_str2))
# print(my_list)

# 7.###################################################
my_str1 = 'mystrnotmystr'
my_str2 = 'hellomystr'
my_set1 = set()
for symbol in set(my_str1):
    if my_str1.count(symbol) == 1:
        my_set1.update(symbol)
my_set2 = set()
for symbol in set(my_str2):
    if my_str2.count(symbol) == 1:
        my_set2.update(symbol)
my_list = list(my_set1.intersection(my_set2))
print(my_list)

# my_str1 = 'mystrnotmystr'
# my_str2 = 'hellomystr'
# my_set1 = set(my_str1)
# for symbol in set(my_str1):
#     if my_str1.count(symbol) > 1:
#         my_set1.remove(symbol)
# my_set2 = set(my_str2)
# for symbol in set(my_str2):
#     if my_str2.count(symbol) > 1:
#         my_set2.remove(symbol)
# my_list = list(my_set1 & my_set2)
# print(my_list)

# 8.###################################################
address = {'country': 'Ukraine',
           'city': 'Zaporozhian Host',
           'street': 'Sich'}
occupation = {'job': 'Full time',
              'position': 'Hetman'}
person = {'surname': 'Khmelnytsky',
          'name': 'Bohdan',
          'age': '62',
          'address': address,
          'occupation': occupation}
print(person)

# 9.###################################################
biscuits = {'flour': 300,
            'milk': 100,
            'butter': 80,
            'eggs': '2pcs'}
custard = {'sugar': 100,
           'butter': 120,
           'vanilla': 5,
           'sour cream': 100}
glaze = {'coca': 50,
         'sugar': 50,
         'butter': 60}
cake_ingredients = {'biscuits': biscuits,
               'custerd': custard,
               'glaze': glaze}
print(cake_ingredients)

# 10.###################################################
people = [{"name": "John", "age": 15},
          {"name": "Jack", "age": 45},
          {"name": "Peter", "age": 90},
          {"name": "Steven", "age": 15},
          {"name": "Marcus", "age": 90},
          {"name": "Poul", "age": 89}]
### а)
age = []
for person in people:
    age.append(person["age"])
min_age = min(age)
for person in people:
    if person["age"] == min_age:
        print(person["name"])

### б)
longest_name_len = 0
for person in people:
    longest_name_len = max(longest_name_len, len(person["name"]))
for person in people:
    if len(person["name"]) == longest_name_len:
        print(person["name"])

### в)
average_age = []
for person in people:
    average_age.append(person["age"])
print(sum(average_age) / len(average_age))

# 11.###################################################
my_dict_1 = {1: 11, 2: 22, 3: 33}
my_dict_2 = {1: 111, 2: 222, 4: 444}
### а)
my_list1 = list(my_dict_1.keys() & my_dict_2.keys())
print(my_list1)

### б)
my_list2 = list(my_dict_1.keys() - my_dict_2.keys())
print(my_list2)

### в)
new_dict = {
    key: my_dict_1[key] for key in set(my_dict_1) - set(my_dict_2)
}
print(new_dict)

# new_dict = {}
# for key in my_dict_1.keys() - my_dict_2.keys():
#     new_dict[key] = my_dict_1[key]
# print(new_dict)

### г)
new_dict2 = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict2[key] = value
    else:
        new_dict2[key] = [value, my_dict_2[key]]
for key, value in my_dict_2.items():
    if key not in my_dict_1:
        new_dict2[key] = value
print(new_dict2)
