from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):

    plt.figure(figsize=(10,6))

    plt.plot(time, voltage, 'g')
    plt.plot(time, voltage, '.g')

    plt.title("Напряжение на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.ylim(0, 1.1*max_voltage)
    plt.grid()

    plt.show()

def plot_sampling_period_hist(time):

    time_steps = []
    for i in range(len(time)-1):
        time_steps.append(time[i+1]-time[i])
    
    plt.figure(figsize=(10,6))

    plt.hist(time_steps)

    plt.title("Распределение периодов дискретизации (время на измерение)")
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество")

    #plt.xlim(0, 0.06)
    # на кой черт (?)
    plt.grid()

    plt.show()