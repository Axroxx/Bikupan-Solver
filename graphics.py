import tkinter as tk
import Image

class ImageButton(tk.Button):
    def __init__(self, id, master, command=None):
        self.id = id
        self.photo = Image.open('images/Hex.png')
        super().__init__(master, image=self.photo, command=self.on_button_click, borderwidth=0)
        self.pack()
        self.key = ""
        self.canvas = None  # Initialize the canvas attribute as None

    def on_button_click(self):
        print(f"Button {self.id} clicked!") 
        self.master.bind("<KeyPress>", self.on_key_press)

    def on_key_press(self, event):
        
        if (not event.keysym.isalpha() and event.keysym.capitalize() not in ["Adiaeresis","Aring","Odiaeresis"]) or len(event.keysym) > 1:  # Check if the pressed key is Alpha
            self.key = ""  # Clear the stored key
            self.photo = Image.open('images/Hex.png')
            self.config(image=self.photo)
            return
        else:
            self.key = event.keysym.capitalize().strip()
            print(self.key)
        print(f"Key pressed: {self.key}")
        self.master.unbind("<KeyPress>")
        self.master.focus_set()  # Set focus back to the main window after capturing the key-press

        img = "images/" + self.key + ".png"
        self.photo = tk.PhotoImage(file=img)
        self.config(image=self.photo)  # Update the displayed image on the button

# Create the main window
win = tk.Tk()
win.title("Bikupan")
win.geometry("800x1000")  # Set the initial window size (width x height)

canvas = tk.Canvas(win, width=1000, height=800, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Make the window resizable in both directions
win.resizable(True, True)

# Replace 'path_to_image.png' with the actual path to your image file

hex_buttons = []

for i in range(12):
    # Create ImageButton instances and add them to the list
    mult = 0
    if i > 3:
        mult = 1
    if i > 7:
        mult = 2
        
    hex_button = ImageButton(i+1, win, 'images/Hex.png')
    hex_button.canvas = canvas  # Store the canvas reference in the ImageButton object
    hex_button.place(x=(100+145*(i%4)), y=(50+85*mult))
    hex_buttons.append(hex_button)
    
for i in range(10):
    
    mult = 0
    if i > 4:
        mult = 1
    hex_button = ImageButton(i+1, win, 'images/Hex.png')
    hex_button.canvas = canvas  # Store the canvas reference in the ImageButton object
    hex_button.place(x=(28+145*(i%5)), y=(94+85*mult))
    hex_buttons.append(hex_button)


# Start the main event loop
win.mainloop()
