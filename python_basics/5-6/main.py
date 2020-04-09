# 5.1
int_test = -1

if int_test < 0:
  print('Не больше 0')

int_test = 1

if int_test > 0:
  print('Больше 0')

# 5.2
if int_test > 0:
  print(1)
else:
  print(-1)

# 5.3
int_test = 10

if int_test < 20:
  int_test += 10
  int_test *= 3
  int_test -= 15
else:
  int_test += 2

print(int_test)

# 6.1
first_int = 10
second_int = 20
result = 0

if first_int > second_int:
  result = first_int - second_int
elif first_int < second_int:
  result = first_int + second_int
else:
  result = first_int

print(result)