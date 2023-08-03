from PIL import Image, ImageFilter

img = Image.open("./images/4.1 pikachu.jpg.jpg")
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save("yyyy.png", "png")