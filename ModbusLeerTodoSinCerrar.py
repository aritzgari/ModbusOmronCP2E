from pymodbus.client import ModbusTcpClient
import time
# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port

# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)
while True:
    # Connect to the Modbus server with a timeout
    lista=[]

    #Tiempo en el que comienza la ejecución del programa para comparar al final
    start_time = time.time()

    connection_result = client.connect()
    if connection_result:
        print("Modbus device is reachable.")
        try:
            for memoria in range(18):
                    response=client.read_holding_registers(memoria+101,1,1)
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
    
    # Close the Modbus connection ¡¡¡¡¡Si se cierra tarda un segundo en volver a conectar!!!!!!
    #client.close()
    print(lista)