from PIL import Image, ImageDraw, ImageFont

#Otevření obrázku z adresáře
#Nutno změnit adresář aby fungovalo!
img = Image.open("C:\\Users\\xboxk\\Desktop\\Python\\PillowExample\\obrazek.jpg")

#Vytvoření objektu pro kreslení na otevřený obrázek
draw = ImageDraw.Draw(img)

#Definice fontu který text bude používat a jeho velikost
font = ImageFont.truetype('arial.ttf', 36)

#Přidání textu do otevřeného obrázku
draw.text((50, 50), "Pillow příklad textu", fill=(0, 0, 0), font=font)

#Uložení nového obrázku
#Nutno změnit adresář aby fungovalo!
img.save("C:\\Users\\xboxk\\Desktop\\Python\\PillowExample\\obrazektext.jpg")
