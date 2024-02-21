import database
import sqlite3
import os
import glob
import eyed3
import logging

#Logging section
LOG_FORMAT = ("%(asctime)s, %(lineno)d, %(levelname)s, %(message)s")
logging.basicConfig(filename="test_main.log",
                    level=logging.DEBUG,
                    filemode="w",
                    format=LOG_FORMAT)
logger = logging.getLogger()

#Create list of subfolders
def lista_mappar(target_folder):
    submappar = []
# Använder 'os'-bibloteket för att läsa av alla submappar i argumentet
# sökvägen som läses in.
    for k in os.listdir(target_folder): 
        submappar.append(k)
#returnerar en lista som innehåller alla submappar
    return submappar

# This function takes path to the mp3 file and read its meta data.
# Should this function also INSERT?
def read_mp3_metadata(file_path):
    audiofile = eyed3.load(file_path)
    
    
    if audiofile.tag:
        print("File:", file_path)
        print("Title:", audiofile.tag.title)
        print("Artist:", audiofile.tag.artist)
        print("Album:", audiofile.tag.album)
        print("Year:", audiofile.tag.getBestDate())
        
    else:
        print("No metadata found for file:", file_path)
# Connecting to database, refrence in database.py
connection = database.connect()

def lista_mp3(pathway):
    mp3_files = []
    for k in glob.glob(os.path.join(pathway, "*.mp3")):
        mp3_names = os.path.basename(k)
        logger.debug(os.path.basename(k))
        mp3_files.append(mp3_names)
    return mp3_files
    
if __name__ == "__main__":
    #Constant varibels with static pathways
    pathwayToMusic = "/Users/andreaslindblad/documents/musik"
    addTheSlash = "/"
    #List containing subfolders in /musik/
    out_submappar = lista_mappar(pathwayToMusic)
    
    #read_mp3_metadata(pathwayToMusic + addTheSlash + "Batushka - Litourgiya/Batushka - Yekteniya I.mp3")
    for k in range (len(out_submappar)):

        lista_mp3(pathwayToMusic+addTheSlash+out_submappar[k])