import tkinter as tk
from tkinter import messagebox
import subprocess

def execute_esptool(command):
    try:
        # Open a command prompt window and execute the specified command
        subprocess.Popen(['start', 'cmd', '/k', 'python', '-m', 'esptool'] + command, shell=True)
    except Exception as e:
        # Display an error message if the command fails
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("ESPTool GUI")

# Create and configure the "Execute ESPTool" button
button_esptool = tk.Button(window, text="Execute ESPTool", command=lambda: execute_esptool([]))
button_esptool.pack(pady=10)

# Create and configure the "Execute ESP8266" button
button_esp8266 = tk.Button(window, text="Execute ESP8266", command=lambda: execute_esptool(['--chip', 'esp8266', 'erase_flash']))
button_esp8266.pack(pady=10)

# Create and configure the "Execute ESP32" button
button_esp32 = tk.Button(window, text="Execute ESP32", command=lambda: execute_esptool(['--chip', 'esp32', 'erase_flash']))
button_esp32.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
