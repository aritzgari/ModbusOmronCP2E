from pymodbus.client import ModbusTcpClient

# Modbus TCP server configuration
server_ip = '192.168.77.100'  # Replace with your server's IP address
server_port = 502           # Default Modbus TCP port

# Create a Modbus TCP client
client = ModbusTcpClient(server_ip, server_port)

# Connect to the Modbus server with a timeout
connection_result = client.connect()

if connection_result:
    print("Modbus device is reachable.")
    # Value to write to a single holding register
    value_to_write = 0

    # Write to a single holding register at address 301
    write_result = client.write_register(200, value_to_write, 1)
    
    # Check if the write was successful
    if write_result.isError():
        print(f"Write error: {write_result}")
    else:
        print("Write successful.")
else:
    print("Modbus device is not reachable.")

# Close the Modbus connection
client.close()