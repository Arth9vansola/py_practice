# set are mutable
# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

# set1.add(11)
# set1.remove(11)
# print(len(set1))
# set1.pop()
# set1.pop()
# set1.pop()
# set1.remove(10)
# set1.discard(9)
# set1.clear()
# set1.update({11,12,13,14,15})
tap = set1.union({10,11,12,13,14,15})
print(tap)
car = set1.intersection({10,12})
print(car)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))