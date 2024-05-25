import requests

# Ange URL:en till den webbplats du vill hämta HTML-koden från
url = 'https://bandcamp.com/nineresh'

# Skicka en GET-förfrågan till URL:en
response = requests.get(url)

# Kontrollera om förfrågan var framgångsrik (statuskod 200)
if response.status_code == 200:
    # Hämta HTML-koden från svaret
    html_content = response.text

    # Spara HTML-koden i en fil
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print('HTML-koden har sparats i filen "webpage.html".')
else:
    print(f'Misslyckades att hämta HTML-koden. Statuskod: {response.status_code}')
