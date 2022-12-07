#Problema 1: Menu
import os
os.system("cls")
opcion=int(input("Menu de recomendaciones \n"+
                 "1. Literatura \n"+
                 "2. Cine \n"+
                 "3. Musica \n"+
                 "4. Videojuegos \n"+
                 "5. Salir \n"+
                 "Elija un opcion (1-5): "))
while opcion <= 5:
    if opcion==1:
        print(input("Lecturas recomendables: \n"+
                    "+Esperandolo a Tito y otros cuentos de futbol (Eduardo Sacheri) \n"+
                    "+El juego de ender (Orson Scott Card) \n"+
                    "+El sueño de los heroes (Adolfo Bioy Casares) \n"))
    elif opcion==2:
        print(input("Peliculas recomendables: \n"+
                    "+Matriz (1999) \n"+
                    "+El ultimo samurai (2003) \n"+
                    "+Cars (2006) \n"))
    elif opcion==3:
        print(input("Discos recomendables: \n"+
                    "+Despedazado por mil partes (La Renga, 1996) \n"+
                    "+Bufalo (La Mississipi, 2008)"+
                    "+Gaia (Mago de Oz,2003) \n"))
    elif opcion==4:
        print(input("Videojuegos Clasicos recomendables: \n"+
                    "+Dia del tentaculo (LucasArts, 1993) \n"+
                    "+Terminal Velocity (Terminal Reality/3D Realms,1995)"+
                    "+Death Rally (Remedy/Apogee,1996) \n"))
    elif opcion==5:
        print(input("Gracias vuelva pronto"))
    else:
        print(input("Opcion no válida"))
os.system("cls")
opcion=int(input("Menu de recomendaciones \n"+
                 "1. Literatura \n"+
                 "2. Cine \n"+
                 "3. Musica \n"+
                 "4. Videojuegos \n"+
                 "5. Salir \n"+
                 "Elija un opcion (1-5): "))