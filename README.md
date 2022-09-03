# proyectoT1028

Introducción


Una novela visual (en inglés visual novel), es un género de videojuego interactivo originario de 

Japón y que está particularmente centrado en una historia o que contiene en sus escritos una 

narración similar a la de una novela; se caracteriza principalmente por la presencia de historias 

complejas, la existencia de escenarios y personajes estáticos, aunque en la actualidad algunas 

novelas visuales tienden a incluir una pequeña animación, pequeñas escenas de vídeo e incluso puede 

presentar efectos de sonido y actuación de voz para cada personaje− y la posibilidad de finales 

alternativos.

Las novelas visuales se diferencian de otros tipos de juegos ya que tienden a enfocarse más hacia la 

trama y a la caracterización, en lugar de centrarse en las escenas de acción y ficción interactiva.

Y ese va a ser mi proyecto, una novela visual. En este primer avance escribiré el pseudo código de 

como va a funcionar el programa; Quizás después decida cambiar la historia, pero la 

programación va a ser la misma. Conforme vaya avanzando el curso iré incluyendo

mas cosas como un árbol de decisiones.


Pseudo Código


Monedas = 100

Print("Había una vez un caballero medieval genérico, que como todo caballero medieval genérico debía rescatar a la princesa que estaba encerrada en la cima de una torre custodiada por varios dragones.")

Print("Antes de partir a su misión el rey le dió una espada, un ungüento mágico que puede curar cualquier herida y 100 monedas para su viaje.")

Print("Así que el caballero salió a emprender su aventura...")

Print("Cuando el caballero entro al bosque se encontró con un vendedor que le ofrecía una espada mas grande por el precio de 50 monedas...")

Print("¿Aceptas la oferta? Sí/No")
Pedir respuesta 

Si "Sí" 
entonces monedas - 50
Print("Tienes una espada nueva")

Sino
Print("El vendedor se va") 

Print("Llega a la torre y la puerta esta cerrada")
Print ("¿Tocar la puera? Sí/No")
Pedir respuesta

Si "Sí"
print("Tocas la puerta y no hay respuesta , mueres esperando a que alguien abra la puerta. Fin del juego")

Sino 
print("¿Derribar la puerta? Sí/No?")
Pedir respuesta 

Si "Sí"
Print ("Derribaste la puerta y entraste al castillo")

Sino
Print ("Regresar al palacio por un abridor de puertas, otro día regresaras al castillo pero hoy fallaste. Fin del juego")

print("Entras al castillo y encuentras al dragón...")
Print("¿Atacar al dragón? Sí/No")
Pedir respuesta

Si "Sí"
Print("El dragón te pega y te mueres. Fin del juego")

Sino 
Print("El dragón te pregunta si quieres ser su amigo...")
Print("¿Quieres ser su amigo? Sí/No")
Pedir respuesta 

Si "Sí"
Print("El dragón se hace tu amigo y te ayuda a rescatar a la princesa, regresas al palacio como un héroe, un nuevo amigo y el amor tu vida. Fin del juego")

Sino
Print("El dragón se pone tan triste por tu respuesta que empieza a llorar, inunda el castillo y mueres ahogado. Fin del juego")

Print("¿Quieres volver a jugar? Sí/No")
Pedir respuesta

Si "Sí"
Entonces se regresa al principio

Sino
Fin del programa

