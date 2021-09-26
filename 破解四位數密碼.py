Password = input("Set Password:")
pwdFound = False
for p1 in range(10):
  for p2 in range(10):
    for p3 in range(10):
      for p4 in range(11):
        if p4 == 0:
          pwd = str(p1) + str(p2) + str(p3)
        else:
          p4 = p4 - 1
          pwd = str(p1) + str(p2) + str(p3) + str(p4)
          
        if pwd == Password:
          print("Bingo: ", pwd)
          pwdFound = True
          break
        else:
          print(pwd)
      if pwdFound: break
    if pwdFound: break
  if pwdFound: break
