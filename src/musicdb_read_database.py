import sqlite3
import logging
def main():
       # Logging section
    LOG_FORMAT = ("%(asctime)s, %(lineno)d, %(levelname)s, %(message)s")
    logging.basicConfig(filename="resources/read.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=LOG_FORMAT)
    logger = logging.getLogger()
    def read():
        conn = sqlite3.connect("database/musicdatabase.db")
        c = conn.cursor()

        c.execute("SELECT * FROM tracks")

        rows = c.fetchall()
        count=0
        for k in rows:
            logger.debug(k)
            count +=1

        conn.close()
        logger.debug(count)
    read()
    
if __name__ == "__main__":
    main()