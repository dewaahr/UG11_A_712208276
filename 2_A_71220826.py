def cetakHuruf(str):
    jumlah=len(str)
    if jumlah % 2==0:
        return str[0]+str[1]+str[2]+"dan"+str[-3]+str[-2]+str[-1]
    else:
        tengah=int(jumlah/2)
        return str[tengah-1]+str[tengah]+str[tengah+1]
kata=input("Masukan Kata:")
cetak=cetakHuruf(kata)
print("Huruf yang diambil pada kata",kata,"adalah",cetak)
