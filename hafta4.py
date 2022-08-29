#    recap
# # 1. değişkenler
#     # değeri değiştirilemeyen: tuple.
#     # değeri değiştirilebilir: list, float, int, string, set, dictionary...
# # 2. ifadeler
# print(bool(2<3))
# print(bool("sandfjasdf"))
# print(bool("False"))
# print(bool("")) # False
# print(bool(0))
# print(bool(34221))
# print(bool(None)) 
# # 3. karar yapıları
#     # if elif else 
# # 4. döngüler
#     # for, while
# for i in range(10):
#     i = i*10
#     print(i)

# for id, element  in enumerate([22,33,44,55,66]):
#     print(id, element)

# a = 3
# b = 5
# while a<b:
#     print("2<5")
#     a +=10
#     if a>b:
#         break
#     print(a,b)

# # 5. fonksiyonlar
# def get_dimensions():
#     length = int(input("Uzunluk: "))
#     width = int(input("Genişlik: "))
#     return length, width
# def getid():
#     id = None # int
#     return id
# if getid():
#     print(id*5)
# # 6. classlar - object oriented programming - nesneler
#     # class, object, instance, method, attribute

# class ogrenci():
#     def __init__(a, isim, soyisim, numara):
#         a.isim = isim
#         a.soyisim = soyisim
#         a.numara = numara
#     def get_ogrenci(a):
#         return a.isim, a.soyisim, a.numara
# ogrenci1 = ogrenci("ahmet", "yilmaz", "12345")




# Exception handling - hata yakalama
# a = 5
# b = -5
# if b < 0:
#     raise ValueError("b değeri negatif")
# print(a-b)

# import time

# ls = [1,2,3,4,5] # 0,1,2,3,4
# try:
#     #time.sleep(10)
#     print(ls[len(ls)])
# except IndexError as e:
#     print(e)
#     print(ls[len(ls)-1])

# except KeyboardInterrupt as e:
#     print(e)
#     print("Programdan çıkılıyor...")
# except:
#     print("Bilinmeyen hata")
#     exit(1)

# OPENCV
# import cv2


# img = cv2.imread("balls.jpg")
# print(img)
# (h,w,c) = img.shape # channel [b,g,r]
# print(img.shape)
# img_np = np.array(img)
# for i in range(h-1):
#     for j in range(w-1):
#         #if i>h/2 and j>w/2:
#             img_np[i,j,0] = int((img_np[i,j,0] + img_np[i+1,j+1,0])/2)
#             img_np[i,j,1] = int((img_np[i,j,1] + img_np[i+1,j+1,1])/2)
#             img_np[i,j,2] = int((img_np[i,j,2] + img_np[i+1,j+1,2])/2)

# cv2.imshow("image",img_np)
# cv2.waitKey(0)
# cv2.imshow("kopek", img[:int(h/2),:int(w/2)])
# cv2.waitKey(0)
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("kopek", img2)
# cv2.waitKey(0)
# cv2.rectangle(img, (0,0), (w,h), (0,0,255), -1)

# img_inverted = cv2.bitwise_not(img)
# #img_inverted = 255 - img
# cv2.imshow("image",img_inverted)
# cv2.waitKey(0)

# img_blur = cv2.blur(img, (500,1))
# cv2.imshow("image",img_blur)
# cv2.waitKey(0)






