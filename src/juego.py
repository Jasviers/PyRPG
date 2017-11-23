from criatura import *
from principeMutante import *
from guerrero import *
import os

guerrero = Guerrero(2,2,5, nombre="Andres \"El Mini Sanchez\"")
guerrero.mostrarVida()
luis = PrincipeMutante(5,1,2, nombre="Luis")
luis.mostrarVida()


while guerrero.hp > 0 and luis.hp > 0:

    print("Tu guerrero {} tiene {}HP y {}Furia".format(guerrero.nombre, guerrero.hp, guerrero.furia))
    print("Menu, indica el número de opción:")
    print("1.- Ataque")
    print("2.- Ataque especial")
    opcion = int(input("Elige opción:\n"))
    os.system("clear")
    if opcion==1:
        guerrero.atacar(luis)
        if luis.hp >0:
            luis.atacar(guerrero)
    else:
        guerrero.ataque_especial(luis)
        if luis.hp >0:
            luis.atacar(guerrero)
    if guerrero.hp <= 0:
        print("{} murio".format(guerrero.nombre))
    if luis.hp <= 0:
        print("{} murio".format(luis.nombre))
    print("-------------------------------------------------------------------")
