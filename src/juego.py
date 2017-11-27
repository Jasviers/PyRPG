from monstruo import *
from guererro import *
from criatura import *


guerrero = Guerrero(5,5,3,3,50,0,0,"Alumno")
Monstruo_Generico = Monstruo(3,3,4,3,"Joaquín Erviti")
print("Nombre= {} Nivel= {} Vida = {} Furia= {}".format(guerrero.nombre, guerrero.nivel, guerrero.hp, guerrero.fu))
Monstruo_Generico.mostrarVida()

while(guerrero.hp > 0 or guerrero.hp > 0):
    print("Nombre= {} Nivel= {} Vida = {} Furia= {}".format(guerrero.nombre, guerrero.nivel, guerrero.hp, guerrero.fu))
    print("1-> Ataque Normal")
    print("2-> Ataque Especial")
    print("3-> Huir")
    eleccion = input("Realiza tu elección")
    if eleccion == 1:
        guerrero.atacar(Monstruo_Generico)
        guerrero.ganarFuria()
        guerrero.atacado(Monstruo_Generico.atk)
    elif eleccion == 2:
        guerrero.ataqueEspecial(Monstruo_Generico)
        guerrero.ganarFuria()
        guerrero.atacado(Monstruo_Generico.atk)

    else:
        guerrero.atacado(Monstruo_Generico.atk)
        guerrero.mostrarVida()
        print("¡Has huido con exito! ")

print("Enemigo derrotado.")
