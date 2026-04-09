from finder import buscar_cocteles
from file_manager import cargar_datos, guardar_datos

def validar_entrada(texto):
    return texto.strip() != ""

def formatear_coctel(c):
    print(f" {c['nombre'].upper()}")
    print("Ingredientes:")
    for ing, medida in c["medidas"].items():
        print(f"- {medida} de {ing}")
    print("Preparación:", c["instrucciones"])


def buscar():
    entrada = input("¿Qué ingredientes tienes? (separados por coma): ").lower()

    if not validar_entrada(entrada):
        print(" Debes ingresar al menos un ingrediente.")
        return

    ingredientes_usuario = [i.strip() for i in entrada.split(",")]

    resultados, sugerencias = buscar_cocteles(ingredientes_usuario)

    if resultados:
        print("Bartender (recetas completas):")
        for c in resultados:
            formatear_coctel(c)

    if sugerencias:
        print("\n También podrías hacer:")
        for c, faltantes in sugerencias:
            print(f" {c['nombre'].upper()}")
            print("Te falta:", ", ".join(faltantes))

    if not resultados and not sugerencias:
        print(" No se encontró ningún cóctel.")


def agregar():
    nombre = input("Nombre del cóctel: ").lower()

    if not validar_entrada(nombre):
        print("Nombre inválido.")
        return

    ingredientes = input("Ingredientes (separados por coma): ").lower()

    if not validar_entrada(ingredientes):
        print("Debes ingresar ingredientes.")
        return

    lista_ingredientes = [i.strip() for i in ingredientes.split(",")]

    medidas = {}
    print("\nIntroduce las medidas:")
    for ing in lista_ingredientes:
        medida = input(f"Cantidad para {ing} (ej: 2 oz): ")
        medidas[ing] = medida

    instrucciones = input("Preparación: ")

    nuevo = {
        "nombre": nombre,
        "ingredientes": lista_ingredientes,
        "medidas": medidas,
        "instrucciones": instrucciones
    }

    data = cargar_datos()
    data.append(nuevo)
    guardar_datos(data)

    print("Cóctel guardado correctamente.")


def menu():
    while True:
        print(" BARTENDER APP")
        print("1. Buscar cóctel")
        print("2. Agregar cóctel")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            buscar()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()