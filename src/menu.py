import tkinter as tk
import localscan
import removeData
import read
from tkinter import filedialog



class MyMenu:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Music Database 1.0")
        self.root.geometry("500x600")


        self.label = tk.Label(self.root, text="Message", font=("Ariel", 20))

        # Run local scan
        self.btnScan = tk.Button(self.root, text="Run local scan",font=("Ariel", 18), command=self.runLocalScan)
        # Remove 
        self.btnRemove = tk.Button(self.root, text="Remove data",font=("Ariel", 18), command=self.remove)
        self.btnRead = tk.Button(self.root, text="Read",font=("Ariel", 18), command=self.read)
        # Quit
        self.btnExit = tk.Button(self.root, text="Quit",font=("Ariel", 18), command=self.exit)

        self.btnScan.pack(padx=15,pady=15)
        self.btnRead.pack(padx=10, pady=10)
        self.btnRemove.pack(padx=10,pady=10)
        self.btnExit.pack(padx=10,pady=10)


        self.root.mainloop()


    def runLocalScan(self):
       localscan.main()
    def exit(self):
        self.root.quit()
    def remove(self):
        removeData.main()
    def read(self):
        read.main()
MyMenu()

