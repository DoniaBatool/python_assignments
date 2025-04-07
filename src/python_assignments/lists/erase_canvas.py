import tkinter as tk

# Canvas Configuration
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Global Variable to Track Eraser Activation
eraser_active = False  

def erase_objects(event):
    """Erase objects in contact with the eraser (if active)"""
    if eraser_active:  # Sirf tab erase kare jab eraser active ho
        x, y = event.x, event.y
        overlapping = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for obj in overlapping:
            if obj != eraser:
                canvas.itemconfig(obj, fill="white")

def toggle_eraser(event):
    """Eraser ko activate/deactivate karega"""
    global eraser_active
    eraser_active = not eraser_active  # Click par toggle hoga (ON/OFF)
    if eraser_active:
        canvas.itemconfig(eraser, fill="pink")  # Active hone par pink dikhayega
    else:
        canvas.itemconfig(eraser, fill="gray")  # Deactivate hone par gray dikhayega

# Tkinter Window Setup
root = tk.Tk()
root.title("Click to Activate Eraser")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Grid Create Karna
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")

# Eraser Create Karna (Initial Color: Gray)
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray")

def move_eraser(event):
    """Mouse move hone par eraser bhi move karega"""
    canvas.moveto(eraser, event.x, event.y)
    erase_objects(event)

# Event Bindings
canvas.bind("<Motion>", move_eraser)  # Mouse move hone par eraser move hoga
canvas.bind("<Button-1>", toggle_eraser)  # Click karne par eraser activate/deactivate hoga

root.mainloop()
