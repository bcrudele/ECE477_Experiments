from machine import Pin, SPI
import time
import ili934x # or ili9341 depending on your display driver

# Define SPI Pins for ESP32 Feather V2
TFT_MOSI = 13  # Data (MOSI)
TFT_SCK  = 14  # Clock (SCK)
TFT_CS   = 5   # Chip Select (CS)
TFT_RST  = 4   # Reset (RST)
TFT_DC   = 33  # Data/Command (DC)

# Initialize SPI interface
spi = SPI(1, baudrate=20000000, polarity=0, phase=0, sck=Pin(TFT_SCK), mosi=Pin(TFT_MOSI))

# Initialize Display
display = ili934x.ILI9341(spi, cs=Pin(5), dc=Pin(33), rst=Pin(4))

# Clear Screen and Set Background
display.text("HELLO world!", 50, 100)

print("LCD Initialized Successfully!")

