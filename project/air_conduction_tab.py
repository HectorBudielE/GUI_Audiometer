import tkinter as tk
from tkinter import ttk
from canvas_file import FigureCanvas
import os, sys

class AirConductionFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Frequency List
        self.list_freq = ['125 Hz', '250 Hz', '500 Hz', '750 Hz', '1000 Hz', '1500 Hz', '2000 Hz', '3000 Hz', '4000 Hz',
                          '6000 Hz', '8000 Hz']
        self.list_freq2 = [125,250,500,750,1000,1500,2000,3000,4000,6000,8000]

        # List for 125 Hz [0]
        self.list_a125 = ['-10 dB HL', '-5 dB HL', '0 dB HL', '5 dB HL', '10 dB HL', '15 dB HL', '20 dB HL', '25 dB HL',
                         '30 dB HL', '35 dB HL', '40 dB HL', '45 dB HL',
                         '50 dB HL', '55 dB HL', '60 dB HL', '65 dB HL', '70 dB HL'] #17
        # List for 250 and 8000 Hz [1][10]
        self.list_a250 = ['-10 dB HL', '-5 dB HL', '0 dB HL', '5 dB HL', '10 dB HL', '15 dB HL', '20 dB HL', '25 dB HL',
                         '30 dB HL', '35 dB HL', '40 dB HL', '45 dB HL',
                         '50 dB HL', '55 dB HL', '60 dB HL', '65 dB HL', '70 dB HL', '75 dB HL', '80 dB HL', '85 dB HL',
                         '90 dB HL',
                         '95 dB HL', '100 dB HL'] #23
        # List for 6000 Hz [9]
        self.list_a6000 = ['-10 dB HL', '-5 dB HL', '0 dB HL', '5 dB HL', '10 dB HL', '15 dB HL', '20 dB HL', '25 dB HL',
                          '30 dB HL', '35 dB HL', '40 dB HL', '45 dB HL',
                          '50 dB HL', '55 dB HL', '60 dB HL', '65 dB HL', '70 dB HL', '75 dB HL', '80 dB HL',
                          '85 dB HL', '90 dB HL',
                          '95 dB HL', '100 dB HL', '105 dB HL', '110 dB HL'] #25
        # List for 500 Hz to 4000 Hz [2][3][4][5][6][7][8]
        self.list_a4000 = ['-10 dB HL', '-5 dB HL', '0 dB HL', '5 dB HL', '10 dB HL', '15 dB HL', '20 dB HL', '25 dB HL',
                          '30 dB HL', '35 dB HL', '40 dB HL', '45 dB HL',
                          '50 dB HL', '55 dB HL', '60 dB HL', '65 dB HL', '70 dB HL', '75 dB HL', '80 dB HL',
                          '85 dB HL', '90 dB HL',
                          '95 dB HL', '100 dB HL', '105 dB HL', '110 dB HL', '115 dB HL', '120 dB HL'] #27

        self.list_a = []
        self.aten = 0

        # Frequency and gain (atenuation) variables initialization
        self.freq_value = 0
        self.aten_value = 0
        self.list_a = self.list_a125

        # Ear variables initialization
        self.ear = 0  # 0->Right Ear, 1->Left Ear
        self.masking = 0  # 0->Masking off, 1->Masking on
        self.start = 0 # 0->Signal ON, 1->Signal OFF


        ttk.Style().configure("myblue.TButton", padding=(10, 10, 3, 10), foreground="#0000ff", justify=tk.CENTER)
        ttk.Style().configure("myblue2.TButton", padding=(10, 10, 3, 10), background="#0000ff", justify=tk.CENTER)
        ttk.Style().configure("myred.TButton", padding=(10, 10, 3, 10), foreground="#ff0000", justify=tk.CENTER)
        ttk.Style().configure("myred2.TButton", padding=(10, 10, 3, 10), background="#ff0000", justify=tk.CENTER)
        ttk.Style().configure("masking_on.TButton", background="#909090", justify=tk.CENTER)
        ttk.Style().configure("masking_off.TButton", background="#404040", justify=tk.CENTER)
        ttk.Style().configure("start.TButton", anchor="center", justify=tk.CENTER)
        ttk.Style().configure("start_right.TButton", anchor="center", justify=tk.CENTER, background="#ff0000")
        ttk.Style().configure("start_left.TButton", anchor="center", justify=tk.CENTER, background="#0000ff")

        # Creation of canvas
        self.canvas = FigureCanvas(self, width=350, height=200)
        self.canvas.grid(row=0, column=0, rowspan=7, padx=10, pady=10)

        # Cursor in the canvas
        self.cursor1 = self.canvas.create_line(5, 5, 5, 5, fill="#ffffff", width=2, tags="cursor1")
        self.cursor2 = self.canvas.create_line(5, 5, 5, 5, fill="#ffffff", width=2, tags="cursor1")

        # Row 0
        self.right_ear_label = ttk.Label(self, text="Right")
        self.right_ear_label.grid(row=0, column=1, padx=0)

        self.left_ear_label = ttk.Label(self, text="Left")
        self.left_ear_label.grid(row=0, column=3, padx=0)

        # Row 1
        self.right_button = ttk.Button(self, text="R", width="2", style="myred2.TButton", command=self.right_ear)
        self.right_button.grid(row=1, column=1, padx=0)

        self.decrease_dB_button = ttk.Button(self, text="-5dB", width="5", padding=(10, 10, 4, 10), command=self.dec_5dB)
        self.decrease_dB_button.grid(row=1, column=2, padx=0)
        #self.decrease_dB_button['state'] = DISABLED

        self.left_button = ttk.Button(self, text=" L", width="2", style="myblue.TButton", command=self.left_ear)
        self.left_button.grid(row=1, column=3, padx=0)

        # Row 2
        self.decrease_button = ttk.Button(self, text="- F", width="4", padding=(10, 10, 3, 10), command=self.dec_freq)
        self.decrease_button.grid(row=2, column=1)
        #self.decrease_button['state'] = DISABLED

        self.play_button = ttk.Button(self, text=self.list_freq[self.freq_value] + "\n" + self.list_a[self.aten_value],
                                      style="start.TButton", width="8", padding=(10, 20, 10, 20), command=self.start)
        self.play_button.grid(row=2, column=2)

        self.cursor1 = self.canvas.create_line(self.canvas.dict_cursorX['125 Hz'] - 5,
                                               self.canvas.dict_cursorY['-10 dB HL'],
                                               self.canvas.dict_cursorX['125 Hz'] + 5,
                                               self.canvas.dict_cursorY['-10 dB HL'],
                                               fill="#000000", width=2, tags="cursor1")
        self.cursor2 = self.canvas.create_line(self.canvas.dict_cursorX['125 Hz'],
                                               self.canvas.dict_cursorY['-10 dB HL'] - 5,
                                               self.canvas.dict_cursorX['125 Hz'],
                                               self.canvas.dict_cursorY['-10 dB HL'] + 5,
                                               fill="#000000", width=2, tags="cursor1")

        self.increase_button = ttk.Button(self, text="+ F", width="4", padding=(10, 10, 3, 10), command=self.inc_freq)
        self.increase_button.grid(row=2, column=3)

        # Row 3
        self.signal_button = ttk.Button(self, text="S", width=2, padding=(10, 10, 3, 10), command=self.open)
        self.signal_button.grid(row=3, column=1, pady=0)

        self.increase_dB_button = ttk.Button(self, text="+5dB", width="5", padding=(10, 10, 4, 10), command=self.inc_5dB)
        self.increase_dB_button.grid(row=3, column=2, pady=0)

        self.masking_button = ttk.Button(self, text="M", width="2", padding=(10, 10, 3, 10), command=self.masking)
        self.masking_button.grid(row=3, column=3, pady=0)

        # Row 4
        self.mark_button = ttk.Button(self, text=" X ", width="4", padding=(10, 10, 4, 10), command=self.mark)
        self.mark_button.grid(row=4, column=1, pady=0)

        self.img_basket = tk.PhotoImage(file=os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"images/basket.png"))
        self.clean_button = ttk.Button(self, image=self.img_basket, padding=(6, 6, 6, 6), command=self.erase_marker)
        self.clean_button.grid(row=4, column=2, pady=0)

        self.img_export = tk.PhotoImage(file=os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),"images/export.png"))
        self.generate_button = ttk.Button(self, image=self.img_export, padding=(6, 6, 6, 6), command=self.generate_pdf)
        self.generate_button.grid(row=4, column=3, pady=0)


    def start(self):
        pass

    def left_ear(self):
        pass

    def right_ear(self):
        pass

    def masking(self):
        # Include action for Masking button
        pass

    def call_freq(self, *args):
        pass

    def call_dB(self, *args):
        pass

    def inc_5dB(self):
        pass

    def dec_5dB(self):
        pass

    def inc_freq(self):
        pass

    def dec_freq(self):
        pass

    def mark(self):
        pass

    def right_marker_no_masking(self):
        pass

    def right_marker_masking(self):
        pass

    def left_marker_no_masking(self):
        pass

    def left_marker_masking(self):
        pass

    def erase_marker(self):
        pass

    def open(self):
        pass

    def generate_pdf(self):
        pass
