import random
NOMBREARCHIVO="pablrasingles.txt"
def cargar_archivo():
    with open(NOMBREARCHIVO, "r", encoding="utf-8") as Archivos:
        return [line.strip().upper() for line in Archivos]
def btener_palabra_aleatoria(Palabras):
    return random.choice(Palabras)   
Total_Palabras = cargar_archivo()
palabra_aleatoria = btener_palabra_aleatoria(Total_Palabras)
print (palabra_aleatoria)
