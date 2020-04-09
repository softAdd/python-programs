# 3.1
var_int = 10
var_float = 8.4
var_str = 'No'
# 3.2
big_int = var_int * 3.5
# 3.3
var_float -= 1
# 3.4
var_int / var_float
big_int / var_float
# 3.5
var_str = ('No' * 2) + ('Yes' * 3)
# 3.6: 10 7.4, NoNoYesYesYes 35.0
print(var_int, var_float, var_str, big_int)

# 4.1
example_int_1 = 1
example_int_2 = 2
# 4.2: true, true, false, false
print(example_int_1 == 1 and example_int_2 == 2)
print(example_int_1 != 2 and example_int_2 != 1)
print(example_int_1 == 1 and example_int_2 == 1)
print(example_int_1 == 2 and example_int_2 == 2)
# 4.3: true, true, false, false
print(example_int_1 == 1 or example_int_2 == 1)
print(example_int_1 == 2 or example_int_2 == 2)
print(example_int_1 != 1 or example_int_2 != 2)
print(example_int_1 > 1 or example_int_2 > 2)
# 4.4: false, true, false
print('a' > 'b')
print('a' < 'b')
print('a' == 'b')