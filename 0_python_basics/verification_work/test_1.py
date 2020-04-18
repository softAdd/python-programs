import math

# task 1
print('task 1:')
print('x')
x = float(input())
print('y')
y = float(input())
print('z')
z = float(input())

a = y + (x / (y ** 2 + abs(((x ** 2) / (y + x ** 2)))))
b = (1 + (math.tan(z / 2) ** 2)) ** 2

print('a:', a)
print('b:', b)
print('----------------------')

# task 2
print('task 2:')
print('k')
k = float(input())
print('b')
b = float(input())

intersectionX = -(b / k)
intersectionY = b

cathetA = abs(intersectionX)
cathetB = abs(intersectionY)
hypotenuse = math.sqrt(cathetA ** 2 + cathetB ** 2)

triangleArea = (cathetA * cathetB) / 2
trianglePerimeter = cathetA + cathetB + hypotenuse

print('triangle area:', triangleArea)
print('triangle perimeter:', trianglePerimeter)
print('----------------------')