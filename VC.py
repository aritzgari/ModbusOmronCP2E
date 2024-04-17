#Intento de aplicación para virtual commissioning
import tkinter as tk
from ModbusLeerTodoSinCerrar import entradas

# Create the main window
window = tk.Tk()
window.title("TF Virtual commissioning") 


# Función para actualizar y mostrar los datos
def actualizar():
    # Llama a tu función para obtener los datos
    lista = obtener_datos()
    
    # Actualiza la interfaz gráfica con los nuevos datos
    actualizar_interfaz(lista)
    
    # Programa la próxima actualización después de 500 milisegundos (0.5 segundos)
    window.after(100, actualizar)

# Función para obtener los datos del dispositivo Modbus
def obtener_datos():
    return entradas()

# Función para actualizar la interfaz gráfica con los datos
def actualizar_interfaz(lista):
    # Borra cualquier widget anterior en la ventana
    for widget in window.winfo_children():
        widget.destroy()

    # Muestra los datos en la ventana organizados en columnas de 5
    for i, dato in enumerate(lista):
        row = i // 5  # Calcula la fila actual
        col = i % 5   # Calcula la columna actual
        label = tk.Label(window, text=f"Entrada {i+1}: {dato}")
        label.grid(row=row, column=col, padx=5, pady=5)

# Inicia el ciclo de actualización
actualizar()

# Ejecuta el bucle principal de Tkinter
window.mainloop()