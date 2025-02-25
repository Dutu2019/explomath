import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Creating freq:notes dictionnary
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 
         'F#', 'G', 'G#', 'A', 'A#', 'B']

# Create the dictionary mapping note names to frequencies
# In MIDI standard, C0 corresponds to MIDI note 12.
frequency_to_note = {}

for octave in range(0, 8):  # Octaves 0 through 7
    for i, note in enumerate(notes):
        # Calculate MIDI note number. C0 is MIDI note 12.
        midi_note = 12 + octave * 12 + i
        # Calculate frequency using the formula:
        # frequency = 440 * 2^((midi_note - 69)/12)
        freq = 440 * 2 ** ((midi_note - 69) / 12)
        # Round frequency to the nearest integer
        frequency_to_note[round(freq)] = f"{note}{octave}"

# Asking user to choose audio file
def ask_file_upload():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfile(
        title="Open audio file", 
        filetypes=[
            ("WAV Files", ".wav"), 
            ("MP3 Files", ".mp3"), 
            ("RAW Files", ".raw")
            ])
    if not file: exit()
    return file.name

file_path = "chord.wav"

# Variables for calculating FFT
sec_to_read = 3.0
sr = sf.info(file_path).samplerate
T = 1.0 / sr
data, sr = sf.read(file_path, int(sec_to_read * sr), always_2d=True)
first_channel = data[:,0]

# Making the fft graph
fft_values = np.fft.fft(first_channel, len(first_channel))
fft_freq = np.fft.fftfreq(len(first_channel), d=T)
magnitude = np.abs(fft_values)

# Remove negative frequencies
positive_indices = np.where(fft_freq >= 0)
positive_freqs = fft_freq[positive_indices]
positive_magnitude = magnitude[positive_indices]

# Frequency filter function 
top_indices = np.argsort(positive_magnitude)[::-1]
freq_set = {0}
freq_to_print = 6
i = 0
while freq_to_print>0:
    minimum = min(list(map(lambda visited_freq: (fft_freq[top_indices[i]]-visited_freq)**2, freq_set)))
    if minimum>50:
        print(f"Freq: {fft_freq[top_indices[i]]}\n")
        freq_set.add(fft_freq[top_indices[i]])
        freq_to_print -= 1
    i += 1

# Plotting the graphs
time = np.linspace(0, len(first_channel) / sr, num=len(first_channel))

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(time, first_channel)
plt.title("Time Domain")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.stem(fft_freq[:len(first_channel)//32], magnitude[:len(first_channel)//32], basefmt=" ")
plt.title("Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()