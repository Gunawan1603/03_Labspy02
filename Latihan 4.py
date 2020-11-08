#Tugas Praktikum 2, input tiga buah bilangan, dari ketiga bilangan, tampilkan bilangan terbesarnya. Gunakan statement if
print()
a = int(input("Masukkan bilangan A= "))
b = int(input("Masukkan bilangan B= "))
c = int(input("Masukkan bilangan C= "))

if ((a>b) & (a>c)):
    print("bilangan terbesarnya A = ", a )
if ((b>c) & (b>a)):
    print("bilangan terbesarnya  B = ", b)
if ((c>a) & (c>b)):
    print("Bilangan terbesarnya C = ", c)
    print ("<<< Selesai >>>")    
