def modus_ponens():
    print("Modus Ponens:") #Imprime este comentario en la terminal
    print("Si estudias para el examen, entonces sacarás una buena calificación.") #Imprime este comentario en la terminal
    condicion_1 = input("¿Estudiaste para el examen? (s/n): ").lower() #Condiciona y pregunta al usuario para permitirle interactuar con el programa
    
    if condicion_1 == "s": #Cuando al condicion es si...
        print("Has estudiado para el examen.")
        afirmacion_consecuente = input("¿Crees que sacarás una buena calificación? (s/n): ").lower() #Hace la siguiente pregunta
        if afirmacion_consecuente == "s":
            print("Es probable que saques una buena calificación.") #Y genera el siguiente comentario
        elif afirmacion_consecuente == "n": 
            print("Quizás no saques una buena calificación.") #Si la respuesta es no entonces imprime este mensaje
        else:
            print("Respuesta no válida.") #Si hubo un error al escribir por parte del usuario imprime este mensaje 
    elif condicion_1 == "n": #Cuando al condicion es no...
        print("No has estudiado para el examen.") #Y genera el siguiente comentario
    else:
        print("Respuesta no válida.") #Si hubo un error al escribir por parte del usuario imprime este mensaje 

# Ejemplo de uso
modus_ponens()
