num1=int(input("Ingrese el primer numero (1 de 3)\n"))
num2=int(input("Ingrese el primer numero (2 de 3)\n"))
num3=int(input("Ingrese el primer numero (3 de 3)\n"))

if num1 > num2 and num1 >num3:
    print ("\n El numero mayor de tres es:", num1)
elif num2 > num1 and num2 > num3:
    print ("\n El numero mayor de tres es:", num2)
else:
    print ("\n El numero mayor de los tres es:", num3)