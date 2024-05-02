from pymodbus.client import ModbusTcpClient
import time

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port
client = ModbusTcpClient(server_ip, server_port)
connection_result = client.connect()
# Function to update and display the data
def leer():
    # Connect to the Modbus server with a timeout
    lista=[]
    #Tiempo en el que comienza la ejecución del programa para comparar al final
    #start_time = time.time()
    if connection_result:
        #print("Modbus device is reachable.")
        try:
            for memoria in range(100,118):
                    response=client.read_holding_registers(memoria,1,1)
                    entrada = format(response.registers[0]) #Formatear lo leido con modbus a un binario y añadir 0 hasta tener 5 digitos
                    #Leer cada digito de la variable y añadirla a una lista
                    lista.append(int(entrada)) #El tipo de la variable original es string.
                
        except Exception as e:
            print(f"Error leyendo: {e}")
    else:
        print("Modbus device is not reachable.")
    
    """ # Calculate the time taken
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds") """
    
    return lista

def escribir(registro, valor):
    esclavo=1
    if connection_result:
        #print("Modbus device is reachable.")
        
        # Write to a single holding register
        write_result = client.write_register(registro, valor, esclavo)
        
        # Check if the write was successful
        if write_result.isError():
            print(f"Write error: {write_result}")
        else:
            print("Write successful.")
    else:
        print("Modbus device is not reachable.")

while True:
    lista=leer()
    print(lista[6])
    if lista[6] == 1:
        print("botón pulsado")
        escribir(200,1)
    else:
        escribir(200,0)