from PIL import Image, ImageFilter

<<<<<<< HEAD
img = Image.open("./images/4.1 pikachu.jpg.jpg")
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save("yyyy.png", "png")
=======
img = Image.open("images/6.1 astro.jpg.jpg")
new_img = img.resize((400, 400))
new_img.save('thumbnail.jpg')
>>>>>>> 5b7b2ac6867cb8a6b1b23c2908d866b3f89b4d24
