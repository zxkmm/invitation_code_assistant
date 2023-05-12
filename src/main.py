import tkinter as tk
import os

gui_width = 180
gui_height = 80

gui_color = "#FFFFFF"
gui_text_color = "#000000"

gui_title = "invitation_code_assistant"
prev_button_text = "<"
next_button_text = "          >          "
go_button_text = "Go"

# get the dir which this script is in
script_dir = os.path.dirname(os.path.abspath(__file__))

# GUI
root = tk.Tk()
root.title(gui_title)
root.configure(bg=gui_color)
root.attributes("-topmost", True)
root.geometry(f"{gui_width}x{gui_height}+{root.winfo_screenwidth() - gui_width}+0")

# -1 is for making sure the first line to be selected
line_counter = -1
total_lines = 0
lines = []

def update_label():
    label_text = f"{line_counter + 1}/{total_lines}"
    label.config(text=label_text)

def on_button_click(offset):
    global line_counter

    next_line = (line_counter + offset) % total_lines
# next line and text
    line_counter = next_line
    next_line_text = lines[line_counter].strip()
    root.clipboard_clear()
    root.clipboard_append(next_line_text)

    update_label()

def on_go_button_click():
    global line_counter
    new_line_number = int(textbox.get())

    if 1 <= new_line_number <= total_lines:
        line_counter = new_line_number - 1
        next_line_text = lines[line_counter].strip()
        root.clipboard_clear()
        root.clipboard_append(next_line_text)

        update_label()

go_button_frame = tk.Frame(root, bg=gui_color)
go_button_frame.pack(side="bottom", fill="y")

textbox = tk.Entry(go_button_frame)
textbox.pack(side="left")

go_button = tk.Button(go_button_frame, text=go_button_text, command=on_go_button_click, bg=gui_color, fg=gui_text_color)
go_button.pack(side="left")

button_frame = tk.Frame(root, bg=gui_color)
button_frame.pack(side="top", fill="x")

prev_button = tk.Button(button_frame, text=prev_button_text, command=lambda: on_button_click(-1), bg=gui_color, fg=gui_text_color)
prev_button.pack(side="left", expand=True)

next_button = tk.Button(button_frame, text=next_button_text, command=lambda: on_button_click(1), bg=gui_color, fg=gui_text_color)
next_button.pack(side="left", expand=True)

label_frame = tk.Frame(root, bg=gui_color)
label_frame.pack(side="top", fill="x")

label = tk.Label(label_frame, text="0/0", bg=gui_color, fg=gui_text_color)
label.pack(expand=True)

text_file_path = os.path.join(script_dir, "list.txt")
with open(text_file_path, "r") as f:
    lines = f.readlines()
total_lines = len(lines)

update_label()

root.mainloop()

