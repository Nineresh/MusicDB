import sqlite3
import os
import glob
import eyed3
import logging

def main():
    print("Starting")

    # Logging section
    LOG_FORMAT = ("%(asctime)s, %(lineno)d, %(levelname)s, %(message)s")
    logging.basicConfig(filename="resources/main.log",
                        level=logging.INFO,
                        filemode="w",
                        format=LOG_FORMAT)
    logger = logging.getLogger()

    count_track = 0
    count_album = 0
    list_album = []
    count_artist = 0
    list_artist = []

    # Database section
    conn = sqlite3.connect("database/musicdatabase.db")
    c = conn.cursor()

    logger.debug("Starting program")

    # Subfolder is a list of subfolders in musik
    subfolder = []
    for k in os.listdir(r"C:\Users\andre\Documents\Obsidian Vault Local\ALVL\Music"): 
        subfolder.append(k)
    logger.debug(subfolder)

    for folder in range (0,len(subfolder)):
        
        mp3_path = glob.glob(os.path.join(r"C:\Users\andre\Documents\Obsidian Vault Local\ALVL\Music", subfolder[folder], "*.mp3"))

        logger.debug(mp3_path)
        for mp3 in mp3_path:
            audiofile = eyed3.load(mp3)
            # Get tags in a varibel
            tag = audiofile.tag
            logger.info(mp3)

            # Use the GetBestDate method. ISSUE TO BE FIXED
            year_tag = tag.getBestDate()
            string_year = str(year_tag)

            # Check if the track already exists in the database
            c.execute("""SELECT * FROM tracks WHERE title=? AND album=? AND artist=?""",
                    (audiofile.tag.title, audiofile.tag.album, audiofile.tag.artist))
            existing_track = c.fetchone()

            if not existing_track:
                c.execute("""INSERT INTO tracks(title, album, artist, year) VALUES (?,?,?,?)""",
                        (audiofile.tag.title, audiofile.tag.album, audiofile.tag.artist, string_year))
                print("Added:")
                print("Track: " + audiofile.tag.title)
                count_track += 1
                print("Album: " + audiofile.tag.album)
                if audiofile.tag.album not in list_album:
                    list_album.append(audiofile.tag.album)
                    count_album += 1
                else:
                    pass
                print("Artist: " + audiofile.tag.artist)

                if audiofile.tag.artist not in list_artist:
                    list_artist.append(audiofile.tag.artist)
                    count_artist += 1
                else:
                    pass

                print("Year: " + string_year)
                conn.commit()
            else:
                print("Track already exists: " + audiofile.tag.title)

    conn.close()
    print("You added:")
    print(count_track, " tracks")
    print(count_album, " albums")
    print(count_artist, " artists")

    

if __name__ == "__main__":
    main()