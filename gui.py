import tkinter as tk
from finder import buscar_cocteles

def buscar():
    entrada = entry.get().lower()

    if entrada.strip() == "":
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, " Ingresa ingredientes")
        return

    ingredientes_usuario = [i.strip() for i in entrada.split(",")]

    resultados, sugerencias = buscar_cocteles(ingredientes_usuario)

    resultado_text.delete("1.0", tk.END)

    if resultados:
        resultado_text.insert(tk.END, " Cócteles completos:\n\n")
        for c in resultados:
            resultado_text.insert(tk.END, f" {c['nombre'].upper()}\n")
            for ing, medida in c["medidas"].items():
                resultado_text.insert(tk.END, f"- {medida} de {ing}\n")
            resultado_text.insert(tk.END, f"{c['instrucciones']}\n\n")

    if sugerencias:
        resultado_text.insert(tk.END, "Puedes intentar:\n\n")
        for c, faltantes in sugerencias:
            resultado_text.insert(tk.END, f" {c['nombre'].upper()}\n")
            resultado_text.insert(tk.END, f"Faltan: {', '.join(faltantes)}\n\n")

    if not resultados and not sugerencias:
        resultado_text.insert(tk.END, " No se encontró nada.")


# Ventana principal
ventana = tk.Tk()
ventana.title(" Ayudante de Bartender")
ventana.geometry("500x500")

# Título
label = tk.Label(ventana, text="Ingresa tus ingredientes:", font=("Arial", 12))
label.pack(pady=10)

# Input
entry = tk.Entry(ventana, width=50)
entry.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Buscar Cóctel", command=buscar)
boton.pack(pady=10)

# Área de resultados
resultado_text = tk.Text(ventana, height=20, width=60)
resultado_text.pack(pady=10)

ventana.mainloop()