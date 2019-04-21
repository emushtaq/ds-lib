"""
ID: eshmeis1
LANG: PYTHON3
TASK: test
"""
import sys
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
sys.stderr.write(str(sum))
fout.write (str(sum) + '\n')
fout.close()