import tkinter as tk
from tkinter import ttk

class ProductCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        self.create_widgets()

    
    def create_widgets(self):
        self.create_treeview()
        self.create_input_fields()
        self.create_buttons()

    def create_treeview(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.pack(padx=10, pady=10)

    def create_input_fields(self):
        fields = [("Nombre del Producto:", 10), ("Precio:", 10), ("Stock:", 10)]
        self.entries = {}
        for label_text, width in fields:
            label = ttk.Label(self.root, text=label_text)
            label.pack(pady=(0, 5), padx=10, anchor="w")

            entry = ttk.Entry(self.root, width=width)
            entry.pack(pady=(0, 10), padx=10, fill="x")
            self.entries[label_text] = entry

    def create_buttons(self):
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        buttons = [("Agregar", lambda: print("Agregar")), 
                   ("Eliminar", lambda:print("Eliminar")),
                   ("Actualizar", lambda: print("Actualizar")), 
                   ("Buscar", lambda:print("Buscar")),
                   ("Mostrar Todo", lambda:print("Mostrar Todo"))]

        for text, command in buttons:
            button = ttk.Button(btn_frame, text=text, command=command)
            button.grid(row=0, column=buttons.index((text, command)), padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductCRUDApp(root)
    root.mainloop()
