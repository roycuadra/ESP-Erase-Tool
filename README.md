# ESP Erase Tool GUI

This Python application provides a graphical user interface (GUI) for executing commands with esptool to erase flash memory.

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
