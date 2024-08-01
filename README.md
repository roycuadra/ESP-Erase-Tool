# ESP Erase Tool GUI

This Python application provides a graphical user interface (GUI) for executing commands using `esptool`. It uses Tkinter for the GUI and subprocess for executing commands in the command prompt.

## Features

- **Execute ESPTool**: Opens a command prompt and runs `esptool` with no additional arguments.
- **Execute ESP8266**: Opens a command prompt and runs `esptool` with the `--chip esp8266 erase_flash` command to erase the flash memory of an ESP8266 chip.
- **Execute ESP32**: Opens a command prompt and runs `esptool` with the `--chip esp32 erase_flash` command to erase the flash memory of an ESP32 chip.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python's standard library)
- `esptool` Python module (installable via `pip`)

## Installation

1. Clone or download this repository.
2. Install the required Python module:

    ```bash
    pip install esptool
    ```

3. Run the application:

    ```bash
    python esp-erase.py
    ```
    
## Code Explanation

### Imports

- `tkinter as tk`: Provides the GUI components.
- `messagebox` from `tkinter`: Used for displaying error messages.
- `subprocess`: Executes commands in the command prompt.

### Functions

#### `execute_esptool(command)`

Executes the `esptool` command using the command prompt. If an error occurs, it displays an error message.

### GUI Components

- **Main Window**: Created with `tk.Tk()` and titled "ESPTool GUI".
- **Buttons**:
  - **Execute ESPTool**: Runs `esptool` with no additional arguments.
  - **Execute ESP8266**: Runs `esptool` with the `--chip esp8266 erase_flash` command.
  - **Execute ESP32**: Runs `esptool` with the `--chip esp32 erase_flash` command.

### Event Loop

- The Tkinter event loop is started with `window.mainloop()`, which keeps the application running.

## Usage

1. Open the GUI application.
2. Click the "Execute ESPTool" button to run `esptool` with no arguments.
3. Click the "Execute ESP8266" button to erase the flash memory of an ESP8266 chip.
4. Click the "Execute ESP32" button to erase the flash memory of an ESP32 chip.

## Troubleshooting

- Ensure that `esptool` is installed and accessible in your system's PATH.
- If you encounter errors, make sure you have the necessary permissions and that the command prompt is correctly configured.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
