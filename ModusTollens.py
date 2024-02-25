# Supongamos que queremos tomar una decisión sobre si un animal es un pez basándonos en dos condiciones:
#Si el animal tiene branquias, entonces es un pez.
#El animal no es un pez.

def modus_tollens(condicion_1, condicion_2): 
    if condicion_2 == "no pez":
        if condicion_1 != "branquias":
            print("El animal no tiene branquias.")
        else:
            print("No se cumple el modus tollens.")
    else:
        print("No se cumple el modus tollens.")

# Ejemplo interactivo
print("Condiciones disponibles: branquias, no branquias, pez, no pez.")
condicion_1 = input("¿El animal tiene branquias? (branquias/no branquias): ").lower()
condicion_2 = input("¿El animal es un pez? (pez/no pez): ").lower()

modus_tollens(condicion_1, condicion_2)
