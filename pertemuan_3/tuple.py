import sys
# membuat tuple
logsApps = ("user1 login", "user2 login",)
print(logsApps)
print("memiliki ukuran tuple: ", sys.getsizeof(logsApps))

logsApps_list = ["user1 login", "user2 login",]
print(logsApps_list)
print("memiliki ukuran list: ", sys.getsizeof(logsApps_list))

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
backup_logsApps = logsApps[:]
print(backup_logsApps)

usr1, usr2 = logsApps
print(usr1)
print(usr2)