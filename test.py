from queue import PriorityQueue as PQ
Q = PQ()

Q.put((3,"Apple"))
Q.put((1,"Banana"))
Q.put((2, "Cherry"))


print(Q.get())
print(Q.get())
print(Q.get())


