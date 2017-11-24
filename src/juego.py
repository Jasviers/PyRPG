from monstruo import *
from guererro import *
from criatura import *

Guerrero_Generico = Guerrero(5,3,3,50,input("¿Como te llamas? "))
Guerrero_Generico.mostrarVida()
Monstruo_Generico = Monstruo(3,4,3,input("¿Contra que te enfrentas?"))
Monstruo_Generico.mostrarVida()

while(Guerrero_Generico.HP > 0 | Monstruo_Generico.HP > 0):
    print(Guerrero_Generico.Nombre & Guerrero_Generico.FU & Guerrero_Generico.HP)
    print("Que haras a continuacion? 1-> Ataque Normal 2-> Ataque Especial 3-> Huir")
    if (input() == 1):
        Guerrero_Generico.atacar(Monstruo_Generico)
        Guerrero_Generico.ganarFuria()
        Guerrero_Generico.mostrarVida()
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Monstruo_Generico.mostrarVida()
    elif (input() == 2):
        Guerrero_Generico.ataqueEspecial(Monstruo_Generico)
        Guerrero_Generico.ganarFuria()
        Guerrero_Generico.mostrarVida()
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Monstruo_Generico.mostrarVida()
    else:
        Guerrero_Generico.atacado(Monstruo_Generico.ATK)
        Guerrero_Generico.mostrarVida()
        print("¡Has huido con exito! ")
