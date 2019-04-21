"""
ID: eshmeis1
LANG: PYTHON3
TASK: ride
"""
mapping = {
	'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
	'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
	'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
	'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
	'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
	'Z': 26
}


def getValue(str):
	value = 1
	for char in str:
		value *= mapping[char]
	return value % 47


fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
comet, group = fin.readline().strip(), fin.readline().strip()
if getValue(comet) == getValue(group):
	fout.write("GO" + '\n')
else:
    fout.write("STAY" + '\n')
fout.close()