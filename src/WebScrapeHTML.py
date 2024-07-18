import requests
import logging

LOG_FORMAT = "%(Levelname)s %(asctime)s,%(message)s"

logging.basicConfig(filename="webscrape_error.log", level=logging.ERROR, format=LOG_FORMAT)
logger = logging.getLogger
url = 'https://bandcamp.com/nineresh'


response = requests.get(url)

# Check for status code 200, "the request was successful"
if response.status_code == 200:
    # Hämta HTML-koden från svaret
    html_content = response.text

    # Spara HTML-koden i en fil
    with open('resources/bandcamp_collection.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    logger.debug("Chill")
else:
    logger.error("Error; status code: " ,{response.status_code})
