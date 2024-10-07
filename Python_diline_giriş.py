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



### öğrenirken yazdığım değer kodlar
# from _datetime import datetime
# from ctypes import memset
#
# age = 20
# age = 30
# Bol = True ## Sum to type of number ##
# first = float(input("First Number: "))
# second = float(input("Seconde Number: "))
# sum = first + second
# 
# # Arithmetic Operators ##
# print(10 / 3) #result as float
# print(10 // 3) #result as int
# print(10 % 3) #result as reminder of 10 by 3
# print(10 ** 3) #1000
# x = 10
# x += 3 ## += , -= , *=
# print(x)
#
# # Comparison Operators ##
# x = 3 > 2 #the result type is boolean , 3 == 2 , 3 >= 2 , etc.
# print(x)
#
# # Logical Operators ##
# price = 25
# print(price > 10 and price < 30) # or , not , and ,
# print(not price < 5)
#
# # If Statment ##
# temperature = 35
# if  temperature > 30 :
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20 :
#     print("It's a nice day")
# else :
#     print(" :( ")
# print("I am not in if statment :)")
# While Loops ##
# i = 1
# while i <= 1_000 : #we can write underscore '_' if we wish
# while i <= 10 :
#     print(i * '*') # so we can multiple int with str but we can't add them
#     i += 1
#
# # Lists ##
# names = ['hosam','ahmet','fatih','kamel']
# print(names)
# print(names[2])
# print(names[-2]) #second form the last , this features it isn't available in other languages
# names[0]='hosam aldeen'
# print(names)
# print(names[0:3]) # contain the first but exclude the end
#
# # List Methods ##
# numbers = [1,2,3,4,5]
# numbers.append(6) # add item in the last of list
# numbers.insert(3,3.5) # add an item in the index you want
# numbers.remove(3) #remove 3 number
# numbers.clear() #remove all the items in the list
# print(len(numbers)) #to know how many item we have in the list
# print(numbers)
#
# # For Loops ##
# numbers = [1,2,3,4,5]
# for number in numbers:
#     print(number)
#
# # Rang Function() ##
# for number in range(5,10,2): #contain first,exclude the seconde and jump as the last
#     print(number)
#
# # Tuples ##
# We can't do any changing on tuples after we created
# numbers = (1,2,3,3)
# numbers.count(3) # how many times repeated
# print(numbers)
