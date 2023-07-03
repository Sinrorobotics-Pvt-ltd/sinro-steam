import tkinter as tk
from tkinter import messagebox


def calculate_area():
    shape = shape_var.get()
    
    if shape == "Square":
        side_length = float(side_entry.get())
        area = side_length ** 2
        result_label.config(text="The area is: {:.2f}".format(area))
    
    elif shape == "Rectangle":
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        result_label.config(text="The area is: {:.2f}".format(area))
    
    elif shape == "Circle":
        radius = float(radius_entry.get())
        area = 3.14159 * (radius ** 2)
        result_label.config(text="The area is: {:.2f}".format(area))
    
    elif shape == "Triangle":
        base = float(base_entry.get())
        height = float(height_entry.get())
        area = 0.5 * base * height
        result_label.config(text="The area is: {:.2f}".format(area))
    
    else:
        messagebox.showerror("Error", "Invalid shape entered.")
        result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Area Calculator")

# Create the shape selection dropdown
shape_var = tk.StringVar()
shape_label = tk.Label(window, text="Select a shape:")
shape_label.pack()
shape_dropdown = tk.OptionMenu(window, shape_var, "Square", "Rectangle", "Circle", "Triangle")
shape_dropdown.pack()

# Create input fields for the respective shape dimensions
side_label = tk.Label(window, text="Side Length:")
side_label.pack()
side_entry = tk.Entry(window)
side_entry.pack()

length_label = tk.Label(window, text="Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

width_label = tk.Label(window, text="Width:")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

radius_label = tk.Label(window, text="Radius:")
radius_label.pack()
radius_entry = tk.Entry(window)
radius_entry.pack()

base_label = tk.Label(window, text="Base:")
base_label.pack()
base_entry = tk.Entry(window)
base_entry.pack()

height_label = tk.Label(window, text="Height:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create the button to calculate the area
calculate_button = tk.Button(window, text="Calculate", command=calculate_area)
calculate_button.pack()

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main event loop
window.mainloop()
