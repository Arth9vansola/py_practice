# tuples are immutable --> cannot changed in main tuple

a = (1,2,3,4,5,6,7,8,9,10)

# print(a.count(2))
# print(a.index(2))

t = (0 ,1, 2, 3)

# print(t[1:])
# print(t[::-1]) # reverse a tuple
# print(t[::]) # print  shallow copy means it will  change the original tuple
# print(t[2:4])
num = t[::]
print(t)
print(num)

# packing and unpacking in tuple

b =("arth","vansola",15) # packing
(name, surname, age) = b # unpacking
print(name)
print(surname)
print(age)

