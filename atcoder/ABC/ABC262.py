cur_year = int(input())
temp_year = (cur_year // 4) * 4 + 2
if temp_year >= cur_year:
  print(temp_year)
else:
  print(temp_year + 4)