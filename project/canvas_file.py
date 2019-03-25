
class FigureCanvas(tk.Canvas):

    def __init__(self, x, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #x = 40  # sets the origin of the table as (x,x)
        self.config(bg="#ffffff")

        col=60 # width of the column
        row=26 # height of the row

        # Dictionary for the frequency location (x) of the cursor
        self.DictCursorX = {'125 Hz': x + 10, '250 Hz': x + 10 + col, '500 Hz': x + 10 + (2 * col),
                            '750 Hz': x + 10 + (2.5 * col), '1000 Hz': x + 10 + (3 * col),
                            '1500 Hz': x + 10 + (2.5 * col) + col, '2000 Hz': x + 10 + (4 * col),
                            '3000 Hz': x + 10 + (2.5 * col) + (2 * col), '4000 Hz': x + 10 + (5 * col),
                            '6000 Hz': x + 10 + (2.5 * col) + (3 * col), '8000 Hz': x + 10 + (6 * col)}
        # Dictionary for the dB location (y) of the cursor
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

        # Dictionary for the index location of the color markers
        self.DictMarkerR={'125 Hz': "Rmark125", '250 Hz': "Rmark250", '500 Hz': "Rmark500",
                          '750 Hz': "Rmark750", '1000 Hz': "Rmark1000", '1500 Hz': "Rmark1500",
                          '2000 Hz': "Rmark2000", '3000 Hz': "Rmark3000", '4000 Hz': "Rmark4000",
                          '6000 Hz': "Rmark6000", '8000 Hz': "Rmark8000"}
        self.DictMarkerL={'125 Hz': "Lmark125", '250 Hz': "Lmark250", '500 Hz': "Lmark500",
                          '750 Hz': "Lmark750", '1000 Hz': "Lmark1000", '1500 Hz': "Lmark1500",
                          '2000 Hz': "Lmark2000", '3000 Hz': "Lmark3000", '4000 Hz': "Lmark4000",
                          '6000 Hz': "Lmark6000", '8000 Hz': "Lmark8000"}
