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
# It then inserts
def insert_mp3_metadata(out_submappar,pathwayToMusic,addTheSlash):
    conn = sqlite3.connect("test_musicdatabase.db")
    c = conn.cursor()

    for k in range (0,len(out_submappar)):
        file_path= lista_mp3(pathwayToMusic+addTheSlash+out_submappar[k])
        
        audiofile = eyed3.load(file_path)
        logger.debug(audiofile.tag.title, audiofile.tag.album, audiofile.tag.artist, audiofile.tag.getBestDate)
        if audiofile.tag:
            c.execute("""INSERT INTO tracks (title, album, artist,year)VALUES(?,?,?,?)""",(audiofile.tag.title,audiofile.tag.album,audiofile.tag.artist,audiofile.tag.getBestDate))
            conn.commit()
        else:
            logger.debug("Error on INSERT")
    conn.close()
# Connecting to database, refrence in database.py
connection = database.connect()

def lista_mp3(pathway):
    mp3_files = []
    for k in glob.glob(os.path.join(pathway, "*.mp3")):
        logger.debug(os.path.basename(k))
        mp3_files.append(k)
    return mp3_files

def create_database_and_table():
    conn = sqlite3.connect("test_musicdatabase.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tracks(
                id INTERGER PRIMARY KEY,
              title TEXT,
              album TEXT,
              artist TEXT,
              year INTERGER) 
    """)
    conn.commit()
    conn.close()
if __name__ == "__main__":

    
    print("Welcome")
    logger.debug("Welcome")
    create_database_and_table()
    #Constant varibels with static pathways
    pathwayToMusic = "/Users/andreaslindblad/documents/musik"
    addTheSlash = "/"
    #List containing subfolders in /musik/
    out_submappar = lista_mappar(pathwayToMusic)
    insert_mp3_metadata(out_submappar,pathwayToMusic,addTheSlash)
    
    print("Good bye")