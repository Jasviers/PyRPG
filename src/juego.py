from monstruo import *
from guererro import *
from criatura import *
from ladron   import *
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("1-> Guerrero. (Tienes un ataque mejor)")
print("2-> Ladron. (Puedes robar)")
print("")
clase = int(input("Elige tu clase:....."))

if clase == 1:
    guerrero = Guerrero(5,5,2,3,30,0,0,"Alumno")
    ataque_especial = "Ataque Poderoso"
elif clase == 2:
    guerrero = Ladron(3,3,3,20,0,0,0,"Alumno")
    ataque_especial = "Robar"

monstruo = Monstruo(3,3,4,3,"Emilio Torredano")
os.system('cls' if os.name == 'nt' else 'clear')


while (monstruo.hp > 0 or guerrero.hp > 0):
    print("")
    print("Nombre = {}   Nivel = {}    Vida = {}    Furia = {}".format(guerrero.nombre, guerrero.nivel, guerrero.hp, guerrero.fu))
    print("")
    print("1-> Ataque Normal")
    print("2-> {}".format(ataque_especial))
    print("3-> Curarse")
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


if (guerrero.hp <= 0):
    print("")
    print("--NO TIENES NI PUTA IDEA (pero eso ya lo sabias ¯\_(ツ)_/¯ )--")
    print("")

elif (monstruo.hp <= 0):
    print("")
    print("--HAS APROBADO CALCULO--")
    print("")
