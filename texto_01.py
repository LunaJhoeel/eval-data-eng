import string
from pprint import pprint

# texto proporcionado
texto = """
Los ingenieros de datos transforman, organizan y almacenan datos en bases de\n
datos. También construyen y mantienen las estructuras de datos y las\n
arquitecturas tecnológicas necesarias para el procesamiento, ingestión e\n
implementación a gran escala de aplicaciones que usan datos de manera \n
intensiva.
"""

# limpia el texto
texto = texto.lower()
# remueve puntuación
texto = texto.translate(str.maketrans('', '', string.punctuation))
# divide en palabras
palabras = texto.split()

# cuenta las ocurrencias 
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# muestra el diccionario estructurado
pprint(conteo_palabras)