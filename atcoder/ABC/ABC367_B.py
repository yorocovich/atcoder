num = input()
result = num.rstrip('0')
if result.endswith('.'):
  result = result[:-1]

print(f'{result}')
