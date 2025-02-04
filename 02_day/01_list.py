# list are mutable---> can be changed in main list

from sympy import false


l = [1,2,40,false,"arth"]
print(l[4][0:2])

# st = "vansola"
# print(st[1:])


lamp = [10,5,6,80,55,32,85]
# lamp.sort()
# lamp.reverse()
# lamp.append(100)
# lamp.remove(100)
# lamp.pop(2)
lamp.insert(2, 100)
print(lamp[2:5])
