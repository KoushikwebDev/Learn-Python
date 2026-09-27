# import numpy as np
# import matplotlib.pyplot as plt

# # Parameters for the individual sine waves
# freqs = [2, 5, 10]  # Frequencies of the sine waves
# amps = [1.5, 0.8, 0.5]  # Amplitudes of the sine waves
# phases = [0, np.pi / 4, np.pi / 2]  # Phase shifts of the sine waves

# # Time values
# t = np.linspace(0, 2 * np.pi, 1000)

# # Generate individual sine waves and sum them up
# composite_wave = sum(
#     amp * np.sin(freq * t + phase) for freq, amp, phase in zip(freqs, amps, phases)
# )

# # Plot the composite wave
# plt.figure(figsize=(10, 6))
# plt.plot(t, composite_wave, label="Composite Wave")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.title("Composite Sine Wave by Koushik Saha")
# plt.legend()
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate a simple sine wave signal
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time values from 0 to 1 second
freq = 5  # Frequency of the sine wave
amplitude = 1  # Amplitude of the sine wave
signal = amplitude * np.sin(2 * np.pi * freq * t)

# Perform FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(
    len(fft_result), d=1 / fs
)  # Compute corresponding frequencies

# Plot the original signal and its FFT
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal")

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Result")

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time values from 0 to 1 second

# Frequencies and amplitudes of the sine waves
frequencies = [40, 30, 10]  # Frequencies of the sine waves in Hz
amplitudes = [10, 20, 30]  # Amplitudes of the sine waves

# Generate the composite signal
composite_signal = np.sum(
    amplitude * np.sin(2 * np.pi * freq * t)
    for freq, amplitude in zip(frequencies, amplitudes)
)

# Perform FFT
fft_result = np.fft.fft(composite_signal)
frequencies = np.fft.fftfreq(
    len(fft_result), d=1 / fs
)  # Compute corresponding frequencies

# Plot the composite signal and its FFT
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, composite_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Composite Signal")

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT Result")

plt.tight_layout()
plt.show()
