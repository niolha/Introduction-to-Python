####################################################
value = 5
new_value = value / 2 if value < 100 else -value
print(new_value)

####################################################
value = 124
new_value = 1 if value < 100 else 0
print(new_value)

####################################################
value = 100
new_value = True if value < 100 else False
print(new_value)

####################################################
my_str = 'have a good day'
print(my_str[::2])

################### Нечетные #######################
my_str = 'have a good day'
print(my_str[1::2])

####################################################
my_str = 'zxasqw'
if len(my_str) < 5:
    my_str = my_str * 2
print(my_str)

####################################################
my_str = 'zxa'
if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
print(my_str)
