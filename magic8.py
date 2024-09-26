import random
pregunta= input("Bienvenido a magic ball, realiza una pregunta: ")


num = random.randint(1, 9)

if num == 1:
    print("Si definitivamente")
elif num ==2:
    print("Es decididamente así.")
elif num == 3:
    print("Sin duda")
elif num == 4:
    print("Responde confusamente, inténtalo de nuevo. ")
elif num == 5:
    print("Pregunta nuevamente más tarde")
elif num == 6:
    print("Mejor no te lo digo ahora")
elif num ==7:
    print("Mis fuentes dicen que no")
elif num == 8:
    print("Perspectiva no tan buena")
elif num == 9:
    print("Muy dudosa")
