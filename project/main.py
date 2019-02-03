import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("GUI Audiometer")
        #main_window.iconbitmap("hear_sound.ico")
        #main_window.config(bg="red")

        ttk.Style().configure(".", font=('Helvetica', 16), justify=tk.RIGHT)

        self.notebook = ttk.Notebook(self)

        self.principal_frame = PrincipalFrame(self.notebook)
        self.notebook.add(self.principal_frame, text="Inicio")

        self.aerea_frame = AereaFrame(self.notebook)
        self.notebook.add(self.aerea_frame, text="P. Aérea")

        self.osea_frame = OseaFrame(self.notebook)
        self.notebook.add(self.osea_frame, text="P. Ósea")

        self.logo_frame = LogoFrame(self.notebook)
        self.notebook.add(self.logo_frame, text="LogoAudiometría")

        self.configuration_frame = ConfigFrame(self.notebook)
        self.notebook.add(self.configuration_frame, text="Config")

        self.calibración_frame = CalibFrame(self.notebook)
        self.notebook.add(self.calibración_frame, text="Calibración")

        self.notebook.pack(padx=5, pady=5, side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)


root = tk.Tk()
root.geometry("800x480")  # Size of the main window
ThemedStyle(root).set_theme('black')
# Themes= 'classic', 'ubuntu', 'keramik_alt',
# 'elegance', 'equilux', 'black', 'default', 'arc',
# 'radiance', 'plastik', 'aquativo', 'keramik', 'clam',
# 'winxpblue', 'clearlooks', 'kroc', 'blue', 'alt'

## root.attributes('-fullscreen',True)
app = Application(root)
app.mainloop()

#if __name__ == "__main__":
