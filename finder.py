from file_manager import cargar_datos

def normalizar(texto):
    return texto.lower().strip()

def coincide(parcial, ingrediente):
    return parcial in ingrediente or ingrediente in parcial

def buscar_cocteles(ingredientes_usuario):
    data = cargar_datos()
    resultados = []
    sugerencias = []

    ingredientes_usuario = [normalizar(i) for i in ingredientes_usuario]

    for coctel in data:
        ingredientes_coctel = [normalizar(i) for i in coctel["ingredientes"]]

        coincidencias = 0
        faltantes = []

        for ing in ingredientes_coctel:
            if any(coincide(ing, user_ing) for user_ing in ingredientes_usuario):
                coincidencias += 1
            else:
                faltantes.append(ing)

        # Coincidencia total
        if coincidencias == len(ingredientes_coctel):
            resultados.append(coctel)

        # Coincidencia parcial (al menos 50%)
        elif coincidencias >= len(ingredientes_coctel) / 2:
            sugerencias.append((coctel, faltantes))

    return resultados, sugerencias