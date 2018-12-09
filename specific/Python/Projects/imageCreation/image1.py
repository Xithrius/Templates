# draw images
# variable = image.open('path')

from PIL import Image, ImageDraw

background = Image.new('RGB', (1000, 1000), color='white')
zoidBerg = Image.open('img/zoidBerg.png')

background_copy = background.copy()

position = (100, 100)

background_copy.paste(zoidBerg, position)
background_copy.save('img/zoid.png')
