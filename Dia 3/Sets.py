mi_set = set([1,1,1,2,3,4,4,2,3,4,5])
print(type(mi_set))
print(mi_set)

print(1 in mi_set)

s1 = {1,2,3}
s2 = {4,5,6}
s1.add(7)
s2.remove(6)
s1.discard(8)
s2.pop()
s1.clear()
s3 = s1.union(s2)
print(s3)
