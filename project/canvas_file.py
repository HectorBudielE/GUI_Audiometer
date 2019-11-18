import tkinter as tk

class FigureCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #x = 40  # sets the origin of the table as (x,x)
        self.config(bg="#ffffff")
        x=40
        col=60 # width of the column
        row=26 # height of the row

        # Dictionary for the frequency location (x) of the cursor
        self.dict_cursorX = {'125 Hz': x + 10, '250 Hz': x + 10 + col, '500 Hz': x + 10 + (2 * col),
                            '750 Hz': x + 10 + (2.5 * col), '1000 Hz': x + 10 + (3 * col),
                            '1500 Hz': x + 10 + (2.5 * col) + col, '2000 Hz': x + 10 + (4 * col),
                            '3000 Hz': x + 10 + (2.5 * col) + (2 * col), '4000 Hz': x + 10 + (5 * col),
                            '6000 Hz': x + 10 + (2.5 * col) + (3 * col), '8000 Hz': x + 10 + (6 * col)}
        # Dictionary for the dB location (y) of the cursor
        self.dict_cursorY = {'-10 dB HL': x + 10, '-5 dB HL': x + 10 + (row / 2), '0 dB HL': x + 10 + row,
                            '5 dB HL': x + 10 + (3 * row / 2), '10 dB HL': x + 10 + (4 * row / 2),
                            '15 dB HL': x + 10 + (5 * row / 2), '20 dB HL': x + 10 + (3 * row),
                            '25 dB HL': x + 10 + (7 * row / 2),
                            '30 dB HL': x + 10 + (4 * row), '35 dB HL': x + 10 + (9 * row / 2),
                            '40 dB HL': x + 10 + (5 * row), '45 dB HL': x + 10 + (11 * row / 2),
                            '50 dB HL': x + 10 + (6 * row), '55 dB HL': x + 10 + (13 * row / 2),
                            '60 dB HL': x + 10 + (7 * row),
                            '65 dB HL': x + 10 + (15 * row / 2), '70 dB HL': x + 10 + (8 * row),
                            '75 dB HL': x + 10 + (17 * row / 2), '80 dB HL': x + 10 + (9 * row),
                            '85 dB HL': x + 10 + (19 * row / 2), '90 dB HL': x + 10 + (10 * row),
                            '95 dB HL': x + 10 + (21 * row / 2), '100 dB HL': x + 10 + (11 * row),
                            '105 dB HL': x + 10 + (23 * row / 2), '110 dB HL': x + 10 + (12 * row),
                            '115 dB HL': x + 10 + (25 * row / 2), '120 dB HL': x + 10 + (13 * row)}

        # Dictionary for the index location of the color markers
        self.dict_markerR={'125 Hz': "Rmark125", '250 Hz': "Rmark250", '500 Hz': "Rmark500",
                          '750 Hz': "Rmark750", '1000 Hz': "Rmark1000", '1500 Hz': "Rmark1500",
                          '2000 Hz': "Rmark2000", '3000 Hz': "Rmark3000", '4000 Hz': "Rmark4000",
                          '6000 Hz': "Rmark6000", '8000 Hz': "Rmark8000"}
        self.dict_markerL={'125 Hz': "Lmark125", '250 Hz': "Lmark250", '500 Hz': "Lmark500",
                          '750 Hz': "Lmark750", '1000 Hz': "Lmark1000", '1500 Hz': "Lmark1500",
                          '2000 Hz': "Lmark2000", '3000 Hz': "Lmark3000", '4000 Hz': "Lmark4000",
                          '6000 Hz': "Lmark6000", '8000 Hz': "Lmark8000"}

        # Creating color rectangles
        self.create_rectangle(x, x + 10 + (3*row), x + 20 + (6*col), x + 20 + (5*row),
                             fill="#ffffcc", width=0)
        self.create_rectangle(x, x + 10 + (5*row), x + 20 + (6*col), x + 20 + (8*row),
                             fill="#ccccff", width=0)
        self.create_rectangle(x, x + 10 + (8*row), x + 20 + (6*col), x + 20 +(10*row),
                             fill="#ffcccc", width=0)
        self.create_rectangle(x, x + 10 +(10*row), x + 20 + (6*col), x + 20 +(13*row),
                             fill="#ffb3b3", width=0)

        # Creating columns
        self.create_line(x, x, x, x + 20 + (13*row), fill="#808080")
        for i in range(0, 7):
            self.create_line(x + 10 + (i*col), x, x + 10 + (i*col), x + 20 + (13*row), fill="#808080")
        for i in range(0, 4):
            self.create_line(x + 10 +(2.5*col) + (i*col), x, x + 10 + (2.5*col) + (i*col),
                             x + 20 + (13*row), fill="#808080")
        self.create_line(x + 20 + (6*col), x, x + 20 + (6*col), x + 20 + (13*row), fill="#808080")
        # Creating rows
        self.create_line(x, x, x + 20 + (6*col), x, fill="#808080")
        for i in range(0, 14):
            self.create_line(x, x + 10 + (i*row), x + 20 + (6*col), x + 10 + (i*row), fill="#808080")
        self.create_line(x, x + 20 + (13*row), x + 20 + (6*col), x + 20 + (13*row), fill="#808080")

        self.configure(width=70 + (6*col), height=70 + (13*row))

        # Creating the texts inside the Canvas
        self.create_text(x + 10 +  (0*col), x - 10, text="125", font=('Helvetica', 9))
        self.create_text(x + 10 +  (1*col), x - 10, text="250", font=('Helvetica', 9))
        self.create_text(x + 10 +  (2*col), x - 10, text="500", font=('Helvetica', 9))
        self.create_text(x + 10 +(2.5*col), x - 10, text="750", font=('Helvetica', 9))
        self.create_text(x + 10 +  (3*col), x - 10, text= "1K", font=('Helvetica', 9))
        self.create_text(x + 10 +(3.5*col), x - 10, text="1K5", font=('Helvetica', 9))
        self.create_text(x + 10 +  (4*col), x - 10, text= "2K", font=('Helvetica', 9))
        self.create_text(x + 10 +(4.5*col), x - 10, text= "3K", font=('Helvetica', 9))
        self.create_text(x + 10 +  (5*col), x - 10, text= "4K", font=('Helvetica', 9))
        self.create_text(x + 10 +(5.5*col), x - 10, text= "6K", font=('Helvetica', 9))
        self.create_text(x + 10 +  (6*col), x - 10, text= "8K", font=('Helvetica', 9))

        self.create_text(x - 5, x + 10 + (0*row), text="-10", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (1*row), text=  "0", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (2*row), text= "10", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (3*row), text= "20", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (4*row), text= "30", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (5*row), text= "40", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (6*row), text= "50", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (7*row), text= "60", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (8*row), text= "70", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (9*row), text= "80", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 +(10*row), text= "90", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 +(11*row), text="100", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 +(12*row), text="110", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 +(13*row), text="120", font=('Helvetica', 9), anchor='e')

        self.create_text(x+3*col, x-15, text="Frecuencias", font=('Helvetica', 9), anchor='s')

        self.create_text(x - 30, x + 10 + (5 * row), text="dB HL", font=('Helvetica', 9), anchor='e',angle=90)
