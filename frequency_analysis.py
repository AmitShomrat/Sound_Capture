import sounddevice as sd
import numpy as np
import scipy.fftpack

import Convert_Values as cv
import Led_Simulator

# Settings
samplerate = 44100  # Sample rate in Hz
chunk_size = 1024  # Size of each audio block
device_index = 8  # Device index for the sound card


# Callback function to process audio data
def callback(indata, frames, time, status):
    if status:
        print(status)

    # Separate left and right channels
    left_channel = indata[:, 0]
    right_channel = indata[:, 1]

    # Compute frequency spectrum using FFT
    fft_data = np.abs(scipy.fftpack.fft(left_channel + right_channel))[:chunk_size // 2]
    freqs = np.fft.fftfreq(chunk_size, 1 / samplerate)[:chunk_size // 2]

    # Estimate the dominant frequency
    dominant_frequency = freqs[np.argmax(fft_data)]

    # Convert the frequency to RGB
    try:
        rgb = cv.frequency_to_rgb(round(dominant_frequency))
        print(f"Dominant Frequency: {dominant_frequency:.2f} Hz -> RGB: {rgb}")

        # Simulate LED graphics with the computed RGB
        # Led_Simulator.display(rgb)  # Replace with actual LED simulator function
    except ValueError as e:
        print(e)


# Open an input stream
with sd.InputStream(device=device_index, callback=callback, channels=2, samplerate=samplerate, blocksize=chunk_size):
    print("Capturing audio... Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopped capturing.")
