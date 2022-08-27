
Monedas = 100
Buenas_acciones = 100

print("Había una vez un caballero medieval genérico, que como todo caballero medieval genérico debía rescatar\n"
      "a la princesa que estaba encerrada en la cima de una torre custodiada por varios dragones.\n")

print("Antes de partir a su misión el rey le dió una espada, un ungüento mágico que puede curar cualquier herida \n"
      "y 100 monedas para su viaje.\n")

print("Así que el caballero salió a su aventura...\n")

print("Cuando el caballero entro al bosque se encontró con un vendedor que le ofrecia una espada mas grande\n"
      "por el precio de 50 monedas...\n")

Pregunta_espada = input("¿Aceptas la oferta?\n")
if Pregunta_espada == ("si"):
      Monedas = Monedas - 50
      print("Cantidad de monedas:", Monedas)
      print("Y una espada nueva")

elif Pregunta_espada == ("no"):
      print("se va")


