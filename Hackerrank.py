# Kullanıcıdan girilen bir yıl Artık Yıl olup olmadığını bilmek için, geliştirdiğim kod:
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year %4==0:
        if year %100==0:
            if year %400==0:
                leap = True
            else:
                return leap
        else:
            leap=True
    else:
        return leap
    return leap
year = int(input())
print(is_leap(year))

# kullanıcıdan girilen sayıyı 1’den o sayıya kadar sayılar yazılması
if __name__ == '__main__':
    n = int(input())

# for i in range(1,n+1):
#     print(i,end='')

i=1
while i<=n:
    print(i,end='')
    i+=1
