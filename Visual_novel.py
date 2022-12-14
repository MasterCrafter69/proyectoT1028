"""
 Proyecto TC1028
 Daniel Aguilar Darío
 A01710975@tec.mx
 El proyecto consiste en una novela visual, espero que lo disfrutes.
"""
lista = ["°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø"
         ",¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,", "°º¤ø,¸¸,                                                                          "
         "                                     ,ø¤º°`°º¤ø,"]

castillo = [['|torre|', '*** muro ***', '|torre|'], ['*** muro ***', '[habitación_princesa]', '*** muro ***'],
            ['|torre|', '{entrada_pricipal}', '|torre|']]

personaje = ["princesa", "vendedor", "dragón"]

escenario = ["bosque", "castillo", "palacio"]

"""
============================================= funciones de la historia  ================================================
"""


def marco(position):
    """
    La función marco recibe el parametro position el cual se utiliza para indicar que tipo de marco se requiere, ya sea
    uno superior o uno inferior, también se utiliza para poner el marco final.
    """
    if position == 'arriba':
        print(lista[0])
        print(lista[1])
    elif position == 'abajo':
        print(lista[1])
        print(lista[0])
        print('')
    elif position == 'fin':
        print(lista[1])
        print("°º¤ø,¸¸,                                                 Fin del juego.                                 "
              "               ,ø¤º°`°º¤ø,")
        marco('abajo')


def asking_username(name):
    len(name)
    name = str(input("\nInserta tu nombre : \n"))
    if name == '':
        name = 'Caballero Generico'
    return name


def inicio(name):
    """
    La función inicio recibe un parametro nombre el cual es el nombre del jugador y se utiliza para integrarlo como
    parte de la historia.
    """
    name = asking_username(name)
    marco('arriba')
    print("°º¤ø,¸¸,                               Había una vez un caballero medieval llamado " + str(name) +
          "                              ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                que como todo caballero medieval genérico debía rescatar            "
          "           ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,             a la ", personaje[0], " que estaba encerrada en la cima de una torre custodiada por va"
          "rios dragones.      ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,  Antes de partir a su misión el rey le dió una espada, un ungüento mágico que puede curar cualquier"
          "herida     ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                         y 100 monedas para su viaje.                               "
          "           ,ø¤º°`°º¤ø,")
    print(lista[1])
    print("°º¤ø,¸¸,                                Así que el caballero salió a su aventura...                         "
          "           ,ø¤º°`°º¤ø,")
    marco('abajo')


def sword_2():
    """
    La función sword_2 se encarga de ilustrar una espada hecha con caracteres.
    """
    print("")
    print('     I')
    print('O===[====================>')
    print('     I   \n')


def vendedor(pregunta_vendedor, monedas):
    """
    La función vendedor recibe dos parametros, preguntar_vendedor y monedas, el primer parametro recibe el valor de
    la desición de de la pregunta al vendedor con lo cual se ejecutará la acción correspondiente, para el caso del
    parametro moneda se traslada el valor del total de las monedas en poseción del vendedor.
    """
    if pregunta_vendedor == 'entra_al_bosque':
        marco('arriba')
        print("°º¤ø,¸¸,  Cuando el caballero entro al", escenario[0], "se encontró con un", personaje[1],
              "que le ofrecia  una espada mas grande        ,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,                                         por el precio de 50 monedas...                         "
              "               ,ø¤º°`°º¤ø,")
        marco('abajo')

    if pregunta_vendedor == 'si':
        monedas = monedas - 50
        marco('arriba')
        print("Cantidad de monedas: ", monedas)
        print("Y una espada nueva")
        sword_2()
        marco('abajo')

    elif pregunta_vendedor == 'no':
        monedas = monedas - 5
        marco('arriba')
        print("El", personaje[1], " de todos modos quiere dinero, logra arrebatarte unas cuantas monedas y se va "
                                  "corriendo")
        print("Cantidad de monedas: ", monedas)
        marco('abajo')

    return monedas


def torre(puerta):
    """
    La función torre recibe el parametro de puerta el cual lleva el valor de la respuesta del jugador y mediante esta
    respuesta se ejecutará la acción del jugador.
    """
    if puerta == 'puerta_cerrada':
        marco('arriba')
        print("°º¤ø,¸¸,                                Llega al", escenario[1], "y la puerta esta cerrada              "
                                                                                "                       ,ø¤º°`°º¤ø,")
        marco('abajo')

    if puerta == 'tocar_la_puerta':
        marco('arriba')
        print(
            "°º¤ø,¸¸,                 Tocas la puerta y no hay respuesta , mueres esperando a que alguien abra la "
            "puerta.         ,ø¤º°`°º¤ø,")
        marco('fin')

    elif puerta == 'derribar_la_puerta':
        marco('arriba')
        print("°º¤ø,¸¸,                            Derribaste la puerta y entraste al", escenario[1],
              "                                       ,ø¤º°`°º¤ø,")
        marco('abajo')

    elif puerta == 'no_derribar':
        marco('arriba')
        print("°º¤ø,¸¸,   Regresas al", escenario[2], " por un abridor de puertas, otro día regresaras al",
              escenario[1], ""
                            " pero hoy fallaste.           ,ø¤º°`°º¤ø,")
        marco('fin')


