from tkinter import *
from tkinter import ttk
import time
import requests

url = "https://alpha-vantage.p.rapidapi.com/query"
headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "8668b5ea1emsh169c17e6f62fa97p1a4b8fjsn71477ee0f336"
}


class application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.market = IntVar()
        self.market.set(1)
        self.sym = 'ADA'
        self.interval = "5min"
        self.input1 = ttk.Entry(self.master)
        self.create_stuff()

    def create_stuff(self):
        Label(root,
              text="""Market:""",
              justify=LEFT).pack(anchor=W)
        ttk.Radiobutton(root,
                        text="crypto",
                        variable=self.market,
                        value=1).pack(anchor=W)

        ttk.Radiobutton(root,
                        text="stock",
                        variable=self.market,
                        value=2).pack(anchor=W)

        self.input1.pack(anchor=W)
        ttk.Button(root,
                   text="find",
                   command=self.update).pack(anchor=W)

    def update(self):
        sym = self.input1.get()
        m = self.market.get()
        print(sym, m)

    def new(self):
        pass

    def watch(self):
        querystring = {"interval": self.interval, "function": "TIME_SERIES_INTRADAY",
                       "symbol": "MSFT", "datatype": "json", "output_size": "compact"}
        res = requests.request("GET", url, headers=headers, params=querystring)
        print(res.text)


if __name__ == '__main__':
    root = Tk(className=' Ticker')
    root.geometry("280x150")
    app = application(master=root)
    app.mainloop()
