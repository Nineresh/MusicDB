import tkinter as tk
import musicdb_search_local
import musicdb_remove_database
import musicdb_read_database
import resources.style
import resources.tkstyle



class MyMenu:
    def __init__(self) -> None:
        # Window config
        self.root = tk.Tk()
        self.root.title(resources.tkstyle.root_title)
        self.root.geometry(resources.tkstyle.root_geometry)
        self.root.columnconfigure(0, weight=1)

        
        self.label = tk.Label(self.root, text="Main Menu", font=(resources.style.standard_font, resources.style.header_font_size))
        
        self.label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        # Main menu
        # Run local scan
        self.btnScan = tk.Button(self.root, text="Run local scan",height= 1, width= 12,font=(resources.style.standard_font, resources.style.standard_font_size), command=self.runLocalScan)
        # Remove data
        self.btnRemove = tk.Button(self.root, text="Remove data",height= 1, width= 12,font=(resources.style.standard_font, resources.style.standard_font_size), command=self.remove)
        # Read to .log
        self.btnRead = tk.Button(self.root, text="Read",height= 1, width= 12,font=(resources.style.standard_font, resources.style.standard_font_size), command=self.read)
        # Quit
        self.btnExit = tk.Button(self.root, text="Quit",height= 1, width= 12,font=(resources.style.standard_font, 18), command=self.exit)

        # Status bar
        self.status_bar = tk.Canvas(self.root, width=200, height=200)
        self.database_check = self.status_bar.create_oval( 50, 50,100,100)

        

        self.btnScan.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.btnRead.grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.btnRemove.grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.btnExit.grid(row=4, column=0, sticky="e", padx=10, pady=10)

        self.root.mainloop()


    def runLocalScan(self):
        musicdb_search_local.main()
        
    def exit(self):
        self.root.quit()
    def remove(self):
        
        
        musicdb_remove_database.main()
    def read(self):
        
        musicdb_read_database.main()


        
MyMenu()

