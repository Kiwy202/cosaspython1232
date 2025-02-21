import requests
from bs4 import BeautifulSoup

url = 'https://desarrolloweb.com/home/html'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    parrafos = soup.find_all('p')

    for parrafo in parrafos:
        texto = parrafo.get_text(strip=True) 
        if texto.startswith("HTML"):
            print(texto)
            break 
else:
    print(f"Hubo un error: {respuesta.status_code}")


