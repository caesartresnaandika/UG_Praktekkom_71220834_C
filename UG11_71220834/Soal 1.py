
#output
print("=========================")
print("Operasi Matematika")
print("1. Jumlah          [+]")
print("2. Kurang          [-]")
print("3. Kali            [*]")
print("4. Bagi            [/]")
print("=========================")
n = int(input("Pilih operasi (1/2/3/4): "))
#rumus2
def penjumlahan(a,b):
    t = (a+b)
    return t
def pengurangan(a,b):
    k = (a-b)
    return k
def perkalian(a,b):
    ka = (a*b)
    return ka
def pembagian(a,b):
    ba = (a/b)
    return ba
#Rumus
if n == 1:
    a = int(input("Masukan Bilangan pertama: " ))
    b = int(input("Masukan Bilangan Kedua: "))
    print("Hasil operasi dari", a ,"+", b , "=" , penjumlahan(a,b))
elif n == 2:
    a = int(input("Masukan Bilangan pertama: " ))
    b = int(input("Masukan Bilangan Kedua: "))
    print("Hasil operasi dari", a ,"-", b , "=" , pengurangan(a,b))
elif n == 3:
    a = int(input("Masukan Bilangan pertama: " ))
    b = int(input("Masukan Bilangan Kedua: "))
    print("Hasil operasi dari", a ,"*", b , "=" , perkalian(a,b))
elif n == 4:
    a = int(input("Masukan Bilangan pertama: " ))
    b = int(input("Masukan Bilangan Kedua: "))
    print("Hasil operasi dari", a ,"/", b , "=" , pembagian(a,b))

    
    
    
    


