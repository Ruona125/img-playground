from PIL import Image, ImageFilter

img = Image.open("images/6.1 astro.jpg.jpg")
new_img = img.resize((400, 400))
new_img.save('thumbnail.jpg')