import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MiScraper/1.0; asier.pernias@gmail.com)"}

respuesta = requests.get(url, headers=headers)
respuesta.raise_for_status()

soup = BeautifulSoup(respuesta.text, 'html.parser')

def normalizar_url(href):
    if href.startswith("/"):
        return "https://es.wikipedia.org" + href
    return href

def extraer_articulo_unico(id_div):
    div = soup.find(id=id_div)
    if div is None:
        return None
    h2 = div.find("h2")
    if h2 is None:
        return None
    enlace = h2.find("a")
    if enlace is None:
        return None
    titulo = enlace.get_text(strip=True)
    href = enlace.get("href", "")
    if not titulo or not href:
        return None
    return {"titulo": titulo, "url": normalizar_url(href)}

def extraer_lista_articulos(id_div):
    div = soup.find(id=id_div)
    if div is None:
        return []
    items = div.find_all("li")
    resultados = []
    for li in items:
        for enlace in li.find_all("a"):
            titulo = enlace.get_text(strip=True)
            href = enlace.get("href", "")
            if not titulo or not href:
                continue
            resultados.append({"titulo": titulo, "url": normalizar_url(href)})
    return resultados

secciones_unicas = {
    "Articulo destacado": "main-tfa",
    "Articulo bueno": "main-tga",
}

secciones_lista = {
    "Actualidad": "main-cur",
    "Efemerides": "main-itd",
}

for nombre, id_div in secciones_unicas.items():
    resultado = extraer_articulo_unico(id_div)
    if resultado:
        print(nombre, resultado["titulo"], resultado["url"])

for nombre, id_div in secciones_lista.items():
    resultados = extraer_lista_articulos(id_div)
    for r in resultados:
        print(nombre, r["titulo"], r["url"])