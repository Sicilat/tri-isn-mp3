ltri = [35, 9, 57, 196, 3, 83, 21, 87, 6, 66, 166, 30, 57, 71, 125, 2, 4, 13, 199, 1]
lfin = []
print(len(lfin))
i = 0
w = 0

while len(lfin) != len(ltri):
	p = 0
	if len(lfin) == 0:
		lfin.append(ltri[i])
		w = 1
	while w == 0:
		if ltri[i] <= lfin[p]:
			lfin.insert(p, ltri[i])
			w = 1
		elif p == len(lfin) -1:
			lfin.append(ltri[i])
			w = 1
		p += 1
	i += 1
	w = 0

print(ltri)
print(lfin)