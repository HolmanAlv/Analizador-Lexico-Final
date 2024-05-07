import tkinter as tk
from tkinter import filedialog
import analizadorLexico as AL
import analizadorSintactico as AS

def leer_archivo():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as file:
            texto = file.read()
            texto_entrada.delete('1.0', tk.END)  # Limpiar el cuadro de texto
            texto_entrada.insert(tk.END, texto)

def realizar_analisisLexico():
    texto = texto_entrada.get('1.0', tk.END)
    textoSalida = AL.realizarAnalisis(texto)
    texto_salida.delete('1.0', tk.END)  # Limpiar el cuadro de texto
    texto_salida.insert(tk.END, textoSalida)

def realizar_analisisSintactico():
    texto = texto_entrada.get('1.0', tk.END)
    textoSalida = AS.realizarAnalisisSintactico(texto)
    texto_salida.delete('1.0', tk.END)  # Limpiar el cuadro de texto
    texto_salida.insert(tk.END, textoSalida)

def agregar_asignacion():
    with open("ejemploAsignacion.txt", "r") as file:
        texto = file.read()
        texto_entrada.delete('1.0', tk.END)  # Limpiar el cuadro de texto
        texto_entrada.insert(tk.END, texto)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador léxico para Java")

# Botón para leer archivo
boton_leer = tk.Button(ventana, text="Leer Archivo", command=leer_archivo)
boton_leer.pack()

# Crear el cuadro de texto
texto_entrada = tk.Text(ventana, height=15 ,width=75)
texto_entrada.pack(pady=10, padx=10, fill='x')

# Botón para agregar asignacion y declaración
boton_analisis = tk.Button(ventana, text="asignación y declaración", command=agregar_asignacion)
boton_analisis.pack()


# Botón para realizar análisis léxico
boton_analisis = tk.Button(ventana, text="Análisis léxico", command=realizar_analisisLexico)
boton_analisis.pack()

# Botón para realizar análisis sintáctico
boton_analisis = tk.Button(ventana, text="Análisis sintáctico", command=realizar_analisisSintactico)
boton_analisis.pack()


# Crear el cuadro de texto de salida
texto_salida = tk.Text(ventana, height=15, width=75)
texto_salida.pack(fill='both', pady=10, padx=10)





# Ejecutar el bucle de eventos
ventana.mainloop()
