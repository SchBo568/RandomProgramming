import tkinter as tk
from tkinter import ttk  # Import the ttk submodule for Combobox
from datetime import datetime, timedelta

# Define timezone offsets in hours (without considering daylight saving time changes)
timezone_offsets = {
    "ET": -4,  # Eastern Time (ET) UTC-4
    "CET": 2,  # Central European Time (CET) UTC+2
    # Add more timezones and offsets as needed
}

def convert_time_to_timezone(source_time, source_timezone, target_timezone):
    source_time = datetime.strptime(source_time, "%I:%M %p")
    source_offset = timedelta(hours=timezone_offsets[source_timezone])
    target_offset = timedelta(hours=timezone_offsets[target_timezone])
    time_difference = target_offset - source_offset
    target_time = source_time + time_difference
    target_time_str = target_time.strftime("%H:%M")
    return target_time_str

def convert_button_click():
    input_time = input_time_entry.get()
    source_timezone = source_timezone_combobox.get()
    target_timezone = target_timezone_combobox.get()
    converted_time = convert_time_to_timezone(input_time, source_timezone, target_timezone)
    result_label.config(text=f"The converted time for {target_timezone} is: {converted_time}")

# Create the main window
root = tk.Tk()
root.title("Time Converter")

# Create widgets
input_time_label = tk.Label(root, text="Enter the time (HH:MM AM/PM):")
input_time_entry = tk.Entry(root)

source_timezone_label = tk.Label(root, text="Source Timezone:")
source_timezone_combobox = ttk.Combobox(root, values=list(timezone_offsets.keys()))  # Use ttk.Combobox

target_timezone_label = tk.Label(root, text="Target Timezone:")
target_timezone_combobox = ttk.Combobox(root, values=list(timezone_offsets.keys()))  # Use ttk.Combobox

convert_button = tk.Button(root, text="Convert", command=convert_button_click)
result_label = tk.Label(root, text="")

# Place widgets on the grid
input_time_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_time_entry.grid(row=0, column=1, padx=10, pady=5)

source_timezone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
source_timezone_combobox.grid(row=1, column=1, padx=10, pady=5)

target_timezone_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
target_timezone_combobox.grid(row=2, column=1, padx=10, pady=5)

convert_button.grid(row=3, columnspan=2, pady=10)
result_label.grid(row=4, columnspan=2, pady=5)

# Start the main loop
root.mainloop()
