import tkinter as tk
from tkinter import ttk

class ProductCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")

        self.create_widgets()
        
    
    def create_widgets(self):
        self.create_treeview()

    def create_treeview(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.pack(padx=10, pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = ProductCRUDApp(root)
    root.mainloop()
