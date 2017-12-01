from monstruo import *
from guererro import *
from criatura import *
import os


guerrero = Guerrero(5,5,3,3,30,0,0,"Alumno")
monstruo = Monstruo(3,3,4,3,"Joaquin Erviti")

while (monstruo.hp > 0 or guerrero.hp > 0):
    print("")
    print("Nombre = {}   Nivel = {}    Vida = {}    Furia = {}".format(guerrero.nombre, guerrero.nivel, guerrero.hp, guerrero.fu))
    print("")
    print("1-> Ataque Normal")
    print("2-> Ataque Especial")
    print("3-> Huir y curarse")
    print("")
    eleccion = int(input("Realiza tu elección:....    "))
    if eleccion == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        guerrero.atacar(monstruo)
        monstruo.mostrarVida()
        monstruo.atacar(guerrero)
        guerrero.ganarFuria()
        guerrero.ganarExperiencia()
        guerrero.ganarNiveles()

    elif eleccion == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        guerrero.ataqueEspecial(monstruo)
        monstruo.mostrarVida()
        monstruo.atacar(guerrero)
        guerrero.ganarFuria()
        guerrero.ganarExperiencia()
        guerrero.ganarNiveles()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        guerrero.hp += 1
        print ("Te has curado 1 punto de vida")
        monstruo.atacar(guerrero)
        guerrero.mostrarVida()
        print("¡Has huido con exito!")

if (guerrero.hp <= 0):
    print("")
    print("--ALUMNO HA MUERTO. IGNORANTE--")
    print("")

elif (monstruo.hp <= 0):
    print("")
    print("--ERVITI HA MUERTO--")
    print("")
