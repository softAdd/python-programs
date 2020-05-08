# task 1
PI = 3.14

def func1(num):
  n = num * 5
  print(n)

func1(PI)
func1(111)
func1('string')

# task 2
def func(n):
  if n < 3:
    n = n * 10

  return n

a = 2
b = func(a)