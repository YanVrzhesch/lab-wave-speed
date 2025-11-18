import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    
    def deinit(self):
        self.bus.close()
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Get data: {data}, Upper byte: {upper_data_byte}, Lower byte: {lower_data_byte}, Number: {number}")
        return number

    def get_voltage(self):
        var = MCP3021.get_number(self)
        return self.dynamic_range/1024*var
    
if __name__ == "__main__":
    try:
        mcp = MCP3021(5.12)
        
        while True:
            voltage = mcp.get_voltage()
            print(voltage)
            time.sleep(0.25)

    finally:
        mcp.deinit()