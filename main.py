import customtkinter as ctk

class ResumeEditor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Resume Editor")
        self.geometry("800x600")

        # Exemplo de botão para upload
        self.upload_button = ctk.CTkButton(self, text="Upload Resume", command=self.upload_resume)
        self.upload_button.pack(pady=10)

    def upload_resume(self):
        print("Upload clicked")

if __name__ == "__main__":
    app = ResumeEditor()
    app.mainloop()
