"""Basic NeoPixel LED animations for the QT Py."""
import time
import board
import neopixel
import adafruit_pypixelbuf
import random


# Update this to match the pin to which you connected the NeoPixels
pixel_pin = board.A2
# Update this to match the number of NeoPixels connected
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)
# Set to 0-1 to change the brightness of the NeoPixels
pixels.brightness = 1.0


def show_waterfall_animation():
    """
    Show a waterfall animation on the NeoPixels.
    """
    white_color = (255, 255, 255)
    black_color = (0, 0, 0)
    light_blue_color = (0, 0, 255)
    dark_blue_color = (0, 0, 128)

    # Make some random colors for the waterfall, using white_color, black_color, light_blue_color, and dark_blue_color
    waterfall_colors = []
    waterfall_frames = []

    for i in range(num_pixels):
        random_color = random.choice(
            [white_color, black_color, light_blue_color, dark_blue_color]
        )
        waterfall_colors.append(random_color)
    
    # Make the animation by shifting the colors down the waterfall
    for i in range(num_pixels):
        waterfall_colors.insert(0, waterfall_colors.pop())
        waterfall_frames.append(waterfall_colors[:])
    
    # Show the animation
    for frame in waterfall_frames:
        for i in range(num_pixels):
            pixels[i] = frame[i]
        pixels.show()
        time.sleep(0.05)


while True:
    show_waterfall_animation()
