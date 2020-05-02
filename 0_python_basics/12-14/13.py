# task 1
def sum(a, b, c):
  return a + b + c

result = sum(1, 2, 3)
print(result)

# task 2
def first_func():
  print('Первая функция')

def second_func():
  first_func()
  print('Вторая функция')

second_func()