![image](https://github.com/user-attachments/assets/241908ba-2948-49a7-bccc-69457d21177e)


# Minecraft Crash Log Viewer 

A simple Python GUI tool built with Tkinter for reading and analyzing Minecraft crash logs. This tool allows you to select a crash log file from your computer, view its contents in a scrollable text area, and automatically highlights key elements of the log to help you quickly identify issues.

## Features

- **File Selection:** Easily choose a Minecraft crash log file using a file dialog.
- **Automatic Syntax Highlighting:** 
  - Header dividers (e.g., "---- Minecraft Crash Report ----") are highlighted in purple.
  - Time lines (e.g., "Time: 2025-03-16 21:23:02") are highlighted in orange.
  - Description lines (e.g., "Description: Watching Server") are highlighted in blue.
  - Exception messages (lines containing "java.lang." or "Caused by:") are highlighted in red.
  - Stack trace lines (lines starting with "at ") are highlighted in green.
  - Thread and section lines are also specially formatted.
- **Crash Description Extraction:** Automatically extracts and displays the crash description from the log.

## Requirements

- Python 3.x
- Tkinter (usually bundled with Python)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed on your system.
3. No additional libraries are required since Tkinter comes with Python.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:

   ```bash
   python MinecraftCrashViewer.py
