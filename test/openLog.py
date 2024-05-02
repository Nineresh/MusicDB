import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Opener")
        
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)

    def open_file(self):
        file_path = r"C:\Users\andre\Documents\Project\musicDB\resources\read.log"  # Ange den specifika filvägen här
        try:
            with open(file_path, 'r') as file:
                # Läs innehållet i filen om du vill göra något med det
                content = file.read()
                print(content)
        except Exception as e:
            print("Error:", e)

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
