class emp:
    name ="empty"

e1 =emp()
e1.name = "ahmed"
delattr(e1 ,"name")
print(e1.name) # will print empty becaude it deleted ahmed
