school = {
  '1a': 30,
  '1b': 25,
  '1c': 23,
  '2a': 22,
  '2b': 27,
  '3a': 23,
  '4a': 26,
  '4b': 29,
  '4c': 32,
  '5a': 33,
}

print('В классе 1a:', school['1a'])

school['1a'] = 29
school['1b'] = 29
school['1c'] = 29
school['5b'] = 29
school['5c'] = 29
del(school['4c'])

print(school)