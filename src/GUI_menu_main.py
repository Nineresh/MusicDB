import tkinter as tk
import resources.style

root = tk.Tk()
root.title("Music Database 1.0")
root.geometry("800x800")
label = tk.Label(root, text="Main Menu", font=(resources.standard_font, resources.header_font_size))
label_02 = tk.Label(root, text="Message of the day:", font=(resources.standard_font, resources.header_font_size))
label.pack(padx=20, pady=0)
label_02.pack(padx=30)
textboxOne = tk.Text(root,height =2, font =(resources.standard_font_font_size, resources.header_font_size))
textboxOne.pack()

frameOne = tk.Frame(root)
frameOne.columnconfigure(0, weight=1)
frameOne.columnconfigure(1, weight=1)
frameOne.columnconfigure(2, weight=1)

btn01 = tk.Button(frameOne, text="Run local scan", font=(resources.standard_font, resources.standard_font_size))
btn01.grid(row=0, column=0, sticky=tk.W+tk.E)

btn02 = tk.Button(frameOne, text="Run cloud scan", font=(resources.standard_font, resources.standard_font_size))
btn02.grid(row=1, column=0, sticky=tk.W+tk.E)

btn03 = tk.Button(frameOne, text="Run read", font=(resources.standard_font, resources.standard_font_size))
btn03.grid(row=2, column=0, sticky=tk.W+tk.E)

btn04 = tk.Button(frameOne, text="Quit", font=(resources.standard_font, resources.standard_font_size))
btn04.grid(row=0, column=1, sticky=tk.W+tk.E)

frameOne.pack(fill="x")
# Main Loop
root.mainloop()

print("Terminal_Program ended (Exit)")