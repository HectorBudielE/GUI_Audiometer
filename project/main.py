import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import os, sys

from air_conduction_tab import AirConductionFrame
import audiogram_canvas

class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("GUI Audiometer")

        main_window.iconbitmap(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"images/hear_sound.ico"))
        main_window.config(bg="#595959")

        ttk.Style().configure(".", font=('Helvetica', 16), justify=tk.RIGHT)

        self.notebook = ttk.Notebook(self)

        self.principal_frame = PrincipalFrame(self.notebook)
        self.notebook.add(self.principal_frame, text="Start")

        self.AirConductionFrame = AirConductionFrame(self.notebook)
        self.notebook.add(self.AirConductionFrame, text="Audiogram")

        self.notebook.pack(padx=5, pady=5, side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)


class PrincipalFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.imageL = tk.PhotoImage(file=os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"images/ear_128.png"))
        self.label_image = tk.Label(self, image=self.imageL)
        self.label_image.place(x=320, y=0)

        self.label_patient_data = ttk.Label(self, text="Patient Data")
        self.label_patient_data.place(x=300, y=130)

        text_variable_name = StringVar()
        self.label_name = ttk.Label(self, text="First and Last Name")
        self.label_name.place(x=20, y=180)
        self.entry_name = ttk.Entry(self, textvariable=text_variable_name, font=('Helvetica', 16))
        self.entry_name.place(x=210, y=180)

        text_variable_age = StringVar()
        self.label_age = ttk.Label(self, text="Age")
        self.label_age.place(x=480, y=180)
        self.entry_age = ttk.Entry(self, textvariable=text_variable_age, font=('Helvetica', 16), width=4)
        self.entry_age.place(x=540, y=180)

        text_variable_address = StringVar()
        self.label_address = ttk.Label(self, text="Address")
        self.label_address.place(x=20, y=230)
        self.entry_address = ttk.Entry(self, textvariable=text_variable_address, font=('Helvetica', 16))
        self.entry_address.place(x=120, y=230)

        self.btnExit = ttk.Button(self, text='Exit', command=root.destroy, width=4)
        self.btnExit.place(x=120, y=280)


if __name__ == "__main__":

    # arduino.initiate_arduino_port()

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
