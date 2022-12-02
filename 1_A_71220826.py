def ubahKata(ori, oriWord ,pengganti):
    return ori.replace(oriWord,pengganti)
def hitungKata(ori, word):
    return ori.count(word)
print("====== Program Manipulasi String ======")
print("1. Hitung kata")
print("2. Ubah Kata")
pilihan=int(input("Masukan Pilihan Anda:"))
ori=input("Masukan sebuah Kalimat atau Kata:")
if pilihan in (1,2,3,4,5,6,7,8,9,0):
    if pilihan==2:
        oriWord=input("Masukan kata yang ingin diubah:")
        pengganti=input("Masukan Kata Pengganti:")
        print("String Berhasil diubah menjadi :",ubahKata(ori, oriWord ,pengganti))
    elif pilihan == 1:
        word=input("Masukan Kata yang ingin dihitung:")
        print("Terdapat sebanyak",hitungKata(ori, word))
    else: print("Pilihan yang anda input tidak terdaftar di daftar pilihan")