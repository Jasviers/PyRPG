from monstruo import *
from guererro import *
from criatura import *


Guerrero_Generico = Guerrero(5,5,3,3,50,0,0,"Alumno")
Monstruo_Generico = Monstruo(3,3,4,3,"Joaqin Erviti")
Guerrero_Generico.mostrarVida()
Monstruo_Generico.mostrarVida()

while(Guerrero_Generico.HP > 0 or Monstruo_Generico.HP > 0):
    print("Nombre= {} Nivel= {} Vida = {} Furia= {}".format(Guerrero_Generico.Nombre, Guerrero_Generico.nivel, Guerrero_Generico.HP, Guerrero_Generico.FU))
    print("1-> Ataque Normal")
    print("2-> Ataque Especial")
    print("3-> Huir")
    eleccion = input("Realiza tu elección")
    if eleccion == 1:
        Guerrero_Generico.atacar(Monstruo_Generico)
        Guerrero_Generico.ganarFuria()
        Guerrero_Generico.mostrarVida()
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Monstruo_Generico.mostrarVida()
    elif eleccion == 2:
        Guerrero_Generico.ataqueEspecial(Monstruo_Generico)
        Guerrero_Generico.ganarFuria()
        Guerrero_Generico.mostrarVida()
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Monstruo_Generico.mostrarVida()
    else:
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Guerrero_Generico.mostrarVida()
        print("¡Has huido con exito! ")
