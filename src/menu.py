import tkinter as tk
import localscan

class MyMenu:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Music Database 1.0")
        self.root.geometry("500x600")


        self.label = tk.Label(self.root, text="Message", font=("Ariel", 20))


        self.btn01 = tk.Button(self.root, text="Run local scan",font=("Ariel", 18), command=self.runLocalScan)
        self.btn02 = tk.Button(self.root, text="Quit",font=("Ariel", 18), command=self.exit)

        self.btn01.pack(padx=10,pady=10)
        self.btn02.pack(padx=10,pady=10)


        self.root.mainloop()

        
    def runLocalScan(self):
       localscan.main()

    def exit(self):
        self.root.quit()
MyMenu()

