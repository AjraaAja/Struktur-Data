# Membuat Struktur Data Dictionary
userLogin = {"name": "Budi", "age": 30, "Role":"Admin"}
print(type (userLogin))

# Mengakses Data
print (f"Nama Akun: {userLogin['name']}")
print (f"Umur Akun: {userLogin['age']} Tahun")
print (f"Role Akun: {userLogin['Role']}")

#Akses data seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

#Menambah Data kedalam dictionary big-0 0(1)
userLogin ["email"] = "example@mail.com"
print (userLogin)

# menghapus data big-0 0(1)
userLogin.pop("email")
print (userLogin)

# Mengubah data kedalam dictionary big-0 0(1)
userLogin ["Role"] = "User"
print(userLogin)

# Nested Dictionary
dbuser= {"user1": {"name": "Andi", "age":30, "Role":"Admin"},
"user2": {"name": "Budi", "age": 25, "Role":"User"},
"user3": {"name": "Candra", "age":28, "Role":"Guest"}}
print(dbuser)

# Akses value base key
print(dbuser["user1"])

# Melakukan Pencarian data di Dictionary Big-0 0(1)
findword = input("Masukkan Kata yang ingin dicari: ")
if findword in dbuser:
    print(f"{findword} ditemukan")
    print(dbuser[findword])
else:    
    print(f"{findword} tidak ditemukan")