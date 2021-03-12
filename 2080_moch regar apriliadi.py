suku = input("Masukkan kalimat: ")
kata = ""

for i in suku:
    if i not in kata and i != " ":
        kata += i
        
print(len(kata))