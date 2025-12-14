# Multi-Clipboard Manager

## Overview
A lightweight, Python-based CLI tool designed to extend the system clipboard functionality. It allows users to save multiple items to a persistent storage (JSON) and easily retrieve them by keyword, solving the limitation of the standard single-item clipboard. 

This project demonstrates the use of file I/O, JSON serialization, and system clipboard integration in Python.

## Features
- **Save to Clipboard**: Store the current clipboard content under a custom keyword.
- **Load from Clipboard**: Retrieve saved text and copy it back to the system clipboard instantly.
- **List All Items**: View all currently saved keywords and their associated data.
- **Persistent Storage**: Data is saved to a local `data.json` file, ensuring it's available across sessions.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: 
  - `clipboard` (for system clipboard interaction)
  - `json` (for data persistence)
  - `sys` (for command-line argument parsing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EmmanuelDumitrache/multiclipboard-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd multiclipboard-python
   ```
3. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install clipboard
   ```

## Usage

Run the script from the terminal with one of the following commands:

**Save current clipboard content:**
```bash
python multiclipboard.py save <keyword>
```

**Load content to clipboard:**
```bash
python multiclipboard.py load <keyword>
```

**List all saved items:**
```bash
python multiclipboard.py list
```

### Interactive Mode
You can also run the commands without arguments to be prompted for input:
```bash
python multiclipboard.py save
# Prompts for key
```
```bash
python multiclipboard.py load
# Prompts for key
```

## Future Improvements
- Add encryption for sensitive data.
- Implement a graphical user interface (GUI) or system tray icon.
- Support for non-text data formats (images, files).
