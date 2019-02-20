import tkinter as tk

class FigureCanvas(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        x = 40  # sets the origin of the table as (x,x)
        self.config(bg="#ffffff")

        col = 60  # width of the column
        row = 26  # height of the row
        # dictionary for the frequency location (x) of the cursor
        self.DictCursorX = {'125 Hz': x + 10, '250 Hz': x + 10 + col, '500 Hz': x + 10 + (2 * col),
                            '750 Hz': x + 10 + (2.5 * col), '1000 Hz': x + 10 + (3 * col),
                            '1500 Hz': x + 10 + (2.5 * col) + col, '2000 Hz': x + 10 + (4 * col),
                            '3000 Hz': x + 10 + (2.5 * col) + (2 * col), '4000 Hz': x + 10 + (5 * col),
                            '6000 Hz': x + 10 + (2.5 * col) + (3 * col), '8000 Hz': x + 10 + (6 * col)}
        # dictionary for the dB location (y) of the cursor
        self.DictCursorY = {'-10 dB HL': x + 10, '-5 dB HL': x + 10 + (row / 2), '0 dB HL': x + 10 + row,
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

        # dictionary for the index location of the color markers
        self.DictMarcadorD = {'125 Hz': "Dmarc125", '250 Hz': "Dmarc250", '500 Hz': "Dmarc500", '750 Hz': "Dmarc750",
                              '1000 Hz': "Dmarc1000", '1500 Hz': "Dmarc1500", '2000 Hz': "Dmarc2000",
                              '3000 Hz': "Dmarc3000",
                              '4000 Hz': "Dmarc4000", '6000 Hz': "Dmarc6000", '8000 Hz': "Dmarc8000"}

        self.DictMarcadorI = {'125 Hz': "Imarc125", '250 Hz': "Imarc250", '500 Hz': "Imarc500", '750 Hz': "Imarc750",
                              '1000 Hz': "Imarc1000", '1500 Hz': "Imarc1500", '2000 Hz': "Imarc2000",
                              '3000 Hz': "Imarc3000",
                              '4000 Hz': "Imarc4000", '6000 Hz': "Imarc6000", '8000 Hz': "Imarc8000"}

        # creating color rectangles
        self.create_rectangle(x, x + 10 + (3 * row), x + 20 + (6 * col), x + 20 + (5 * row), fill="#ffffcc",
                              width=0)
        self.create_rectangle(x, x + 10 + (5 * row), x + 20 + (6 * col), x + 20 + (8 * row), fill="#ccccff",
                              width=0)
        self.create_rectangle(x, x + 10 + (8 * row), x + 20 + (6 * col), x + 20 + (10 * row), fill="#ffcccc",
                              width=0)
        self.create_rectangle(x, x + 10 + (10 * row), x + 20 + (6 * col), x + 20 + (13 * row), fill="#ffb3b3",
                              width=0)

        # creating columns
        self.create_line(x, x, x, x + 20 + (13 * row), fill="#808080")
        for i in range(0, 7):
            self.create_line(x + 10 + (i * col), x, x + 10 + (i * col), x + 20 + (13 * row), fill="#808080")
        for i in range(0, 4):
            self.create_line(x + 10 + (2.5 * col) + (i * col), x, x + 10 + (2.5 * col) + (i * col),
                             x + 20 + (13 * row), fill="#808080")
        self.create_line(x + 20 + (6 * col), x, x + 20 + (6 * col), x + 20 + (13 * row), fill="#808080")
        # creating rows
        self.create_line(x, x, x + 20 + (6 * col), x, fill="#808080")
        for i in range(0, 14):
            self.create_line(x, x + 10 + (i * row), x + 20 + (6 * col), x + 10 + (i * row), fill="#808080")
        self.create_line(x, x + 20 + (13 * row), x + 20 + (6 * col), x + 20 + (13 * row), fill="#808080")

        self.configure(width=70 + (6 * col), height=70 + (13 * row))

        # creating the texts inside the canvas
        self.create_text(x + 10, x - 10, text="125", font=('Helvetica', 9))
        self.create_text(x + 10 + (1 * col), x - 10, text="250", font=('Helvetica', 9))
        self.create_text(x + 10 + (2 * col), x - 10, text="500", font=('Helvetica', 9))
        self.create_text(x + 10 + (2.5 * col), x - 10, text="750", font=('Helvetica', 9))
        self.create_text(x + 10 + (3 * col), x - 10, text="1K", font=('Helvetica', 9))
        self.create_text(x + 10 + (3.5 * col), x - 10, text="1K5", font=('Helvetica', 9))
        self.create_text(x + 10 + (4 * col), x - 10, text="2K", font=('Helvetica', 9))
        self.create_text(x + 10 + (4.5 * col), x - 10, text="3K", font=('Helvetica', 9))
        self.create_text(x + 10 + (5 * col), x - 10, text="4K", font=('Helvetica', 9))
        self.create_text(x + 10 + (5.5 * col), x - 10, text="6K", font=('Helvetica', 9))
        self.create_text(x + 10 + (6 * col), x - 10, text="8K", font=('Helvetica', 9))

        self.create_text(x - 5, x + 10 + (0 * row), text="-10", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (1 * row), text="0", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (2 * row), text="10", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (3 * row), text="20", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (4 * row), text="30", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (5 * row), text="40", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (6 * row), text="50", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (7 * row), text="60", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (8 * row), text="70", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (9 * row), text="80", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (10 * row), text="90", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (11 * row), text="100", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (12 * row), text="110", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (13 * row), text="120", font=('Helvetica', 9), anchor='e')

        self.create_text(x+3*col, x-15, text="Frecuencias", font=('Helvetica', 9), anchor='s')

        self.create_text(x - 30, x + 10 + (5 * row), text="dB HL", font=('Helvetica', 9), anchor='e',angle=90)


class FigureCanvas2(tk.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        x = 35  # sets the origin of the table as (x,x)
        self.config(bg="#ffffff")

        col = 40  # width of the column
        row = 25  # height of the row

        # dictionary for the frequency location (x) of the cursor
        self.DictCursorX = {'0': x + 10, '10': x + 10 + col, '20': x + 10 + (2 * col),
                            '30': x + 10 + (3 * col), '40': x + 10 + (4 * col),
                            '50': x + 10 + (5 * col), '60': x + 10 + (6 * col),
                            '70': x + 10 + (7 * col), '80': x + 10 + (8 * col),
                            '90': x + 10 + (9 * col), '100': x + 10 + (10 * col)}
        # dictionary for the dB location (y) of the cursor
        self.DictCursorY = {'0%': x + 10, '10%': x + 10 + row, '20%': x + 10 + (2 * row),
                            '30%': x + 10 + (3 * row), '40%': x + 10 + (4 * row),
                            '50%': x + 10 + (5 * row), '60%': x + 10 + (6 * row),
                            '70%': x + 10 + (7 * row), '80%': x + 10 + (8 * row),
                            '90%': x + 10 + (9 * row), '100%': x + 10 + (10 * row)}

        # dictionary for the index location of the color markers
        self.DictMarcadorD = {'0': "Dmarc0", '10': "Dmarc10", '20': "Dmarc20", '30': "Dmarc30",
                              '40': "Dmarc40", '50': "Dmarc50", '60': "Dmarc60",
                              '70': "Dmarc70",
                              '80': "Dmarc80", '90': "Dmarc90", '100': "Dmarc100"}

        self.DictMarcadorI = {'0': "Imarc0", '10': "Imarc10", '20': "Imarc20", '30': "Imarc30",
                              '40': "Imarc40", '50': "Imarc50", '60': "Imarc60",
                              '70': "Imarc70",
                              '80': "Imarc80", '90': "Imarc90", '100': "Imarc100"}

        # creating columns
        self.create_line(x, x, x, x + 20 + (10 * row), fill="#808080")
        for i in range(0, 11):
            self.create_line(x + 10 + (i * col), x, x + 10 + (i * col), x + 20 + (10 * row), fill="#808080")
        self.create_line(x + 20 + (10 * col), x, x + 20 + (10 * col), x + 20 + (10 * row), fill="#808080")
        # creating rows
        self.create_line(x, x, x + 20 + (10 * col), x, fill="#808080")
        for i in range(0, 11):
            self.create_line(x, x + 10 + (i * row), x + 20 + (10 * col), x + 10 + (i * row), fill="#808080")
        self.create_line(x, x + 20 + (10 * row), x + 20 + (10 * col), x + 20 + (10 * row), fill="#808080")

        self.configure(width=60 + (10 * col), height=90 + (10 * row))

        # creating the texts inside the canvas
        self.create_text(x + 10, x + 20 + (10 * row) + 10, text="0", font=('Helvetica', 9))
        self.create_text(x + 10 + (1 * col), x + 20 + (10 * row) + 10, text="10", font=('Helvetica', 9))
        self.create_text(x + 10 + (2 * col), x + 20 + (10 * row) + 10, text="20", font=('Helvetica', 9))
        self.create_text(x + 10 + (3 * col), x + 20 + (10 * row) + 10, text="30", font=('Helvetica', 9))
        self.create_text(x + 10 + (4 * col), x + 20 + (10 * row) + 10, text="40", font=('Helvetica', 9))
        self.create_text(x + 10 + (5 * col), x + 20 + (10 * row) + 10, text="50", font=('Helvetica', 9))
        self.create_text(x + 10 + (6 * col), x + 20 + (10 * row) + 10, text="60", font=('Helvetica', 9))
        self.create_text(x + 10 + (7 * col), x + 20 + (10 * row) + 10, text="70", font=('Helvetica', 9))
        self.create_text(x + 10 + (8 * col), x + 20 + (10 * row) + 10, text="80", font=('Helvetica', 9))
        self.create_text(x + 10 + (9 * col), x + 20 + (10 * row) + 10, text="90", font=('Helvetica', 9))
        self.create_text(x + 10 + (10 * col), x + 20 + (10 * row) + 10, text="100", font=('Helvetica', 9))

        self.create_text(x - 5, x + 10 + (0 * row), text="100%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (1 * row), text="90%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (2 * row), text="80%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (3 * row), text="70%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (4 * row), text="60%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (5 * row), text="50%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (6 * row), text="40%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (7 * row), text="30%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (8 * row), text="20%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (9 * row), text="10%", font=('Helvetica', 9), anchor='e')
        self.create_text(x - 5, x + 10 + (10 * row), text="0%", font=('Helvetica', 9), anchor='e')
