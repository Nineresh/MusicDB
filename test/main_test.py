import database
import os
def main():
    pass
#Create list of subfolders
def lista_mappar(target_folder):
    submappar = []
# Använder 'os'-bibloteket för att läsa av alla submappar i argumentet
# sökvägen som läses in.
    for k in os.listdir(target_folder):
        
        submappar.append(k)
#returnerar en lista som innehåller alla submappar
    return submappar

# Connecting to database, refrence in database.py
connection = database.connect()

if __name__ == "__main__":
    pass
