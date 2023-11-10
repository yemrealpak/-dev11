import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("şifre uzunluğunu giriniz?"))

sifre = ""

for i in range(uzunluk):
    sifre = sifre + random.choice(karakterler)


print(sifre)
