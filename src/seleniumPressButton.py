from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Ange sökvägen till din WebDriver
driver_path = 'path/to/chromedriver'

# Skapa en ny instance av Chrome WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Gå till önskad webbsida
    driver.get('URL_TILL_HEMSIDAN')

    # Vänta lite för att se till att sidan laddas (kan justeras eller användas mer avancerade väntemetoder)
    time.sleep(3)

    # Hitta knappen. Anta att vi letar efter en knapp med id 'myButton'
    button = driver.find_element(By.ID, 'myButton')

    # Klicka på knappen
    button.click()

    # Vänta lite för att se vad som händer efter klicket
    time.sleep(3)
    
finally:
    # Stäng webbläsaren
    driver.quit()
