from machine import Pin, SPI
import time
import st7789  # or ili9341 depending on your display driver

# Define SPI Pins for ESP32 Feather V2
TFT_MOSI = 23  # Data (MOSI)
TFT_SCK  = 18  # Clock (SCK)
TFT_CS   = 5   # Chip Select (CS)
TFT_RST  = 4   # Reset (RST)
TFT_DC   = 33  # Data/Command (DC)

# Initialize SPI interface
spi = SPI(1, baudrate=40000000, polarity=0, phase=0, sck=Pin(TFT_SCK), mosi=Pin(TFT_MOSI))

# Initialize Display
tft = st7789.ST7789(spi, 240, 320, reset=Pin(TFT_RST, Pin.OUT), cs=Pin(TFT_CS, Pin.OUT), dc=Pin(TFT_DC, Pin.OUT))

# Clear Screen and Set Background
tft.fill(st7789.BLACK)

# Display a message
tft.text("ESP32 Feather V2!", 50, 100, st7789.WHITE)

# Blink an LED to indicate successful setup
#led = Pin(13, Pin.OUT)  # User LED on ESP32 Feather V2
#for _ in range(5):
  #  led.on()
   # time.sleep(0.5)
   # led.off()
   # time.sleep(0.5)

print("LCD Initialized Successfully!")
