from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port
# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)
connection_result = client.connect()

def leergrupo():
    # Read device information
    if connection_result:
        try:
            response=client.read_holding_registers(120,18,1)   
            registers_values = response.registers
            binary_representations = [int(format(value)) for (value) in registers_values]
            #int_list = [int(x) for x in binary_representations]
            print(binary_representations)
        except Exception as e:
            print(f"Error leyendo: {e}")
        client.close()
leergrupo()