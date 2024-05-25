import sqlite3
def main():
    def remove():
        conn = sqlite3.connect("database/musicdatabase.db")

        cursor = conn.cursor()
    #Table remains but ALL data i wiped
        cursor.execute("DELETE FROM tracks")

        conn.commit()

        conn.close()

    print("Starting")
    remove()
    print("Data is removed")



if __name__ == "__main__":
    main()