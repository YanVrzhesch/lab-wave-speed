import mcp3021_driver
import RPi.GPIO as gpio
import time
import adc_plot

gpio.setmode(gpio.BCM)
door = 15
gpio.setup(door, gpio.IN)
mcp = mcp3021_driver.MCP3021(1)

v_values = []
t_values = []
duration = 3.0
filename = "exp5.txt"

try:
    '''while True:
        print(gpio.input(door))
        time.sleep(0.1)'''
    print(f"Waiting for door to open, filename {filename}")
    while ( gpio.input(door) ):
        pass

    t0 = time.time()
    vmax = 0

    while ( time.time()-t0 < duration ):
        voltage = mcp.get_voltage()
        t_values.append(time.time()-t0)
        v_values.append(voltage)
        vmax = max(voltage, vmax)

    with open(filename, 'w') as file:
        for i in range(len(t_values)):
            file.write(str(t_values[i]) + '\t' + str(v_values[i]) + '\n')
    adc_plot.plot_voltage_vs_time(t_values, v_values, vmax)

finally:
    mcp.deinit()