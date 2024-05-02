from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port

# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

def escribirplc(registro, valor):
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

    # Close the Modbus connection
    #client.close()