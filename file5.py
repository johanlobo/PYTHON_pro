employees={}
with open(r'C:\Users\Juvie Leona\Documents\employees.txt') as newfile:
    for i in newfile:
        w=i.split(';')
        if w[0]=='pic':
            continue
        employees[w[0]]=w[1].strip()

salaries={}
with open(r'C:\Users\Juvie Leona\Documents\salaries.txt') as newfile:
    for i in newfile:
        w=i.split(';')
        if w[0]=='pic':
            continue
        salaries[w[0]]=int(w[1])+int(w[2])

for k,v in employees.items():
    if k in salaries:
     salary=salaries[k]
     print(f'{v} has a salary of {salary}')
    else:
     print(f'{v} has no salary information')