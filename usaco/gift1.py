"""
ID: eshmeis1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')
persons = {}
person_order = []
np = int(fin.readline().strip())
for i in range(np):
    person = fin.readline().strip()
    persons[person] = {'amount': 0}
    person_order.append(person)

for i in range(np):
    member = fin.readline().strip()
    amount, no_of_people = map(int, fin.readline().split())
    persons[member]['amount'] += amount
    pp_amount = int(amount/no_of_people) if no_of_people > 0 else 0
    for i in range(no_of_people):
        receiver = fin.readline().strip()
        persons[member]['amount'] -= pp_amount
        persons[receiver]['amount'] += int(amount/no_of_people)
    persons[member]['amount'] -= amount

for person in person_order:
    fout.write(f"{person} {persons[person]['amount']}" + '\n')

fout.close()