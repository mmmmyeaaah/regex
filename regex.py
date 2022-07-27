import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r'(\+7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s?\(?(\w+\.)\s(\d{4})\)?)?'

# меняем номера
for id, i in enumerate(contacts_list):
    res = re.sub(pattern, r'+7(\2)\3-\4-\5 \7\8', i[-2])
    contacts_list[id][-2] = res  

# выставляем ФИО 
for id, i in enumerate(contacts_list):
    if len(i[0].split()) == 2:
        a = i[0].split()
        contacts_list[id][0] = a[0]
        contacts_list[id][1] = a[1]

    if len(i[0].split()) == 3:
        a = i[0].split()
        contacts_list[id][0] = a[0]
        contacts_list[id][1] = a[1]
        contacts_list[id][2] = a[2]
        
    if len(i[1].split()) == 2:
        a = i[1].split()
        contacts_list[id][1] = a[0]
        contacts_list[id][2] = a[1]
        
# объединяем и избавляемся от списков с задвоенными ИМЕНАМИ и ФАМИЛИЯМИ          
for numb, i in enumerate(contacts_list):
    for id, j in enumerate(contacts_list):
        if j[0] == i[0] and j[1] == i[1] and j[2] != i[2]:
            if contacts_list[id][2] == '':
                contacts_list[id][2] = contacts_list[numb][2]
            if contacts_list[id][3] == '':
                contacts_list[id][3] = contacts_list[numb][3]
            if contacts_list[id][4] == '':
                contacts_list[id][4] = contacts_list[numb][4]
            if contacts_list[id][5] == '':
                contacts_list[id][5] = contacts_list[numb][5]
            if contacts_list[id][6] == '':
                contacts_list[id][6] = contacts_list[numb][6]
            
            del contacts_list[numb]
            
# объединяем списки с задвоенными ФИО
for numb, i in enumerate(contacts_list):
    for id, j in enumerate(contacts_list):
        if j[0] == i[0] and j[1] == i[1] and j[2] == i[2]:
            if contacts_list[id][3] == '':
                contacts_list[id][3] = contacts_list[numb][3]
            if contacts_list[id][4] == '':
                contacts_list[id][4] = contacts_list[numb][4]
            if contacts_list[id][5] == '':
                contacts_list[id][5] = contacts_list[numb][5]
            if contacts_list[id][6] == '':
                contacts_list[id][6] = contacts_list[numb][6]       

# избавляемся от линего оставшегося списка(в других случаях не сработает, другой вариант так и не доделал..)
for id, i in enumerate(contacts_list):
    if len(i) > 7:
        del contacts_list[id]               
    
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)


