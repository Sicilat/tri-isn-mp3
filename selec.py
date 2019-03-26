ltri = [35, 9, 57, 196, 3, 83, 21, 87, 6, 66, 166, 30, 57, 71, 125, 2, 4, 13, 199, 1]

print(ltri)

for i in range(len(ltri) - 1, 0, -1):
      x = 0
      for p in range(1,i+1):
          if ltri[p] > ltri[x]:
              x = p

      temp = ltri[i]
      ltri[i] = ltri[x]
      ltri[x] = temp

print(ltri)