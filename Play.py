import tkinter as tk
import random
import time
import threading


def get_random_color():
    return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'

def change_background():
    canvas.configure(bg=get_random_color())
    root.after(1000, change_background)

def create_circle():
    for _ in range(10):
        size = random.randint(20, 100)
        x = random.randint(0, min(900, root.winfo_width()))
        y = random.randint(0, min(900, root.winfo_height()))
        circle = canvas.create_oval(x, y, x+size, y+size, fill=get_random_color(), outline="")
        root.after(2000, lambda c=circle: canvas.delete(c))
    root.after(1000, create_circle)


root = tk.Tk()
root.title("Вечеринка")
root.geometry("900x900")

canvas = tk.Canvas(root, width=900, height=900, highlightthickness=0)
canvas.pack(fill="both", expand=True)

#threading.Thread(target=play_music, daemon=True).start()
change_background()
create_circle()

root.mainloop()




