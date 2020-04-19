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