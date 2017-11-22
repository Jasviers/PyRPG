# PyRPG

## Introducción
- Escribe tu nick de github en el pad.
- Clona el repositorio.
- Se debe crear una rama en este repositorio (branch <Nick>).
- Crear carpeta src y en ella un fichero vacio \__init\__.py.
- Crear ficheros criatura.py, guerrero.py, monstruo.py* y juego.py.
- Implementa al menos lo que se pide.
- Amplia todo lo que quieras tu juego.


# A implementar

## Clase Criatura
### Atributos
- Vida(HP)-Int
- Ataque(ATK)-Int
- Defensa(DEF)-Int

### Metodos
- Atacar(Criatura_Atacada): Realiza daño a la criatura atacada
- Atacado(ATK): Recibe daño (HP -= criatura.ATK - DEF)
- MostrarVida(): Muestra por pantalla la vida que tiene y la total

## Clase Guerrero
- Hereda de la clase Criaturas.
### Atributos
- Heredados.
- Furia.-Int(0-100)
- Nombre.-String

### Metodos
- Heredados.
- AtaqueEspecial(Criatura_Atacada): Gasta furia, debe comprobar que hay furia para hacerlo si no ataca de forma normal; hace un ataque con un 1.5 de daño.

## Clase Monstruo*
- Hereda de la clase Criaturas.
### Atributos
- Los heredados.
- Nombre-String

### Metodos
- Los heredados.

## Juego
- Crear a tu personaje y a los monstruos.
- Crear menu de juego: muestra tu nombre y atributos en una linea y luego un menu con las opciones:
  - 1.-Atacar.
  - 2.-Ataque Especial.
  - 3.-Rendirse.
- Se pide selecionar una de las opciones.
- Se realiza tu turno y luego el del enemigo.
- Tiene que repetirse hasta que tu vida o la del enemigo llegue o baje de cero.


# Añadidos interesantes
- Sistema de experiencia y niveles.
- Creador de personaje.
- Mas monstruos y clases de personaje.
- Generador de monstruos aleatorios para los combates.

*El monstruo que mas os apetezca
