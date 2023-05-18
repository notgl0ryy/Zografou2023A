list=['3','5','3','2','1','1','3']
list_unique=[]
for item in list:

    if item not in list_unique:
        list_unique.append(item)
        print(list_unique)
