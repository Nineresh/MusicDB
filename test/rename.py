
import os
import logging
# Logging section
LOG_FORMAT = ("%(asctime)s, %(lineno)d, %(levelname)s, %(message)s")
logging.basicConfig(filename="resources/test_rename.log",
                    level=logging.INFO,
                    filemode="w",
                    format=LOG_FORMAT)
logger = logging.getLogger()
def rename_files(folder_path):
    # Lista för att hålla reda på alla filer i mappen
    files_to_rename = os.listdir(folder_path)
    
    # Loopa tills det inte finns fler filer att bearbeta
    while files_to_rename:
        # Ta bort det första elementet i listan och använd det som filnamn
        filename = files_to_rename.pop(0)
        
        # Skapa den fullständiga sökvägen till filen
        filepath = os.path.join(folder_path, filename)
        
        # Kontrollera om det är en fil (inte en mapp)
        if os.path.isfile(filepath):
            # Dela upp filnamnet i ord
            filename_parts = filename.split()
            
            # Kontrollera om filnamnet innehåller flera ord
            if len(filename_parts) > 1:
                
                # Extrahera det sista ordet
                new_filename = filename_parts[-1]
                
                # Skapa den nya filens fullständiga sökväg
                new_filepath = os.path.join(folder_path, new_filename)
                
                # Byt namn på filen
                os.rename(filepath, new_filepath)
                
                logger.info(f"Filnamn ändrat från '{filename}' till '{new_filename}'")
            else:
               logger.info(f"Ignorerar fil '{filename}' eftersom det bara innehåller ett ord.") 

# Ange sökvägen till mappen som innehåller filerna du vill ändra namn på
folder_path = r"C:\Users\andre\Documents\Obsidian Vault Local\ALVL\Music\Ithildin - Arda's Herbarium- A Musical Guide to the Mystical Garden of Middle Earth and Stranger Places - Vol. III"

# Anropa funktionen för att ändra filnamn
rename_files(folder_path)
