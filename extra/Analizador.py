import tkinter as tk
from tkinter import filedialog, Text
import os

# Esta función se llamará cuando se presione el botón "Cargar Archivo".
def cargar_archivo():
    filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar Archivo",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    archivo_label.config(text=filename)
    global ruta_archivo
    ruta_archivo = filename

# Esta función se llamará cuando se presione el botón "Analizar Archivo".
def analizar_archivo():
    if ruta_archivo:
        # Aquí deberías llamar a tu función de análisis pasándole ruta_archivo como argumento.
        # resultado_analisis = mi_funcion_de_analisis(ruta_archivo)
        resultado_analisis = "Resultado del análisis."  # Simulación del resultado
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete(1.0, tk.END)
        resultado_texto.insert(tk.END, resultado_analisis)
        resultado_texto.config(state=tk.DISABLED)
    else:
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete(1.0, tk.END)
        resultado_texto.insert(tk.END, "Por favor, carga un archivo primero.")
        resultado_texto.config(state=tk.DISABLED)

# Configuración inicial de la ventana de Tkinter.
root = tk.Tk()
root.title("Analizador de Archivos")

ruta_archivo = ''

# Botón para cargar el archivo.
cargar_archivo_btn = tk.Button(root, text="Cargar Archivo", padx=10, pady=5, fg="white", bg="#263D42", command=cargar_archivo)
cargar_archivo_btn.pack()

# Etiqueta para mostrar el archivo cargado.
archivo_label = tk.Label(root, text="Ningún archivo seleccionado", bg="gray")
archivo_label.pack()

# Botón para analizar el archivo.
analizar_archivo_btn = tk.Button(root, text="Analizar Archivo", padx=10, pady=5, fg="white", bg="#263D42", command=analizar_archivo)
analizar_archivo_btn.pack()

# Área de texto para mostrar el resultado del análisis.
resultado_texto = Text(root, height=10, width=50)
resultado_texto.pack()
resultado_texto.config(state=tk.DISABLED)

root.mainloop()