def mapa_castillo():
    """
    La función de mapa_castillo se encarga de imprimir el mapa del castillo.
    """
    print('   ' + castillo[0][0] + ' ' + castillo[0][1] + ' ' + castillo[0][2])
    print(castillo[1][0] + ' ' + castillo[1][1] + ' ' + castillo[1][2])
    print('   ' + castillo[2][0] + ' ' + castillo[2][1] + ' ' + castillo[2][2])
    print('')


def dragon(encontrar):
    """
    La función degon recibe el parametro encontrar, este parametro contiene el valor de la selección del usuario para
    la selección de la siguiente esena del juego al encontrar al dragon
    """
    if encontrar == 'encontrar_dragon':
        marco('arriba')
        print("°º¤ø,¸¸,                                   Entras al", escenario[1], " y encuentras al", personaje[2], ""
              "                             ,ø¤º°`°º¤ø,")
        marco('abajo')

    if encontrar == 'atacar':
        marco('arriba')
        print("°º¤ø,¸¸,                                           El", personaje[2],
              "te pega y te mueres                  "
              "                     ,ø¤º°`°º¤ø,")
        marco('fin')

    elif encontrar == 'amigos':
        marco('arriba')
        print("°º¤ø,¸¸,                                      El", personaje[2],
              "te pregunta si quieres ser su amigo                            ,ø¤º°`°º¤ø,")
        marco('abajo')

    elif encontrar == 'si_amigos':
        marco('arriba')
        print("°º¤ø,¸¸,      El", personaje[2], "se hace tu amigo y te ayuda a rescatar a la ", personaje[0],
              " regresas al ", escenario[2], " como un héroe,    ,ø¤º°`°º¤ø,")
        print(
            "°º¤ø,¸¸,                                        un nuevo amigo y el amor tu vida.                         "
            "             ,ø¤º°`°º¤ø,")
        marco('fin')

    elif encontrar == 'no_amigos':
        marco('arriba')
        print("°º¤ø,¸¸,                        El ", personaje[2],
              " se poner triste por tu respuesta, tanto que empieza a llorar          ,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,                                        inunda el", escenario[1],
              " y mueres ahogado.                                  ,ø¤º°`°º¤ø,")
        marco('fin')


"""
===========================================  parte principal del programa ==============================================
"""
print('\nResponde a las preguntas utilizando si o no\n')
monedas = 100
respuesta = input('¿Quieres jugar?\n')
while respuesta != 'no':
    inicio('')
    monedas = vendedor('entra_al_bosque', monedas)
    pregunta_espada = input('¿Quieres comprar la espada?\n')
    if pregunta_espada == 'si':
        monedas = vendedor('si', monedas)
    elif pregunta_espada == 'no':
        monedas = vendedor('no', monedas)
    torre('puerta_cerrada')
    pregunta_puerta = input('¿Quieres tocar la puerta?\n')
    if pregunta_puerta == 'si':
        torre('tocar_la_puerta')
        respuesta = input('¿Volver a intentar?\n')
    elif pregunta_puerta == 'no':
        pregunta_derribar = input('¿Derribar la puerta?\n')
        if pregunta_derribar == 'no':
            torre('no_derribar')
            respuesta = input('¿Volver a intentar?\n')
        elif pregunta_derribar == 'si':
            torre('derribar_puerta')
            respuesta_mapa = input('¿ver mapa?\n')
            if respuesta_mapa == 'si':
                mapa_castillo()
            dragon('encontrar_dragon')
            respuesta_atacar = input('¿Atacar?\n')
            if respuesta_atacar == 'si':
                dragon('atacar')
                respuesta = input('¿Volver a intentar?\n')
            elif respuesta_atacar == 'no':
                dragon('amigos')
                respuesta_amigos = input('¿Quieres ser su amigo?\n')
                if respuesta_amigos == 'si':
                    dragon('si_amigos')
                    respuesta = input('¿Volver a intentar?\n')
                elif respuesta_amigos == 'no':
                    dragon('no_amigos')
                    respuesta = input('¿Volver a intentar?\n')
