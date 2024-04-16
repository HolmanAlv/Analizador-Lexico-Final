import tkinter as tk
from tkinter import filedialog
import analizador_lexico as AL

def leer_archivo():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as file:
            texto = file.read()
            texto_entrada.delete('1.0', tk.END)  # Limpiar el cuadro de texto
            texto_entrada.insert(tk.END, texto)

def realizar_analisis():
    texto = texto_entrada.get('1.0', tk.END)
    textoSalida = AL.realizarAnalisis(texto)
    texto_salida.delete('1.0', tk.END)  # Limpiar el cuadro de texto
    texto_salida.insert(tk.END, textoSalida)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador léxico para Java")

# Botón para leer archivo
boton_leer = tk.Button(ventana, text="Leer Archivo", command=leer_archivo)
boton_leer.pack()

# Crear el cuadro de texto
texto_entrada = tk.Text(ventana, height=15 ,width=75)
texto_entrada.pack(pady=10, padx=10, fill='x')

# Botón para realizar análisis
boton_analisis = tk.Button(ventana, text="Análisis", command=realizar_analisis)
boton_analisis.pack()

# Crear el cuadro de texto de salida
texto_salida = tk.Text(ventana, height=15, width=75)
texto_salida.pack(fill='both', pady=10, padx=10)





# Ejecutar el bucle de eventos
ventana.mainloop()
