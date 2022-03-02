import pyperclip
import keyboard
import time
from pystray import MenuItem as Item
import pystray
from PIL import Image


class FormatNuker:
    def __init__(self):
        self.should_run = True

    def update_clipboard_format(self):

        if self.should_run:
            # need to wait for os
            time.sleep(0.2)
            text_from_clipboard = pyperclip.paste()
            # encodes to bytes in ascii
            text = text_from_clipboard.encode('ascii', errors='ignore')

            if text_from_clipboard != '':
                print("Format nuked!")
                # decode bytes to ascii
                decoded_text = text.decode('ascii')
                pyperclip.copy(decoded_text)
            else:
                print("Couldnt remove the format...")
        else:
            print("Paused!")

    def quit_window(self, tray_icon, item):
        tray_icon.stop()

    def pause(self, tray_icon, item):
        self.should_run = not self.should_run


nuker = FormatNuker()

# Create system tray
image = Image.open("settings.ico")
menu = [Item('Quit', nuker.quit_window), Item('Pause', nuker.pause)]
icon = pystray.Icon("name", image, "Format nuker", menu)

# Add hot key
keyboard.add_hotkey('ctrl+c', nuker.update_clipboard_format)

# start system tray icon
icon.run()
