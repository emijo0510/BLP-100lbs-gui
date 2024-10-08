
'''
    Engineers: Emily Jones & Advika Govindarajan
    Date Created: 09/23/24
    Current Draft
'''
import tkinter as tk
import random

# Function to toggle the button's color and text when pressed
def toggle_button(button):
    current_color = button['bg']
    if current_color == 'green':
        button.config(bg='red', text='In Progress')
    else:
        button.config(bg='green', text='Start')

# Function to draw a simple line graph on a canvas
def draw_graph(canvas, data_points):
    # Clear previous drawing
    canvas.delete("all")
    
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    if len(data_points) < 2:
        return  # No graph to draw
    
    # Calculate spacing and scaling
    x_step = width / (len(data_points) - 1)
    y_max = max(data_points)
    y_min = min(data_points)
    
    # Normalize the data to fit the canvas height
    points = [(i * x_step, height - (y - y_min) / (y_max - y_min) * height) for i, y in enumerate(data_points)]
    
    # Draw the lines
    for i in range(len(points) - 1):
        canvas.create_line(points[i], points[i + 1], fill='blue', width=2)

# Function to update the graph with data from an external source
def update_graph(canvas, external_data_source):
    # Get new data points from the external array (for example, the next 10 values)
    if external_data_source and len(external_data_source) > 0:
        data_points = external_data_source.pop(0)  # Get the first set of data points
        draw_graph(canvas, data_points)
    
    # Schedule the next update
    canvas.after(2000, update_graph, canvas, external_data_source)  # Refresh every 2 seconds

# Initialize tkinter window
root = tk.Tk()
root.title("BLP GUI")
root.geometry("900x700")

# Create frames and labels for the GUI layout
def create_sensor_frame(root, label_text, external_data_source):
    frame = tk.Frame(root, padx=5, pady=5)
    frame.pack_propagate(False)
    frame.configure(width=300, height=200)
    
    status_label = tk.Label(frame, text=label_text, font=('Arial', 10))
    status_label.pack(anchor="n")
    
    state_label = tk.Label(frame, text="Good/Error", font=('Arial', 10))
    state_label.pack(anchor="w")

    psi_label = tk.Label(frame, text="PSI: 0", font=('Arial', 10))
    psi_label.pack(anchor="w")

    # Create canvas for graph
    canvas = tk.Canvas(frame, bg="white", width=250, height=100)
    canvas.pack(anchor="center", pady=10)
    
    # Start updating the graph with data from external data source
    update_graph(canvas, external_data_source)
    
    return frame

# Simulated external data source (List of arrays, each representing a new data set)
external_data = [
    [random.randint(50, 150) for _ in range(10)],
    [random.randint(60, 160) for _ in range(10)],
    [random.randint(55, 155) for _ in range(10)],
    [random.randint(65, 165) for _ in range(10)],
    [random.randint(50, 150) for _ in range(10)]
]

# Top-left thrust and temp sections
thrust_frame = create_sensor_frame(root, "Thrust", external_data.copy())  # Pass a copy of the external data
thrust_frame.grid(row=0, column=0)

temp_frame = create_sensor_frame(root, "Temp", external_data.copy())  # Pass a copy of the external data
temp_frame.grid(row=0, column=1)

# Pressure sections
pressure1_frame = create_sensor_frame(root, "Pressure 1", external_data.copy())
pressure1_frame.grid(row=0, column=2)

pressure2_frame = create_sensor_frame(root, "Pressure 2", external_data.copy())
pressure2_frame.grid(row=1, column=0)

pressure3_frame = create_sensor_frame(root, "Pressure 3", external_data.copy())
pressure3_frame.grid(row=1, column=1)

pressure4_frame = create_sensor_frame(root, "Pressure 4", external_data.copy())
pressure4_frame.grid(row=1, column=2)

pressure5_frame = create_sensor_frame(root, "Pressure 5", external_data.copy())
pressure5_frame.grid(row=2, column=1)

# Start and Abort buttons
start_button = tk.Button(root, text="Start", bg="green", fg="white", width=10, height=2,
                         command=lambda: toggle_button(start_button))
start_button.grid(row=4, column=0, pady=10, columnspan=2)

abort_button = tk.Button(root, text="Abort", bg="red", fg="white", width=10, height=2)
abort_button.grid(row=4, column=1, pady=10, columnspan=2)

# FV and OV buttons
fv04_button = tk.Button(root, text="FV-04", width=10, height=2)
fv04_button.grid(row=5, column=0, padx=10)

ov04_button = tk.Button(root, text="OV-04", width=10, height=2)
ov04_button.grid(row=5, column=1, padx=10)

fv02_button = tk.Button(root, text="FV-02", width=10, height=2)
fv02_button.grid(row=6, column=0, padx=10)

ov02_button = tk.Button(root, text="OV-02", width=10, height=2)
ov02_button.grid(row=6, column=1, padx=10)

# Spark time and Burn time entries
spark_time_label = tk.Label(root, text="Spark time", font=('Arial', 10))
spark_time_label.grid(row=7, column=0, pady=5)
spark_time_entry = tk.Entry(root, width=10)
spark_time_entry.grid(row=8, column=0)

burn_time_label = tk.Label(root, text="Burn time", font=('Arial', 10))
burn_time_label.grid(row=7, column=1, pady=5)
burn_time_entry = tk.Entry(root, width=10)
burn_time_entry.grid(row=8, column=1)

# Record Data, HITL, and Coil buttons
record_button = tk.Button(root, text="Record Data", width=10, height=2)
record_button.grid(row=5, column=2, padx=10)

hitl_button = tk.Button(root, text="HITL", width=10, height=2)
hitl_button.grid(row=6, column=2, padx=10)

coil_button = tk.Button(root, text="Coil", width=10, height=2)
coil_button.grid(row=7, column=2, padx=10)

# Add refresh rate/time placeholder
refresh_label = tk.Label(root, text="refresh rate / time", font=('Arial', 10))
refresh_label.grid(row=0, column=4)

# Run the tkinter main loop
root.mainloop()