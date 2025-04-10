"""
This code is used to show a simple resonance graph by inputing a known inductance and a known capacitance
author: Peter Kveton
"""

# This graph will plot the y-axis response and the x-axis frequency

import numpy as np
import matplotlib.pyplot as plt

# Initial Conditions
inductance = 10
capacitance = 0.001
resonant_freq = 1/np.sqrt(inductance * capacitance)
amplitude_constant = 1
initial_voltage = 5
resistance = 10
def calculate_y_values(resonant_frequency, amplitude_coef):
    amplitude_values = []
    current_values = []
    x_values = np.linspace(0, resonant_frequency + 25, 99)
    for index in x_values:
        if index == resonant_frequency:
            print(index)
            index = index + 0.001
            amplitude = amplitude_coef/(index - resonant_frequency)
            current = (index * initial_voltage) / (np.sqrt((inductance*index**2 - capacitance**-1)**2
                                                          + (resistance * index)**2))
            amplitude_values.append(amplitude)
            current_values.append(current)

        else:
            amplitude = amplitude_coef/(index - resonant_frequency)
            current = (index * initial_voltage) / (np.sqrt((inductance * index ** 2 - capacitance ** -1) ** 2
                                                           + (resistance * index) ** 2))
            amplitude_values.append(amplitude)
            current_values.append(current)
    return x_values, amplitude_values, current_values

def plot_values(values_array):
    x_values, amplitude_values, current_values = values_array[0], values_array[1], values_array[2]

    # Amplitude vs Frequency Graph
    #plt.plot(x_values, amplitude_values)
    #plt.title('Simple Resonance Graph', fontsize=18, fontweight='bold')
    #plt.xlabel(f'Frequency [Hz]', fontsize=18, fontweight='bold')
    #plt.ylabel(f'Amplitude', fontsize=18, fontweight='bold')
    #plt.plot()

    # Current vs Frequency Graph
    plt.plot(x_values, current_values)
    plt.title('RCL Current Resonance Graph', fontsize=18, fontweight='bold')
    plt.xlabel(f'Frequency [Hz]', fontsize=18, fontweight='bold')
    plt.ylabel(f'Current [Amps]', fontsize=18, fontweight='bold')
    plt.plot()
    plt.show()

print(plot_values(calculate_y_values(resonant_freq, amplitude_constant)))