
# sadece rakamları arttırarak sayıyı bulan program ------

# gercek_sifre = input("Gerçek Şifre: ")
# tahmin_sifresi = 0
# while not gercek_sifre == str(tahmin_sifresi):
#     print(tahmin_sifresi)
#     tahmin_sifresi += 1
# print("tebrikler, şifreniz doğru",tahmin_sifresi)

# 3242442 % 10 =  2
# 3242442 // 10 = 32424
# 324244 % 10 = 4


# # tüm karakterler için sifre bulucu program ----------
# karakterler = [0,1,2,3,4,5,6,7,8,9,
# "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
# "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 

# def sifre_bulucu_fonc(deger): # 123 (10luk) = 1Z (62 lik)
#     basamak_Sayisi = 1
#     tahmin_edilen_sifre = ""
#     while not deger <= len(karakterler)**basamak_Sayisi:
#         basamak_Sayisi += 1
    
#     for i in range(1,basamak_Sayisi):
#         basamak_degeri = karakterler[deger % len(karakterler)]
#         tahmin_edilen_sifre = str(basamak_degeri) + tahmin_edilen_sifre
#         deger = deger // len(karakterler)
#     return tahmin_edilen_sifre

# gercek_sifre = input("Gerçek Şifre: ")
# sifre_degeri = 0
# sifrenin_uzunlugu = 1
# tahmin_sifresi = 0
# while gercek_sifre != tahmin_sifresi:
#     sifre_degeri += 1
#     tahmin_sifresi = sifre_bulucu_fonc(sifre_degeri)
#     print(tahmin_sifresi)

# print("tebrikler, şifreniz doğru",tahmin_sifresi)





# pi sayisi bulma ----------------------
# import random

# ceyrek_cemberde = 0
# ceyrek_cember_disinda = 0
# for i in range(1,100000):
#     p = (random.random(), random.random())
#     lenght_p = (p[0]**2 + p[1]**2)**0.5
#     if lenght_p < 1.0:
#         ceyrek_cemberde += 1
#     else:
#         ceyrek_cember_disinda += 1
    
# pi_ = 4 * ceyrek_cemberde / (ceyrek_cemberde + ceyrek_cember_disinda)
# print(pi_)



# CLASS LAR --------------------------------------------------------------

# # float, int, str, bool, list, tuple, dict, set

# class ogrenci_():
#     pass

# ogrenci1 = ogrenci_()

# ogrenci1.id = 100000
# ogrenci1.isim = "Ahmet"
# ogrenci1.soyisim = "Kaya"
# ogrenci1.yas = 20
# ogrenci1.kilo = 60

# print(ogrenci1.id)
# print(ogrenci1.isim)
# print(ogrenci1.soyisim)
# print(ogrenci1.yas)
# print(ogrenci1.kilo)





# class ogrenci():
#     def __init__(a, isim, soyisim, numara, bolum, notlar):
#         a.isim = isim
#         a.soyisim = soyisim
#         a.numara = numara
#         a.bolum = bolum
#         a.notlar = notlar
#         #self.ortalama = self.ortalama_hesapla()
    
# ogrenci1 = ogrenci("Ahmet", "Kaya", 100000, "Bilgisayar", [10,20,30,40,50])
# print(ogrenci1.isim)




# class ogrenci():
#     def set_name(self,isim):
#         if type(isim) == str:
#             self.isim = isim
#         else:
#             print("Lütfen isim giriniz")
#     def get_name(self):
#         return self.isim

# ogrenci1 = ogrenci()
# ogrenci1.set_name("kaya")
# print(ogrenci1.get_name())




# class rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         return self.width * self.height
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#     def get_diagonal(self):
#         return (self.width ** 2 + self.height ** 2) ** 0.5

# r1 = rectangle(height=3,width=2)
# print(r1.get_area())
# print(r1.get_diagonal())




# class rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_area(self,width=None,height=None):
#         if not( width == None and height == None):
#             return width * height
#         else:
#             self.area = self.width * self.height
#             return self.area
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)
#     def get_diagonal(self):
#         return (self.width ** 2 + self.height ** 2) ** 0.5

# rectangle_ = rectangle(height=3,width=2)
# area_2_5 = rectangle_.get_area(2,5)
# print(rectangle_.get_area())
# print(rectangle_.area)


# # modül(kütüphane) ekleme --------

# # seçenek 1
# import dortgen
# r1 = dortgen.rectangle(height=3,width=2)


# # seçenek 2
# from dortgen import rectangle
# r1 = rectangle(height=3,width=2)


# # seçenek 3
# from dortgen import rectangle as rt
# r1 = rt(height=3,width=2)

# # seçenek 4
# from dortgen import *
# r1 = rectangle(height=3,width=2)

# from dortgen import print_ as print
# print("dfs",end="\n") #\t \r



# # Inheritence -------------
# from hayvan import hayvan,kopek,karga

# kopek1 = kopek(12)
# print(kopek1.yas)
# print(kopek1.ucabiliyormu)
# print(kopek1.cins)

# karga1 = karga("kuzgun",5)
# print(karga1.yas)
# print(karga1.ucabiliyormu)
# print(karga1.cins)

# hayvan1 = hayvan("kuzgun",5,True)
# print(hayvan1.yas)
# print(hayvan1.ucabiliyormu)
# print(hayvan1.cins)

