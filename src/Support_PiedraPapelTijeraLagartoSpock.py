import random
import pyfiglet
from colorama import init, Fore

class PiedraPapelTijeraLagartoSpock():
    def __init__(self) -> None:
        
        self.recursos = [
            {"piedra":{"tijera" : "Piedra Aplasta a Tijera.","lagarto" : "Piedra Aplasta a Lagarto."}},
            {"papel" :{"piedra" : "Papel Envuelve a Piedra.","spock" : "Papel Refuta a Spock."}},
            {"tijera":{"papel" : "Tijera Corta a Papel.","lagarto" : "Tijera Decapita a Lagarto."}},
            {"lagarto":{"spock" : "Lagarto Envenena a Spock.","papel" : "Lagarto Devora a Papel."}},
            {"spock":{"tijera" : "Spock Aplasta a Tijera.","piedra" : "Spock Vaporiza a Piedra."}}
        ]

    def buscar_en_diccionario(self,entrada,dickcionario):
        """
        Busca una entrada en un diccionario.

        Este método intenta acceder a un valor en el diccionario utilizando la entrada proporcionada como clave. 
        Si la clave existe, devuelve `True`. Si no existe, captura la excepción y devuelve `False`.

        Args:
            entrada (str): La clave que se desea buscar en el diccionario.
            dickcionario (dict): El diccionario en el que se realiza la búsqueda.

        Returns:
            bool: `True` si la entrada se encuentra en el diccionario; de lo contrario, `False`.
        """
        try:
            dickcionario[entrada]
            return True
        except:
            return False

    def ver_ganador_o_empate(self,user,machinery,versus):
        """
        Determina el ganador de un enfrentamiento entre el usuario y la máquina.

        Este método evalúa las selecciones del usuario y de la máquina para determinar el resultado de un juego. 
        Utiliza un diccionario de interacciones (`versus`) para verificar si la selección del usuario gana 
        o pierde contra la selección de la máquina. Devuelve un código que indica el resultado.

        Args:
            user (str): La selección del usuario (por ejemplo, "piedra", "papel", "tijera").
            machinery (str): La selección de la máquina (por ejemplo, "piedra", "papel", "tijera").
            versus (list): Una lista de listas que contiene diccionarios de interacciones entre selecciones.

        Returns:
            int: 
                - `0` si el usuario gana a la máquina,
                - `1` si la máquina gana al usuario,
                - `-1` si no se determina un ganador (por ejemplo, en caso de empate).
        """
        seleccion_usuario = user
        seleccion_maquina = machinery
        diccionario_usuario = versus[0][0][seleccion_usuario]
        diccionario_maquina = versus[1][0][seleccion_maquina]
        resultado = -1
        if seleccion_maquina in diccionario_usuario:
                resultado = 0 #Usuario gana a maquina
                return resultado
                
        elif seleccion_usuario in diccionario_maquina:
                resultado = 1 #Maquina gana a usuario
                return resultado


    def batalla(self):
        """
        Inicia el juego de Piedra, Papel, Tijera, Lagarto, Spock.

        Este método permite al usuario jugar una serie de rondas contra una inteligencia artificial. 
        El usuario selecciona el número de rondas (máximo 5) y elige entre las opciones disponibles 
        (Piedra, Papel, Tijera, Lagarto o Spock). Después de cada ronda, se determina el resultado 
        y se muestra al usuario el número de victorias y derrotas al final del juego.

        Returns:
            None: Este método no devuelve un valor, pero imprime en pantalla el resultado del juego
            y la puntuación final del usuario.
        """
        init(autoreset=True)
        titulo = pyfiglet.figlet_format("Pi.Pa.Ti.La.Sp", font="slant")
        print(Fore.GREEN + titulo)
        print("Bienvenido a Piedra, Papel, Tijera, Lagarto, Spock!:")
        print("Las reglas son simples:")
        print("1º Selecciona cuantas rondas quieres jugar.")
        print("2º Elige entre Piedra,Papel,Tijera,Lagarto o Spock y escríbela")
        print("3º Al finalizar las rondas obtendrás los resultados")
        print("Jugarás en contra de una IA de alto rendimiento, ¿estás listo?")
        input(Fore.YELLOW + "Estas listo?, Presiona Cualquier Tecla para Jugar!")
        print("")

        ok = False
        while ok == False:
                try:
                    rondas = int(input(Fore.GREEN + f"Elige el número de rondas (máximo 5)"))
                    if int(rondas) > 5 or int(rondas) <= 0:
                        print(f"Como no haces caso ahora te haces 5 rondas chaval")
                        rondas = 5
                        
                    ok = True
                    i = 0
                    wins = 0
                    loses = 0
                    while i < rondas:
                        choose = ["piedra","papel", "tijera","lagarto","spock"]
                        numero_random = random.randrange(0, 5, 1)
                        maquina_elige = choose[numero_random]
                        user = input("Piedra, Papel, Tijera, Lagarto o Spock?, elige: ")
                        if user.lower() == "stop":
                            break
                        check = 0
                        if user.lower() == "piedra" or user.lower() == "papel" or user.lower() == "tijera" or user.lower() == "lagarto" or user.lower() == "spock":
                            check =  1
                        else:
                            while check == 0:
                                user = input("Piedra, Papel, Tijera, Lagarto o Spock?, elige: ")
                                if user.lower() == "piedra" or user.lower() == "papel" or user.lower() == "tijera" or user.lower() == "lagarto" or user.lower() == "spock":
                                    check = 1
                                else:
                                    print(f"Has introducido un valor incorrecto, reintenta")

                        
                        
                        userl = user.lower()
                        while maquina_elige == userl:
                            numero_random = random.randrange(0, 5, 1)
                            maquina_elige = choose[numero_random]
                        
                        seleccion_maquina = list(filter(lambda recursom:self.buscar_en_diccionario(maquina_elige,recursom),self.recursos))
                        seleccion_user = list(filter(lambda recurso:self.buscar_en_diccionario(userl,recurso),self.recursos))
                        que_vs_que = [seleccion_user,seleccion_maquina] #Sabemos que [0] siempre es user y [1] siempre será la máquina
                        resultado = self.ver_ganador_o_empate(userl,maquina_elige,que_vs_que)
                        textovs = pyfiglet.figlet_format(f"{userl} VS {maquina_elige}")
                        print(Fore.MAGENTA + textovs)
                        print(f"Has elegido: "+ f"{userl}")
                        print(f"La IA de alto rendimiento ha escogido: {maquina_elige}")

                        if resultado == 0:
                            wins += 1
                            reason = seleccion_user[0][userl][maquina_elige]
                            textowin = pyfiglet.figlet_format(f"GANAS")
                            print(Fore.GREEN + textowin)
                            print(Fore.YELLOW + reason)
                            print("")
                            input("Pulsa cualquier tecla para continuar")
                            print("")
                            i += 1
                        else:
                            loses += 1
                            reason = seleccion_maquina[0][maquina_elige][userl]
                            textowin = pyfiglet.figlet_format(f"PIERDES")
                            print(Fore.RED + textowin)
                            print(Fore.YELLOW + reason)
                            print("")
                            input("Pulsa cualquier tecla para continuar")
                            print("")
                            i += 1
                        
                    textowin = pyfiglet.figlet_format(f"RESULTADOS")
                    print(Fore.GREEN + textowin)
                    print(Fore.YELLOW + f"De {rondas} has ganado {wins} y has perdido {loses}, tu puntuación es de {wins}/{rondas}")
                    print(Fore.CYAN + f"Pulsa cualquier tecla para salir del juego.")

                except:
                    print(f"Valor incorrecto, reinténtalo")
                    ok = False

