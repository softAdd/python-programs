# task 1
print('Введите количество шаров:')
balls = int(input())
necessary_balls = 1
lines = 0

while (balls >= necessary_balls):
  balls = balls - necessary_balls
  necessary_balls += 1
  lines += 1

print('Количество рядов:', lines)

# task 2
print('Введите числа через пробел:')
numbers = input().split(' ')
numbers = map(int, numbers)
numbers = list(numbers)
print('Введите число b:')
b = int(input())
numbers = list(filter(lambda x: x > b, numbers))
ft = __import__('functools')
result = ft.reduce(lambda acc,cv: acc + cv, numbers)
print('Сумма элементов, больших числа b:', result)

# task 3
print('Введите x (x > 0, x < 1):')
x = float(input())

if (x > 0 and x < 1):
  divider = 1
  current_member = 1 / (divider ** 2)
  row_result = current_member
  while(current_member >= x):
    divider += 1
    current_member = 1 / (divider ** 2)
    row_result += current_member

  print('Сумма ряда:', row_result)
  print('При x:', x)
  print('Со значением последнего элемента:', current_member)
else:
  print('Неверно указано число.')
  sys = __import__('sys')
  sys.exit()