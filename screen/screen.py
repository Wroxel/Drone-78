from screen.pico_parallel_lcd import GpioLcd
import utime
from .. import globals

# Define GPIO pins for LCD
RS = 0
E = 1
D4 = 2
D5 = 3
D6 = 4
D7 = 5

# Initialize the LCD
lcd = GpioLcd(
    rs_pin=RS,
    enable_pin=E,
    d4_pin=D4,
    d5_pin=D5,
    d6_pin=D6,
    d7_pin=D7,
    num_lines=2,
    num_columns=8,
)


def lcd_screen():
    lcd.clear()
    # Display a message
    lcd.write(globals.battery_status)
    lcd.set_cursor_to_second_line()
    lcd.write("(●'◡'●)")