import tkinter as tk
from tkinter import ttk

class AirConductionFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ttk.Style().configure("myblue.TButton", padding=(10, 10, 3, 10), foreground="#0000ff", justify=tk.CENTER)
        ttk.Style().configure("myblue2.TButton", padding=(10, 10, 3, 10), background="#0000ff", justify=tk.CENTER)
        ttk.Style().configure("myred.TButton", padding=(10, 10, 3, 10), foreground="#ff0000", justify=tk.CENTER)
        ttk.Style().configure("myred2.TButton", padding=(10, 10, 3, 10), background="#ff0000", justify=tk.CENTER)
        ttk.Style().configure("masking_on.TButton", background="#909090", justify=tk.CENTER)
        ttk.Style().configure("masking_off.TButton", background="#404040", justify=tk.CENTER)

        # Creation of canvas
        #self.canvas = FigureCanvas(self, width=350, height=200)
        #self.canvas.grid(row=0, column=0, rowspan=7, padx=10, pady=10)
