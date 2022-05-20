tuple=("Rahul",123,9172501144,'john','rohan')

print(tuple)
print(tuple[0])
print(tuple[:3])
print(tuple[2:])
print(tuple[1:4])
print(tuple+tuple)

tuple2 = (tuple,tuple)
print("tuple2 : ",tuple2)


t = ('rahul','masal',123)

c = list(t)
print(c)
c[1]='ROHIT'
print(c)