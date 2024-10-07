# 1.Kullanıcı gireceği doğum yılından şuanki yaşını bilme : (bunun için datetime kütühanesini çağırdım)
name = input("What Is Your Name? ")
birth_year = input("What is your birth year? ")

# Parameter tipi dönüştürme ##
age = datetime.now().year - int(birth_year)
print(age)

# 2.String üzerine birkaç operatör kullanma
course = "Python for Beginners"
print(course.upper()) #orjinal string'i değiştirmez
print(course.find('t')) #verdiğimiz string'de t harfine arar, eğer bulmazsa -1 verir
print(course.replace('for','4')) #bu da orjınal string'i değiştirmez
print('for' in course) # 'for' kelinesi course string'inde varmı yokmu diye in operatörü ile bilebiliriz

# 3.	Girilen ağırlığı LBS biriminden KG birimine ve tersi. (python dili küçük veya büyük harfa uyarılı olduğu için ve bundan dolayı kodun aksamasını önlemek için girilen harf ne olursa olsun büyük harfa çevirilip öylece derlemek.
weight = int(input("Your weight: "))
letter = input("Please write the letter which your enterd the weight with, is it in (K)kg Or in (L)bs ? ")
if letter.upper() == "L" :
    weight /= 2.20
    print("You weight with (K)kg is: " + str(weight))
elif letter.upper() == "K" :
    weight *= 2.20
    print("You weight with (L)bs is: " + str(weight))
else :
    print("Wrong typing !. Please try again.")
