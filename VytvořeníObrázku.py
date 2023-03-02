from PIL import Image

#Vytvoření nového obrázku s bílým pozadím
#Přepsáním 500, 500 změníte rozměr vytvořeného obrázku
#Přepsáním color = (255, 255, 255) změníte barvu pozadí obrázku . Používejte RGB!
img = Image.new('RGB', (500, 500), color = (255, 255, 255))

#Uložení nového obrázku
#Nutno změnit adresář aby fungovalo!
img.save("C:\\Users\\xboxk\\Desktop\\Python\\PillowExample\\obrazek.jpg")

