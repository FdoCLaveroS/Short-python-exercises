llueve = False
temperatura =int(input("Ingresa temp°"))
if temperatura <18:
    if llueve == True:
        print ("Llevare paraguas y abrigo")
    else: 
        print ("Solo llevaré abrigo")
else:
    print ("No necesito ni paraguas ni abrigo")
