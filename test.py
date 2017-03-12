import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image

# Raspberry Pi pin configuration:
RST = 26
DC = 19
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# image = Image.open('test.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
image = Image.open('test.png').convert('1')

# Display image.
disp.image(image)
disp.display()
