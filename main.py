from ui.main_window import MainWindow
from config import load_config

def main():
    # Carrega config
    config = load_config()

    # Acessa as configurações
    origin_path = config["origin_path"]
    save_path = config["save_path"]

    # Interface
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
