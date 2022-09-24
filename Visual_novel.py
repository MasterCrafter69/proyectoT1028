monedas = 100
buenas_acciones = 100

def marco_arriba():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°¤ø,¸¸,ø¤º°`°º")
    print("°º¤ø,¸¸,                                                                                           ,ø¤º°`°º")


def marco_abajo():
    print("°º¤ø,¸¸,                                                                                           ,ø¤º°`°º")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°¤ø,¸¸,ø¤º°`°º")


def asking_username():
    global name
    name = str(input("enter the name : "))
    return name

def sword_2():
    print("")
    print('     I')
    print('O===[====================>')
    print('     I   \n')

def entra_al_bosque():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,  Cuando el caballero entro al bosque se encontró con un vendedor que le ofrecia una espada mas grande         ,ø¤º°`°º¤ø,\n"
        "°º¤ø,¸¸,                                         por el precio de 50 monedas...                                        ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,\n")
    resp = input("¿continuar? si/no\n")
    return resp

def si_acepte_la_oferta():
    global monedas
    monedas = monedas - 50
    print("Cantidad de monedas:", monedas)
    print("Y una espada nueva")
    sword_2()

def no_acepte_la_oferta():
    global monedas
    monedas = monedas - 25
    print("El vendedor de todos modos quiere dinero, logra arrebatarte unas cuantas monedas y se va corriendo")
    print("Cantidad de monedas:", monedas)

def torre():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                Llega a la torre y la puerta esta cerrada                                      ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    resp = input("¿continuar? si/no\n")
    return resp

def tocas_la_puerta():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                   Tocas la puerta y no hay respuesta , mueres esperando a que alguien abra la puerta.         ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                 Fin del juego.                                                ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    exit()


def si_derribar_puerta():
    if pregunta_derribar ==("si"):
        print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,                                Derribaste la puerta y entraste al castillo                                    ,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
        print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
        resp = input("¿continuar? si/no\n")
        return resp

def no_derribar_puerta():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,   Regresas al palacio por un abridor de puertas, otro día regresaras al castillo pero hoy fallaste.           ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                 Fin del juego.                                                ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    exit()

def dragon():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                    Entras al castillo y encuentras al dragón...                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,\n")


def atacar():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                           El dragón te pega y te mueres                                       ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                 Fin del juego.                                                ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    exit()


def amigos():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                El dragón te pregunta si quieres ser su amigo                                  ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")

def si_amigo():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,      El dragón se hace tu amigo y te ayuda a rescatar a la princesa, regresas al palacio como un héroe,       ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                        un nuevo amigo y el amor tu vida.                                      ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                 Fin del juego.                                                ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    exit()


def no_amigo():
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                         El dragón se poner triste por tu respuesta que empieza a llorar                       ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                        inunda el castillo y mueres ahogado.                                   ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                 Fin del juego.                                                ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
    exit()


asking_username()
print("")
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                               Había una vez un caballero medieval llamado " + str(name) +"                    ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                                que como todo caballero medieval genérico debía rescatar                       ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,             a la princesa que estaba encerrada en la cima de una torre custodiada por varios dragones.        ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,  Antes de partir a su misión el rey le dió una espada, un ungüento mágico que puede curar cualquier herida    ,ø¤º°`°º¤ø,\n"
      "°º¤ø,¸¸,                                         y 100 monedas para su viaje.                                          ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                                Así que el caballero salió a su aventura...                                    ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,                                                                                                               ,ø¤º°`°º¤ø,")
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,°º¤ø,¸¸,ø¤º°`°º¤ø,\n")

respuesta = input("¿Quieres entrar al bosque? si/no\n")
while respuesta == 'si':
    respuesta = entra_al_bosque()
    pregunta_espada = input("¿Aceptas la oferta? si/no\n")
    if pregunta_espada == ("si"):
        si_acepte_la_oferta()
    elif pregunta_espada == ("no"):
        no_acepte_la_oferta()
    respuesta = torre()
    if respuesta == ("no"):
        break
    pregunta_puerta = input("¿Tocar la puerta? si/no")
    if pregunta_puerta == ("si"):
        tocas_la_puerta()
    elif pregunta_puerta == ("no"):
        pregunta_derribar = input("¿Derribar la puerta? si/no?")
        if pregunta_derribar == ("si"):
           respuesta = si_derribar_puerta()
           if respuesta == ("no"):
               break
        elif pregunta_derribar == ("no"):
            no_derribar_puerta()
        dragon()
        pregunta_atacar = input("¿Atacar al dragón? si/no \n")
        if pregunta_atacar == ("si"):
            atacar()
        elif pregunta_atacar ==("no"):
            amigos()
            pregunta_amigo = input("¿Quieres ser su amigo? si/no \n")
            if pregunta_amigo == ("si"):
                si_amigo()
            elif pregunta_amigo == ("no"):
                no_amigo()

print('Fin del juego')
exit()

