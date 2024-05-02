import tkinter as tk
from pymodbus.client import ModbusTcpClient
import time
from ModbusLeerTodo import entradas
from Modbuswrite import escribirplc

# Create the main window
window = tk.Tk()
window.title("TF Virtual commissioning")

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port
client = ModbusTcpClient(server_ip, server_port)

# Create labels to display the initial data
labels = []
for i in range(18):
    label_text = f"Entrada {i+1}: "  # Correct label text
    label = tk.Label(window, text=label_text)
    labels.append(label)
    if i < 9:
        col = i
        row = 0
    else:
        col = i - 9
        row = 1
    label.grid(row=row, column=col, padx=5, pady=5)

# Function to update and display the data
def actualizar():
    # Call your function to obtain the data
    lista = obtener_datos()
    
    # Update the text of the labels with the new data
    for i, dato in enumerate(lista):
        labels[i].config(text=f"Entrada {i+1}: {dato}")

# Function to obtain data from the Modbus device
def obtener_datos():
    # Connect to the Modbus server with a timeout
    lista=[]
    #Tiempo en el que comienza la ejecución del programa para comparar al final
    start_time = time.time()
    connection_result = client.connect()
    if connection_result:
        print("Modbus device is reachable.")
        try:
            for memoria in range(100,118):
                    response=client.read_holding_registers(memoria,1,1)
                    entrada = format(response.registers[0]) #Formatear lo leido con modbus a un binario y añadir 0 hasta tener 5 digitos
                    #Leer cada digito de la variable y añadirla a una lista
                    lista.append(entrada)
                
        except Exception as e:
            print(f"Error leyendo: {e}")
    else:
        print("Modbus device is not reachable.")
    end_time = time.time()
    # Calculate the time taken
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
    return lista

# Call actualizar() once to display the initial data
actualizar()

def escribir(registro, valor):
    # Connect to the Modbus server with a timeout
    connection_result = client.connect()
    esclavo=1
    if connection_result:
        print("Modbus device is reachable.")
        
        # Write to a single holding register
        write_result = client.write_register(registro, valor, esclavo)
        
        # Check if the write was successful
        if write_result.isError():
            print(f"Write error: {write_result}")
        else:
            print("Write successful.")
    else:
        print("Modbus device is not reachable.")

# Create buttons to write 0 and 1
apagar1 = tk.Button(window, text="APAGAR", command=lambda:escribir(200, 0))
apagar1.grid(row=3, column=0, padx=5, pady=5)

encender1 = tk.Button(window, text="ENCENDER", command=lambda:escribir(200, 1))
encender1.grid(row=3, column=1, padx=5, pady=5)

# Create a button to update the data
button = tk.Button(window, text="Actualizar", command=actualizar)
button.grid(row=2, column=0, columnspan=9, pady=10)  # Span the button across both lines

# Run the Tkinter main loop
window.mainloop()