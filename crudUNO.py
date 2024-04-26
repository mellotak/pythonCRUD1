import tkinter as tk
from tkinter import ttk

class ProductCRUDApp:
    def __init__(self, root):
        self.root = root

# Crear una etiqueta para mostrar "Hola Mundo"
        label = ttk.Label(self.root, text="Hola Mundo")
        label.pack(padx=150, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductCRUDApp(root)
    root.mainloop()
