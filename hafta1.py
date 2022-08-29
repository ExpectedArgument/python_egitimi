# aşağıdaki kod blokları ayrı ayrı yorum dışı bırakılarak çalıştırılabilir.
# Hepsini aynı anda yorum dışın a bırakmayın.
# VSCode ta yorum dışı bırakma komutu: Ctrl ye basılı tutup K ve U ye tıklayın.
# VSCode ta yorum içe alma komutu: Ctrl ye basılı tutup K ve C ye tıklayın.

# # INTRO: ---------------------------------------------------------------
# st = "merhaba" # st adında bir string tanımlandı
# print(st) # st değeri bastırıldı

# print(""" # 3 tırnak enter işlemini kabul eder
# frg
# rw
# gre""")

# print ("fnwfnwlf\\\  # string içerininde \ karakteri kullanmak için \\ yazılır.
# fewfw\   # \ karakteri bir sonraki karakteri iptal eder. burada enter işlemi yapılmıyor.
# fwf")

# x = input("bir sayı giriniz.")
# print(x)
# y = input("başka bir sayı giriniz.")
# print(y)
# sonuc = int(float(x)*float(y))
# print("2 sayının çarpımı:",sonuc,".")
# print("2 sayının çarpımı:" + str(sonuc)+".")
# print(f"2 sayının çarpımı:{sonuc}.")


# print("x"*5)
# print("4+5")
# print(4+5)
# print(int(float(4+5)))
# nb1 = int(4+5)
# # nb = int("4+5") # hata verir çünkü "4+5" bir sayı değil
# # print("nb",nb)
# print("nb1",nb1)

# sayi1 = input("bir tam sayı giriniz:")
# uzunluk = len(sayi1)
# sayi2 = 1348741
# uzunluk2 = len(str(sayi2))
# print(f"sayınız {uzunluk} basamaklıdır.")
# print(f"{sayi2}, {uzunluk2} basamaklıdır.")

# z = 4.55 + 5
# print(z)
# print("z değişkeni tipi:",type(z))
# print("z değişkeni tipi:",type(str(z)))
# print(round(z,1))

# # OPERATORS: + - * / % ** // -------------------
# print(3+3)
# print(3-3)
# print(3*3)
# print(3/2)
# print(3%-2)
# print(3**3)
# print(3//2)
# x = 2**(2*5/2) + 2 % 3/5
# print(x)

# ---- ifadeler ---
# x = 4
# z = x < 5  # x 5 ten küçükse True, değilse False
# print(type(z))
# print(int(False))
# print(int(True))
# print(int(z)*10)
# print( 5 <= 6)
# print( 5 != 5)
# int, str, float, bool

# # LIST ---------
# aw = [] # boş liste
# sq = [1] # tek elemanlı liste
# print(type(aw))
# print(type(sq))

# ys = list((2,3,4,5<6,2>3)) #ys ile fs aynı şeydir
# print(xs)
# fs = [2,3,4,5<6,2>3]
# print(fs)

# xs = [2,3,4,5<6,2>3, 5+6, "fre"+ "fre", "x"*10,6, "cdsnjks", 
# 3.2, [23, "fwfw", 32.0 , .5, 1. ]] # 1. (1.0), .5 (0.5)
# print(xs)
# print(type(xs))
# print(xs[0])
# print(xs[11][1])
# print(len(xs))
# print(xs[7])
# print(len(xs[11]))
# print(xs[11][-1])
# print(xs[11][-2])

# st = input("bir string giriniz:")
# print(st[1:-3])   # 3 basamaktan küçükse hata verir

# zs = [2,3,4,5,6,7,8,9,10]
# zs.append(11)
# print(zs)
# zs.remove(2)
# print(zs)
# zs.clear()
# print(zs)

# TUPLE -------
# xs = (2,3,4,5,6,7,8,9,10) # tuple tanımlandığı gibi kalır ve değiştirilemez
# print(xs)
# print(type(xs))
# print(xs[0])
# print(xs[-1])
# print(xs[2:-2])

# zs = (2) # bu bir tuple değildir.
# cs = (2,) # tek elemanlı tuple tanımlaması - virgül kullanılır.
# ws = () # elemansız tuple tanımlaması.
# print(type(zs))
# print(type(cs))
# print(type(ws))


# # DICTIONARY ------
# dict = {"isim":"muvahhid","soyisim":"kılıç"} # key(string):value
# print(dict)
# print(dict["isim"])
# # print(dict["id"]) # hata verir id yok çünkü
# dict["id"] = 1213
# print(dict)
# dict.pop("id") # id key'ini ve değerini siler
# print(dict)

# # SET ------
# x = {2,3,4,5,6,7,8,9,10}
# y = {6,7,8,9,10,11}
# print(x & y) # ortak kesişimi verir
# print(x | y) # x ve y'nin birleşimini verir
# print(x - y) # x'ten y'yi çıkartır (olmayan elemanlar etkisizdir)
# print(x ^ y) # x ve y'den farkını verir
# print(x > y) # x'in y'yi kapsar mı
# print(x < y) # x'in y'nin alt kümesi mi
# print(x == y) # x ve y eşit mi
# print(x != y) # x ve y eşit değil mi
# print(x >= y) # x ve yi kapsar veya eşit mi
# print(x <= y) # x ve y'nin alt kümesi veya eşit mi
# print(x is y) # x ve y eşit mi (x ve y aynı nesne mi)
# print(5 in y) # 5 y de var mı

