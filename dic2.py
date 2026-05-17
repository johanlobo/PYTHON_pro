wl = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]
def cou(wl):
    dic={}
    for i in wl:
        init=i[0]
        if init not in dic:
            dic[init]=[]
        dic[init].append(i)
    return dic

groups=cou(wl)

for k,v in groups.items():
    print(f'contents for {k}')
    for i in v:
        print(i)
print()


staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("lobo", None)
if deleted == None:
  print("This person is not a staff member")
else:
  print(deleted, "deleted")