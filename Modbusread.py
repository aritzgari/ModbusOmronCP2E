from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port
# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

while True:
    # Connect to the Modbus server with a timeout
    connection_result = client.connect()
    # Read device information
    try:
        response=client.read_holding_registers(120,100,1)
        #print(response.registers[0]) da un número entero con el que indica los estados de las entradas
        binary = format(response.registers[0]) #Formatear lo leido con modbus a un binario y añadir 0 hasta tener 5 digitos
        #Leer cada digito de la variable y añadirla a una lista    
        print(binary)
    except Exception as e:
        print(f"Error leyendo: {e}")
    # Close the Modbus connection
    client.close()