
print("Pemeriksa Kelipatan 9")
a = int(input("Masukan Kelipatan 9 yang ingin diperiksa: "))
def kelipatan_sembilan(a):
    h = (a/9)
    return h
if kelipatan_sembilan(a) == 9:
    print("Benar")
else:
    print("Salah")
