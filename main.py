import sys
import pygame
import sounddevice as sd
from led_simulation import draw_leds, update_led_properties
from frequency_analysis import process_audio_callback

# Pygame and audio settings
WIDTH, HEIGHT = 800, 400
BLACK = (0, 0, 0)
samplerate = 44100
chunk_size = 1024
device_index = 8

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LED Simulator")
    clock = pygame.time.Clock()

    # Start audio stream
    with sd.InputStream(device=device_index, callback=process_audio_callback,
                        channels=2, samplerate=samplerate, blocksize=chunk_size):
        print("Capturing audio... Press Ctrl+C to stop.")

        try:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # Update LED visualization
                draw_leds(screen, WIDTH, HEIGHT, BLACK)
                pygame.display.flip()
                clock.tick(30)

        except KeyboardInterrupt:
            print("Stopped capturing.")


if __name__ == "__main__":
    main()
