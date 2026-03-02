import sys
# membuat tuple
logsApps = ("user1 login", "user2 login",)
print(logsApps)
print("memiliki ukuran tuple: ", sys.getsizeof(logsApps))

logsApps: list

#buktikan bahwa tuple tidak bisa diubah/immutable
#menambahkan elemen ke tuple
#logsApps.append("user3 login")
#update elemen ke tuple
#logsApps[0] = "user4 login"
#menghapus elemen ke tuple
logsApps.remove("user2 login")

#pembuktian bahwa tuple tidak bisa diakses dengan index
print(logsApps[0])#akses dengan index ke-0
print(logsApps[-1])#akses dengan index ke-1

#slice dan copy tuple
print(logsApps[0:1])
backup_logsApps: tuple:
print(backup_logsApps)

usr1: str, usr2: str, usr3: str = logsApps
print(usr1)