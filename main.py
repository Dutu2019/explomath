import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from gui import *
from threading import Thread

# Create the dictionary mapping note names to frequencies
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 
         'F#', 'G', 'G#', 'A', 'A#', 'B']

frequency_to_note = {}
for octave in range(0, 8):  # Octaves 0 through 7
    for i, note in enumerate(notes):
        # Calculate MIDI note number. C0 is MIDI note 12.
        midi_note = 12 + octave * 12 + i
        # Calculate frequency using the formula:
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

file_path = ask_file_upload()

# Variables for calculating FFT
sec_to_read = 0.3
sr = sf.info(file_path).samplerate
dT = 1.0 / sr
data, sr = sf.read(file_path, int(sec_to_read * sr), always_2d=True)
signal = data[:,0]

# Time axis for original signal graph
time = np.linspace(0, len(signal) / sr, num=len(signal))

# Making the fft graph
fft_freq = np.fft.fftfreq(len(signal), d=dT)
fft_values = np.abs(np.fft.fft(signal))

# Remove negative frequencies
positive_indices = np.where(fft_freq >= 0)
fft_freq = fft_freq[positive_indices]
fft_values = fft_values[positive_indices]

# Normalising magnitude [0, 1]
top_indices = np.argsort(fft_values)[::-1]
fft_values = np.abs(fft_values/fft_values[top_indices[0]])

# Get top frequencies and search their corresponding note
present_notes = []
present_freqs = fft_freq[np.where(fft_values>=0.3)]
diffs = np.diff(present_freqs)
mask = np.concatenate(([True], diffs > 5.0))
filtered_present_freqs = present_freqs[mask]
for key in frequency_to_note:
    for present_freq in filtered_present_freqs:
        if key-5 <= present_freq <= key+5:
            present_notes.append(frequency_to_note[key])

# GUI
activate_tiles(present_notes)
GUI_Thread = Thread(target=run_gui)
GUI_Thread.start()

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title("Time Domain")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.stem(fft_freq[:len(signal)//32], fft_values[:len(signal)//32], basefmt=" ")
plt.title("Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()