import mcp3021_driver
import time
import adc_plot

v_values = []
t_values = []

duration = 10.0

try:
    mcp = mcp3021_driver.MCP3021(5.12)
    t0 = time.time()
    vmax = 0

    while ( time.time()-t0 < duration ):
        voltage = mcp.get_voltage()
        t_values.append(time.time()-t0)
        v_values.append(voltage)
        vmax = max(voltage, vmax)

    adc_plot.plot_voltage_vs_time(t_values, v_values, vmax)
    adc_plot.plot_sampling_period_hist(t_values)

finally:
    mcp.deinit()