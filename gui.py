import tkinter as tk
import tkinter.ttk


countries = {"Google Cloud": ['China ', 'Taiwan ', 'Japan ', 'India ', 'Singapore ', 'Australia ', 'Finland ', 'Belgium ', 'United Kingdom ', 'Germany ', 'Netherlands ', 'Switzerland ', 'Canada ', 'Brazil ', 'USA '],
             "Amazon Web Service": ['USA ', 'China ', 'India ', 'Japan ', 'South Korea ', 'Singapore ', 'Australia ', 'Canada ', 'Germany ', 'Ireland ', 'United Kingdom ', 'France ', 'Sweden ', 'Brazil '],
             "Azure": ['Hong Kong ', 'Singapore ', 'USA ', 'Ireland ', 'Netherlands ', 'Japan ', 'Brazil ', 'Australia ', 'India ', 'Canada ', 'United Kingdom ', 'South Korea ', 'France ', 'South Africa ']}
hardware = ['RTX 2080 Ti', 'RTX 2080', 'GTX 1080 Ti', 'GTX 1080', 'AMD RX480', 'Titan ValueError(', 'Tesla V100-SXM2-32GB', 'Tesla V100-SXM2-16GB', 'Tesla P100', 'Tesla K40c', 'Tesla K80', 'TPU2', 'TPU3',
            'Intel Xeon E5-2699', 'AGX Xavier', 'GTX TITAN X', 'TITAN X Pascal', 'T4', 'Titan RTX', 'RTX 8000', 'GTX 750', 'Quadro K6000', 'Quadro P6000', 'Tesla M40 24GB', 'Tesla V100-PCIE-16GB', 'Titan Xp']


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.hardware_var = tk.StringVar()
        self.country_var = tk.StringVar()
        self.cloudprovider_var = tk.StringVar()
        self.hour_var = tk.StringVar()
        self.min_var = tk.StringVar()
        self.sec_var = tk.StringVar()
        self.title('Carbon Meter')
        self.create_main_widgets()

    def update_countries(self, event=None):
        self.CountryCombo['values'] = countries[self.CloudCombo.get()]

    def create_main_widgets(self):
        headingLabel = tk.Label(self, text="Carbon Meter", font="Roboto 12")
        headingLabel.grid(row=0, column=0, columnspan=5,
                          padx=10, pady=10, sticky="w")
        tkinter.ttk.Separator(self, orient="horizontal").grid(
            row=1, column=0, columnspan=5, sticky='ew')

        tk.Label(self, text="HARDWARE: ").grid(
            row=2, column=0, padx=(10, 0))
        self.HardwareCombo = tkinter.ttk.Combobox(
            self, width=15, values=hardware, state="readonly", textvariable=self.hardware_var)
        self.HardwareCombo.set("SELECT HARDWARE")
        self.HardwareCombo.grid(row=2, column=1)

        tk.Label(self, text="Cloud Provider: ").grid(
            row=2, column=2, padx=(10, 0))
        self.CloudCombo = tkinter.ttk.Combobox(
            self, width=15, values=list(countries.keys()), state="readonly", textvariable=self.cloudprovider_var)
        self.CloudCombo.set("SELECT CLOUD PROVIDER")
        self.CloudCombo.bind('<<ComboboxSelected>>', self.update_countries)
        self.CloudCombo.grid(row=2, column=3)

        tk.Label(self, text="COUNTRY: ").grid(row=2, column=4, padx=(10, 0))
        self.CountryCombo = tkinter.ttk.Combobox(
            width=15, state="readonly", textvariable=self.country_var)
        #self.CountryCombo.bind('<<ComboboxSelected>>', self.taketimeinput)
        self.CountryCombo.set("SELECT COUNTRY")
        self.CountryCombo.grid(row=2, column=5, padx=(0, 10))

        tkinter.ttk.Separator(self, orient="horizontal").grid(
            row=3, column=0, columnspan=5, sticky='ew')


app = Application()
app.mainloop()
