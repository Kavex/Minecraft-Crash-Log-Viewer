import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select Minecraft Crash Log",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        process_log(file_path)

def process_log(file_path):
    try:
        with open(file_path, 'r', encoding="utf8") as file:
            content = file.read()
        # Display full log content in the text area
        text_area.config(state=tk.NORMAL)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
        apply_syntax_highlighting()
        
        # Extract crash description automatically
        crash_description = extract_crash_description(content)
        if crash_description:
            crash_label.config(text="Crash Description: " + crash_description)
        else:
            crash_label.config(text="Crash Description: Not found")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")

def extract_crash_description(content):
    # Look for a line starting with "Description:"
    for line in content.splitlines():
        if line.startswith("Description:"):
            return line.split("Description:")[1].strip()
    # Fallback: return first line that mentions 'Exception'
    for line in content.splitlines():
        if "Exception" in line:
            return line.strip()
    return None

def apply_syntax_highlighting():
    # Remove previous tags
    for tag in ["header", "time", "description", "exception", "stacktrace", "thread", "section"]:
        text_area.tag_remove(tag, "1.0", tk.END)
    
    content = text_area.get("1.0", tk.END)
    lines = content.splitlines()
    
    line_num = 1
    for line in lines:
        line_start = f"{line_num}.0"
        line_end = f"{line_num}.end"
        
        # Header lines (e.g., "---- Minecraft Crash Report ----")
        if line.startswith("----") and line.endswith("----"):
            text_area.tag_add("header", line_start, line_end)
        
        # Time lines (e.g., "Time: 2025-03-16 21:23:02")
        if line.startswith("Time:"):
            text_area.tag_add("time", line_start, line_end)
        
        # Description lines (e.g., "Description: Watching Server")
        if line.startswith("Description:"):
            text_area.tag_add("description", line_start, line_end)
        
        # Thread lines (e.g., "Thread: Server Watchdog")
        if line.startswith("Thread:") or (line.startswith('"') and "Thread" in line):
            text_area.tag_add("thread", line_start, line_end)
        
        # Section dividers (e.g., lines starting with "--")
        if line.startswith("--"):
            text_area.tag_add("section", line_start, line_end)
        
        # Exception messages (any line containing "java.lang." or "Caused by:")
        if "java.lang." in line or "Caused by:" in line:
            text_area.tag_add("exception", line_start, line_end)
        
        # Stack trace lines (lines starting with "at ")
        if line.strip().startswith("at "):
            text_area.tag_add("stacktrace", line_start, line_end)
        
        line_num += 1

    # Configure tag styles
    text_area.tag_config("header", foreground="purple", font=('TkDefaultFont', 10, 'bold'))
    text_area.tag_config("time", foreground="orange")
    text_area.tag_config("description", foreground="blue", font=('TkDefaultFont', 10, 'bold'))
    text_area.tag_config("exception", foreground="red")
    text_area.tag_config("stacktrace", foreground="green")
    text_area.tag_config("thread", foreground="brown", font=('TkDefaultFont', 10, 'italic'))
    text_area.tag_config("section", foreground="darkcyan", font=('TkDefaultFont', 10, 'bold'))

# Set up the main window
root = tk.Tk()
root.title("Minecraft Crash Log Viewer")

# Create a button to select the crash log file
select_button = tk.Button(root, text="Select Crash Log", command=select_file)
select_button.pack(pady=5)

# Label to show the extracted crash description
crash_label = tk.Label(root, text="Crash Description: ")
crash_label.pack(pady=5)

# Scrollable text widget to display the full log content
text_area = scrolledtext.ScrolledText(root, width=120, height=40)
text_area.pack(padx=10, pady=10)

root.mainloop()
