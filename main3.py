llueve = True
temperatura =int(input("Ingresa temp°"))
if temperatura <18 and llueve == True:
    print ("Llevare paraguas y abrigo")
elif temperatura <18 and llueve ==False:
    print ("Solo llevare abrigo")
else:
    print("No llevare paraguas ni abrigo")

