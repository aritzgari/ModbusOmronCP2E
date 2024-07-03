import time
from pymodbus.client import ModbusTcpClient

i=0
base=120
botones=7
salidas=140

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502             # Default Modbus TCP port
client = ModbusTcpClient(server_ip, server_port)
connection_result = client.connect()

# Function to update and display the data
def leer():
    # Connect to the Modbus server with a timeout
    lista=[]
    if connection_result:
        try:
            for memoria in range(base,base+botones): # for memoria in range(120,138): MAX
                response=client.read_holding_registers(memoria,1,1)
                entrada = format(response.registers[0])
                #Leer cada digito de la variable y añadirla a una lista
                lista.append(int(entrada)) #El tipo de la variable original es string. 
        except Exception as e:
            print(f"Error leyendo: {e}")
    else:
        print("Modbus device is not reachable.")
    return lista

def escribir(registro, valor):
    esclavo=1
    if connection_result:
        write_result = client.write_register(registro, valor, esclavo)
        # Check if the write was successful
        if write_result.isError():
            print(f"Write error: {write_result}")
    else:
        print("Modbus device is not reachable.")

while True:
    lista=leer()
    print(lista)
    numero=salidas+i
    escribir(numero,1)
    time.sleep(1)
    escribir(numero,0)
    i=i+1 
    if(i==12):
        i=0
    