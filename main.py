import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

sec_to_read = 0.2
sr = 44_100
T = 1.0 / sr
first_channel, _ = sf.read("250.wav", int(sec_to_read * sr))

# first_channel = data[:,0]
time = np.linspace(0, len(first_channel) / sr, num=len(first_channel))

def DFT(data: np.ndarray, sample_rate: int) -> np.ndarray:
    num_of_samples = len(data)
    freq_axis = np.linspace(0, num_of_samples, num=num_of_samples)
    amp_axis = np.zeros(num_of_samples, dtype=np.float64)

    # Create list of phases
    n_list = np.linspace(0, num_of_samples-1, num_of_samples)
    phase_list = 2 * np.pi * n_list / num_of_samples
    for i, freq in enumerate(np.nditer(freq_axis)):
        cos_value = np.sum(data*np.cos(phase_list*freq))/num_of_samples
        sin_value = np.sum(data*np.sin(phase_list*freq))/num_of_samples
        amp_axis[i] = (cos_value**2+sin_value**2)**(1/2)
    return (freq_axis, amp_axis)

fft_values = np.fft.fft(first_channel, len(first_channel))
fft_freq = np.fft.fftfreq(len(first_channel), d=T)
magnitude = np.abs(fft_values)

positive_indices = np.where(fft_freq >= 0)
positive_freqs = fft_freq[positive_indices]
positive_magnitude = magnitude[positive_indices]

top_indices = np.argsort(positive_magnitude)[::-1]
for i in top_indices[:5]:
    print(f"Freq: {fft_freq[i]}\n")

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(time, first_channel)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.stem(fft_freq[:len(first_channel)//8], magnitude[:len(first_channel)//8], basefmt=" ")
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()