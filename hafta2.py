# list, tuple, set, dictionary
# xs = ([],[2,4])
# print(xs)
# xs[1][0] = [3,6]
# print(xs)

# Karar ifadeleri -------------
# asilsifre = "1234"
# sifre = input("sifre giriniz.")

# if asilsifre == sifre:
#     print("sifreyi dogru girdiniz.")
#     print("aferin")
#     print("sen sifreni değiştir isteersen")
# else:
#     print("sifreyi yanlış girdiniz.")

# print("if dışı")

# ogrenci_notu = 30

# if 40 > ogrenci_notu:
#     print("başarısız")
# else:
#     print("dersi geçer")

# if 50 > ogrenci_notu:
#     print("sartlı gecer")
# elif 60 > ogrenci_notu:
#     print("az daha çalış")
# else:
#     print("başarılı")

# Döngüler ---------
# print(1)
# print(2)
# print(3)
# print(4)
# s = 5
# while s < 100:
#     #s += 1 # s=s+1
#     print(s)


# is: ==

# ds = [1,2,3,4,5,6]
# for x in ds:
#     if x == 1 or x == 3 or x == 5:
#         print(x)

# dc = [1,2,3,4,5,6]
# for c in dc:
#     continue
#     if c == 4:
#         print(c, "nin içinde", 4, "var" )
#         # break
# print(c)

# dc = [1,2,3,4,5,6]
# for c in dc:
#     if c == 4:
#         print(c, "nin içinde", 4, "var" )
    
#     elif type(c) == int:
#         print(c*4)

# x = 1
# for i in range(x+1): # 1,2,3,.....x
#     if x == 1:
#         print("asal sayı değil")
#         break
#     if i == 1 or i == 0:
#         continue
#     if x == i:
#         print("asal sayıdır")
#         break
#     if x % i == 0:
#         print("asal sayı değildir")
#         break
    
# x = 5
# sonuc = 1
# for i in range(1,x+1):
#     if i <= x:
#         sonuc = sonuc * i
# print(sonuc)

# FONKSİYONLAR -----------

# def asalbulucu(x):
#     for i in range(x+1): # 1,2,3,.....x
#         if x == 1:
#             print(x,"asal sayı değil")
#             break
#         if i == 1 or i == 0:
#             continue
#         if x == i:
#             print(x,"asal sayıdır")
#             break
#         if x % i == 0:
#             print(x,"asal sayı değildir")
#             break
# x = 10
# asalbulucu(x)
# print(x)

# def carpmaislemi(x,y):
#     sonuc = x*y
#     #return sonuc
# s = carpmaislemi(4,5)
# print(s)

# def asalbulucu(x):
#     for i in range(x+1): # 1,2,3,.....x
#         if x == 1:
#             print(x,"asal sayı değil")
#             return False
#         if i == 1 or i == 0:
#             continue 
#         if x == i:
#             print(x,"asal sayıdır")
#             return True
#         if x % i == 0:
#             print(x,"asal sayı değildir")
#             return False
# x = 10
# if asalbulucu(x):
#     print("ASALDIR")
# else:
#     print("ASAL DEĞİLDİR")

