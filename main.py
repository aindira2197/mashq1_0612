#if_else
docs = input('Hujjat topwirilganmi:  ').lower()
interview = input("Suhbatdan o'tdimi: ").lower()
test = input("testdan o'tdimi: ").lower()

if docs == "ha":
    if interview == "ha":
        if test == "ha":
            print("Siz ishga qabul qilindingiz.")
        else:
            print("Test natijalari yetarli emas.")
    else:
        print("Suhbatdan o'tmagansiz.")
else:
    print("Avvalo hujjat topwiring.")

#for
text = input("Matn kiriting: ").split(" ")
print(text)
new = ""

for i in text:
    new += i[0]

print(new)

#list
roy = [4, 7, 2, 5, 1, 10]
new = []

for i in roy:
    new.append(roy.index(i)*i)

print(new)
