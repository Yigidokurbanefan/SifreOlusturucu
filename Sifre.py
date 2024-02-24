import random
olustur = ""
k = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = "1234567890"
z = "+-/*!&$#?=@"
uzunluk = int(input("Parolanin uzunlugu ne kadar olsun(Sayi girin)"))
for i in range(uzunluk):
    if i % 3 == 0:
        olustur+= random.choice(k)
    elif i % 3 == 1:
        olustur+= random.choice(s)
    elif i % 3 == 2:
        olustur += random.choice(z)
        

print(olustur)
