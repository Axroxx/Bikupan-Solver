import tkinter as tk

class ImageButton(tk.Button):
    def __init__(self, id, master, command=None):
        self.id = id
        self.photo = tk.PhotoImage(file='images/Hex.png')
        super().__init__(master, image=self.photo, command=self.on_button_click, borderwidth=0)
        self.pack()
        self.key = ""
        self.canvas = None  # Initialize the canvas attribute as None

    def on_button_click(self):
        print(f"Button {self.id} clicked!")
        self.master.bind("<KeyPress>", self.on_key_press)

    def on_key_press(self, event):
        
        if not event.keysym.isalpha() and event.keysym.capitalize() not in ["Å","Ä","Ö"]:  # Check if the pressed key is "Esc" or "BackSpace"
            self.key = ""  # Clear the stored key
            self.photo = tk.PhotoImage(file='images/Hex.png')
            self.config(image=self.photo)
            return
        else:
            self.key = event.keysym.capitalize().strip()
        print(f"Key pressed: {self.key}")
        self.master.unbind("<KeyPress>")
        self.master.focus_set()  # Set focus back to the main window after capturing the key-press

        img = "images/" + self.key + ".png"
        self.photo = tk.PhotoImage(file=img)
        self.config(image=self.photo)  # Update the displayed image on the button

# Create the main window
win = tk.Tk()
win.title("Bikupan")
win.geometry("800x600")  # Set the initial window size (width x height)

canvas = tk.Canvas(win, width=800, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Make the window resizable in both directions
win.resizable(True, True)

# Replace 'path_to_image.png' with the actual path to your image file
image_button = ImageButton(1, win)
image_button.canvas = canvas  # Store the canvas reference in the ImageButton object

image_button.place(x=50, y=50)

# Start the main event loop
win.mainloop()
