from PIL import Image

virus_image = Image.open("images/virus.jpg")
virus_image = virus_image.convert('RGBA')
newImage = []
for item in virus_image.getdata():
    if item[:3] == (255, 255, 255):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

virus_image.putdata(newImage)
virus_image.save('output.png')