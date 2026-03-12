
import sys
tokenword: set[str | int]= {"tidak bisa"}
print(tokenword)
print (type(tokenword))
print("ukuran memori", sys .getsizeof(tokenword))

katasambung: set[str] = {"kemudian", "lalu", "setelah"}
print(katasambung)
print(type(katasambung))
print("ukuran memori", sys.getsizeof(katasambung))

katasambung.remove("kemudian")
print(katasambung)
tokenword.discard("tidak bisa")
print(tokenword)

tokenword.add("mungkin")
print(tokenword)
tokenword.update(["pasti", "mungkin"])
print(tokenword)

tokenword.remove("mungkin")
tokenword.add("nanti")
print(tokenword)

setA: set[int] = {1, 2, 3, 4}
setB: set[int] = {3, 4, 5, 6}

print(setA|setB)
print(setA&setB)
print(setA-setB)
print(setA^setB)