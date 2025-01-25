from PIL import Image 
import random  

width, height = 23040, 12960 
image = Image.new("RGBA", (width, height))  # 画像の各ピクセルをランダムな色に設定 

for y in range(height):
for x in range(width):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  a = random.randint(0, 255)
  image.putpixel((x, y), (r, g, b, a))  
image.save("random_24K_image.png")
