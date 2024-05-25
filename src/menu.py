import tkinter as tk
import musicdb_search_local
import musicdb_remove_database
import musicdb_read_database



class MyMenu:
    def __init__(self) -> None:
        # Window config
        self.root = tk.Tk()
        self.root.title("Music Database 1.0")
        self.root.geometry("500x600")

        deliver = "Hello"
        self.label = tk.Label(self.root, text="Main Menu", font=("Ariel", 20))
        self.label.pack()
        self.textboxUpdate = tk.Text(self.root, height=5, width=20)
        
        # Run local scan
        self.btnScan = tk.Button(self.root, text="Run local scan",font=("Ariel", 18), command=self.runLocalScan)
        # Remove 
        self.btnRemove = tk.Button(self.root, text="Remove data",font=("Ariel", 18), command=self.remove)
        # Read to .log
        self.btnRead = tk.Button(self.root, text="Read",font=("Ariel", 18), command=self.read)
        # Quit
        self.btnExit = tk.Button(self.root, text="Quit",font=("Ariel", 18), command=self.exit)

        self.btnScan.pack(padx=25,pady=25)
        self.btnRead.pack(padx=25, pady=25)
        self.btnRemove.pack(padx=25,pady=25)
        self.btnExit.pack(padx=25,pady=25)
        self.textboxUpdate.place(x=50, y=450)

        self.root.mainloop()


    def runLocalScan(self):
        musicdb_search_local.main()
        text_to_display = f"""You added:)
    (count_track, " tracks")
    (count_album, " albums")
    (count_artist, " artists")"""
        self.textboxUpdate.insert(tk.END, text_to_display + "\n")
    def exit(self):
        self.root.quit()
    def remove(self):
        text_to_display = "Data is removed"
        self.textboxUpdate.insert(tk.END, text_to_display + "\n")
        
        musicdb_remove_database.main()
    def read(self):
        musicdb_read_database.main()
MyMenu()

