import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

def on_button_click():
    button.pack_forget()
    label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)  # Colocar la etiqueta en una posición diferente
    label.config(text="TE AMO ", bg="red", fg="white", font=("Love Letters", 24, "bold"))

# Crear ventana principal
window = tk.Tk()
window.title("Ventana de Amor")
window.geometry("800x600")

# Cargar imagen de fondo
bg_image = Image.open("faviana.jpg")
bg_image = bg_image.resize((window.winfo_width(), window.winfo_height()), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)

# Crear etiqueta para la imagen de fondo
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_image  # Mantener referencia para que la imagen no sea recolectada por el garbage collector

# Crear botón
button = tk.Button(window, text="COSITA HERMOSA", command=on_button_click, font=("Love Letters", 28, "bold"), fg="white", bg="red", highlightbackground="white", highlightthickness=2)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear etiqueta para el mensaje
label = tk.Label(window, text="", font=("Love Letters", 24, "bold"), fg="white", bg="red")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Iniciar el bucle de la ventana
window.mainloop()
