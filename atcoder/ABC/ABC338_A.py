i_str = input()

chkstr = i_str[0].upper() + i_str[1:].lower()

if i_str == chkstr:
  print("Yes")
else:
  print("No")