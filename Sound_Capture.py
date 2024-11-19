import sounddevice as sd
import numpy as np
import scipy.fftpack

# Settings
samplerate = 44100  # Sample rate in Hz
chunk_size = 1024   # Size of each audio block
device_index = 8    # Device index for the sound card (set according to your list)

# Callback function to process audio data
def callback(indata, frames, time, status):
    if status:
        print(status)

    # Separate left and right channels (float32 dtype)
    left_channel = indata[:, 0]
    right_channel = indata[:, 1]


    # Compute frequency spectrum using FFT
    # the fft_data is computed to deliver the position of the dominant frequency.
    fft_data = np.abs(scipy.fftpack.fft(left_channel + right_channel))[:chunk_size // 2]
    freqs = np.fft.fftfreq(chunk_size, 1 / samplerate)[:chunk_size // 2]

    # Estimate the dominant frequency
    dominant_frequency = freqs[np.argmax(fft_data)]

    # Compute dynamic range (RMS value for both channels)
    rms_left = np.sqrt(np.mean(left_channel**2))
    rms_right = np.sqrt(np.mean(right_channel**2))
    dynamic_range = 20 * np.log10((rms_left + rms_right) / 2)  # Adding 1e-6 to avoid log(0)

    # Compute panning (balance between left and right channels)
    panning = (rms_right - rms_left) / (rms_left + rms_right + 1e-6)

    # Log the results
    print(f"Frequency: {dominant_frequency:.2f} Hz, Dynamic Range: {dynamic_range:.2f} dB, Panning: {panning:.2f}")

# Open an input stream
with sd.InputStream(device=device_index , callback=callback, channels=2, samplerate=samplerate, blocksize=chunk_size):
    print("Capturing audio... Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopped capturing.")
