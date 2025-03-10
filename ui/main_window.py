import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Aplicação")
        self.geometry("300x200")
        
        # Adicionando widgets
        self.label = tk.Label(self, text="Olá, Mundo!")
        self.label.pack(pady=20)
        
        self.button = tk.Button(self, text="Clique aqui", command=self.on_click)
        self.button.pack()

    def on_click(self):
        self.label.config(text="Você clicou no botão!")

