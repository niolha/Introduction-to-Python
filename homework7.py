###1###################################################
### вариант 1
my_number = 213870002056100
my_number_str = str(my_number)
my_nul = '0'
result_1 = my_number_str.count(my_nul)
print(result_1)

### вариант 2
# my_number = 213870002056100
# my_number_str = str(my_number)
# result = 0
# for digit in my_number_str:
#     if digit == '0':
#         result = result + 1
# print(result)

###2###################################################
my_number = 2138700020561000
my_number_str = reversed(str(my_number))
result = 0
for digit in my_number_str:
    if digit == '0':
        result = result + 1
    else:
        break
print(result)

###3###################################################
my_list_1 = [5, 4, 2, 6, 2, 4]
my_list_2 = [9, 0, 5, 4, 4, 3, 7, 8]
my_result = []
my_result.extend(my_list_1[::2])
my_result.extend(my_list_2[1::2])
print(my_result)

###4###################################################
my_list = [1, 2, 3, 4]
new_list = []
for digit in my_list[1::]:
    new_list.append(digit)
new_list.append(my_list[0])
print(new_list)

### через генератор списков
# my_list = [1, 2, 3, 4]
# new_list = [digit for digit in my_list[1::]]
# new_list.append(my_list[0])
# print(new_list)

### через метод.pop
# my_list = [1, 2, 3, 4]
# popped_number = my_list.pop(0)
# new_list = my_list.copy()
# new_list.append(popped_number)
# print(new_list)

###5###################################################
my_list = [1, 2, 3, 4]
popped_number = my_list.pop(0)
my_list.append(popped_number)
print(my_list)

###6###################################################
my_str = '43 больше чем 34 но меньше чем 56'
my_numbers = my_str.split()
result = 0
for numbers in my_numbers:
    if numbers.isdigit():
        result = result + int(numbers)
print(result)

###7###################################################
# my_str = "My looong string My long string9ghf"
# l_limit = "o"
# r_limit = "g"
# start_index = 0
# for index in range(len(my_str)):
#     if my_str[index] == l_limit:
#         start_index = index + 1
#         break
# end_index = 0
# for index in range(len(my_str)):
#     if my_str[index] == r_limit:
#         end_index = index
# sub_str = my_str[start_index:end_index]
# print(sub_str)

my_str = "My looong string My long string9ghf"
l_limit = my_str.find('o')
r_limit = my_str.rfind('g')
sub_str = my_str[l_limit:r_limit]
print(sub_str)

###8###################################################
my_str = 'abcdefghj'
result = []
for index in range(len(my_str)):
    if index % 2 == 0:
        couple = my_str[index:index+2]
        if len(couple) == 1:
            couple = my_str[index] + "_"
        result.append(couple)
print(result)

### через функцию enumerate
# my_str = 'abcdefghj'
# result = []
# for index, value in enumerate(my_str):
#     if index % 2 == 0:
#         couple = my_str[index:index+2]
#         if len(couple) > 1:
#             result.append(couple)
#         else:
#             result.append(value + '_')
# print(result)

###9###################################################
numbers = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0
for index in range(len(numbers)):
    if index == 0 or index == len(numbers) - 1:
        continue
    if numbers[index - 1] + numbers[index + 1] < numbers[index]:
        result = result + 1
print(result)
