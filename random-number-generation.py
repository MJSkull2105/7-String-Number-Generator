import tkinter as tk
import random

def generate_random_number():
    number = random.randint(1000000, 9999999)
    result_label.config(text=str(number))


window = tk.Tk()
window.title("Random")


generate_button = tk.Button(window, text="Generate", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 18))
result_label.pack(pady=20)


window.mainloop()
