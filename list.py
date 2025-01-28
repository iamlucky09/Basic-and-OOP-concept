# yo list ko euta example ho
def extend(val,lst=[]):
    lst.append(val)
    return lst

list1=extend(10)
list2=extend('a')
list3=extend(12,[])
print(list1)
print(list3)

# yo chai arko process le ho jun ma chai naya list banayera implemented garincha

def extend_list(val, lst=None):
    if lst is None: 
        lst = []  
    lst.append(val)
    return lst

list1=extend_list('a')
list2=extend_list('a')
list3=extend_list(12,[])
print(list1)
print(list3)
