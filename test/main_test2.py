import sqlite3
import os
import glob
import eyed3
import logging
print("Starting")
#Logging section
LOG_FORMAT = ("%(asctime)s, %(lineno)d, %(levelname)s, %(message)s")
logging.basicConfig(filename="test_main.log",
                    level=logging.DEBUG,
                    filemode="w",
                    format=LOG_FORMAT)
logger = logging.getLogger()

#Database section
conn = sqlite3.connect("test_musicdatabase.db")
c = conn.cursor()

logger.debug("Starting program")
#Subfolder is a list of subfolders in musik
subfolder = []
for k in os.listdir("/Users/andreaslindblad/documents/musik"): 
    subfolder.append(k)


for folder in range (0,len(subfolder)):
    mp3_path= glob.glob(os.path.join("/Users/andreaslindblad/documents/musik/"+subfolder[folder], "*.mp3"))
    for mp3 in mp3_path:
        audiofile = eyed3.load(mp3)
        c.execute("""INSERT INTO tracks(title, album, artist) VALUES (?,?,?)""",(audiofile.tag.title, audiofile.tag.album, audiofile.tag.artist))
        print("Added:")
        print("Track: "+ audiofile.tag.title)
        print("Album: "+ audiofile.tag.album)
        print("Artist: "+ audiofile.tag.artist)
        #print("Year: "+ audiofile.tag.best_release_date)
        conn.commit()
conn.close()
print("Ending")
logger.debug("Ending")